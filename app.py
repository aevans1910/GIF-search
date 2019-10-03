import os

from dotenv import load_dotenv
load_dotenv() 

TENOR_API_KEY = os.getenv("TENOR_API_KEY")

from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    """Return homepage."""
    # Testing
    print("entered route")
    # Extracting the query term from url using request.args.get()
   
    term = request.args.get('search')

    # Making 'params' dictionary containing the query term, our API key, 'key', and how many GIFs to return, 'limit'

    params = {"q": term, "key": TENOR_API_KEY, 'limit': 10}
    gifs = None

    # Making an API call to Tenor using the 'requests' library. 
    r = requests.get("https://api.tenor.com/v1/search", params)

    # Using the '.json()' function to get the JSON of the returned response
    # object
    if r.status_code == 200:
        gifs = r.json()

    # Using dictionary notation, get the 'results' field of the JSON,
    # which contains the GIFs as a list
    results = gifs["results"]
    print (results)

    # Rendered the 'index.html' template, passing the list of gifs as a
    # named parameter called 'gifs'

    return render_template(
        "index.html",
        gifs=results)

if __name__ == '__main__':
    app.run(debug=True)