# Create README.md file for download

readme_content = """
# Custom CTF (Capture The Flag) Platform

## Short Description
A web-based Capture The Flag platform with challenges (web, crypto, reversing, forensics) and a scoreboard system for gamified cybersecurity learning.

---

## Folder Structure
Custom_CTF_Platform/
│
├── app.py
├── run.py
├── requirements.txt
├── README.md
├── database.db
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── scoreboard.html
│   └── challenge.html
│
├── static/
│   ├── css/style.css
│   └── js/scripts.js
│
└── challenges/
    ├── web/challenge1.json
    ├── crypto/challenge1.json
    ├── reversing/challenge1.json
    └── forensics/challenge1.json

---

## Features
- User registration & login
- Web, Crypto, Reversing, Forensics challenges
- Live scoreboard system
- Polished web UI
- SQLite database (no Docker required)
- Easy challenge creation using JSON
- Beginner-friendly CTF learning platform

---

## Installation & Setup

1. Clone the repository
git clone https://github.com/shahdevam8/Custom-CTF-Platform
cd Custom_CTF_Platform

2. Create virtual environment
python -m venv venv

3. Activate virtual environment
Windows:
venv\\Scripts\\activate
Linux/Mac:
source venv/bin/activate

4. Install dependencies
pip install -r requirements.txt

5. Run the application
python run.py

Open browser:
http://127.0.0.1:5000

---

## How to Use

1. Register a new account
2. Login with credentials
3. Browse challenges by category
4. Solve challenges and submit flags
5. Earn points and track progress on scoreboard

---

## Challenge Format Example
{
  "title": "Basic Web Challenge",
  "description": "Find the hidden flag in page source",
  "category": "web",
  "points": 50,
  "flag": "FLAG{hidden_flag}",
  "hint": "View Page Source"
}

---

## Learning Outcomes
- Hands-on cybersecurity practice
- Understanding CTF environments
- Secure coding exposure
- Gamified security learning
