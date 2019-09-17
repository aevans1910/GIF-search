from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    """Return homepage."""
    # Test
    print("entered route")
    # TODO: Extract the query term from url using request.args.get()
    term = request.args.get('term')

    # TODO: Make 'params' dictionary containing:
    # a) the query term, 'q'
    # b) your API key, 'key'
    # c) how many GIFs to return, 'limit'

    params = {"q": term, "key": "BG41AB43M6OC", 'limit': 1}
    gifs = None

    # TODO: Make an API call to Tenor using the 'requests' library. For 
    # reference on how to use Tenor, see: 
    # https://tenor.com/gifapi/documentation
    r = requests.get("https://api.tenor.com/v1/search", params)

    # TODO: Use the '.json()' function to get the JSON of the returned response
    # object
    if r.status_code == 200:
        gifs = r.json()

    # TODO: Using dictionary notation, get the 'results' field of the JSON,
    # which contains the GIFs as a list
    results = gifs["results"]
    print (results)

    # TODO: Render the 'index.html' template, passing the list of gifs as a
    # named parameter called 'gifs'

    return render_template(
        "index.html",
        gifs=results)

#This is the begining of the creation of the gif route
# @app.route('/gif')
#     def get_gif():


if __name__ == '__main__':
    app.run(debug=True)