from flask import Flask, render_template
import requests

app = Flask(__name__)  

def get_meme():
    # Public API that returns a random post from a subreddit as JSON
    url = "https://meme-api.com/gimme/wholesomememes"
    reponse = requests.get(url,timeout=10)
    data = reponse.json()
    return data["url"], data["subreddit"]


@app.route("/")
def index():
    meme_url, subreddit = get_meme()
    return render_template("index.html", meme_url=meme_url, subreddit=subreddit)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


