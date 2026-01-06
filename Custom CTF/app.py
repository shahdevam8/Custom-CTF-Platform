from flask import Flask, render_template, request, redirect, session, url_for
import sqlite3
import os

app = Flask(__name__)
app.secret_key = "ctf_secret_key"

DB = "database.db"

# ------------------ DATABASE ------------------

def init_db():
    conn = sqlite3.connect(DB)
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT,
        score INTEGER DEFAULT 0
    )
    """)

    c.execute("""
    CREATE TABLE IF NOT EXISTS challenges (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        category TEXT,
        flag TEXT,
        points INTEGER
    )
    """)

    # Insert challenges once
    c.execute("SELECT COUNT(*) FROM challenges")
    if c.fetchone()[0] == 0:
        challenges = [
            ("Basic SQLi", "Web", "flag{sql_injection}", 100),
            ("Base64 Decode", "Crypto", "flag{crypto_fun}", 50),
            ("Hidden Strings", "Reversing", "flag{reverse_it}", 150),
            ("Image Metadata", "Forensics", "flag{meta_found}", 75)
        ]
        c.executemany("INSERT INTO challenges VALUES (NULL,?,?,?,?)", challenges)

    conn.commit()
    conn.close()

# ------------------ ROUTES ------------------

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=["GET","POST"])
def register():
    if request.method == "POST":
        user = request.form["username"]
        pwd = request.form["password"]

        conn = sqlite3.connect(DB)
        c = conn.cursor()
        try:
            c.execute("INSERT INTO users (username,password) VALUES (?,?)", (user,pwd))
            conn.commit()
        except:
            return "Username already exists"
        conn.close()
        return redirect("/login")
    return render_template("register.html")

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        user = request.form["username"]
        pwd = request.form["password"]

        conn = sqlite3.connect(DB)
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE username=? AND password=?", (user,pwd))
        result = c.fetchone()
        conn.close()

        if result:
            session["user"] = user
            return redirect("/challenges")
        return "Invalid credentials"

    return render_template("login.html")

@app.route("/challenges", methods=["GET","POST"])
def challenges():
    if "user" not in session:
        return redirect("/login")

    conn = sqlite3.connect(DB)
    c = conn.cursor()

    if request.method == "POST":
        cid = request.form["cid"]
        submitted_flag = request.form["flag"]

        c.execute("SELECT flag,points FROM challenges WHERE id=?", (cid,))
        real_flag, points = c.fetchone()

        if submitted_flag == real_flag:
            c.execute("UPDATE users SET score = score + ? WHERE username=?",
                      (points, session["user"]))
            conn.commit()

    c.execute("SELECT * FROM challenges")
    challenges = c.fetchall()
    conn.close()

    return render_template("challenges.html", challenges=challenges)

@app.route("/scoreboard")
def scoreboard():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("SELECT username,score FROM users ORDER BY score DESC")
    users = c.fetchall()
    conn.close()
    return render_template("scoreboard.html", users=users)

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

# ------------------ MAIN ------------------

if __name__ == "__main__":
    init_db()
    app.run(debug=True)