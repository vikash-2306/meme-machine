Meme Machine

A small Flask web app that fetches a random meme from Reddit (through a public meme API) and shows it in a meme-themed page that refreshes every 30 seconds.

Built while following NetworkChuck's Flask + Python + APIs tutorial, then extended with my own custom UI themes.

Features
Flask backend that calls a meme API with requests
Jinja2 template that receives the meme URL and subreddit from Python
Auto-refresh every 30 seconds with a live countdown
Retro "MemeOS 98" theme: fake error popups, "Press F" counter, bonk-the-meme click, stock ticker, emoji rain
Alternate meme-style theme with animated backgrounds and a glitch title
Screenshots

Add screenshots here (put images in a screenshots/ folder).

Tech stack
Python 3
Flask
Requests
HTML, CSS, vanilla JavaScript
Project structure
meme_project/
├── meme_flask.py        # Flask app + API call
├── requirements.txt
├── templates/
│   └── meme_index.html  # Page template
└── README.md
Run it locally (Windows)
bash
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python meme_flask.py

Then open http://127.0.0.1:5000 in your browser.

On macOS/Linux, activate the venv with source venv/bin/activate and use python3.

How it works
meme_flask.py defines a route for /.
On each request it calls the meme API and gets the image URL and subreddit.
render_template passes meme_url and subreddit into the HTML.
The page reloads every 30 seconds, which fetches a new meme.
Notes
To change the subreddit, edit the URL inside get_meme().
Some subreddits can return content that is not safe for work. Pick the subreddit with that in mind.
Flask's built-in server is for development only. For deployment use a production server such as gunicorn.
Credits

Tutorial inspiration: NetworkChuck, "Flask + Python + APIs" on YouTube.

Ideas for next steps
Subreddit dropdown
"Next meme" button without a full page reload
Deploy to Render or PythonAnywhere