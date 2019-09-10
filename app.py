from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    """Return homepage."""
    # TODO: Extract query term from url
    #pull URL as a string with requests
    #extract term from string
    # TODO: Make 'params' dict with query term and API key
    #define the params dictionary as query term/API key
    #append extracted term from url to dictionary
    # TODO: Make an API call to Tenor using the 'requests' library
    #use requests library to call API
    #append api to dictionary with same term
    # TODO: Get the first 10 results from the search results
    #call dictionary
    #loop over 10 gif's
    #display 10 gif's according to template
    # TODO: Render the 'index.html' template, passing the gifs as a named parameter
    #call templates and gif data
    #render template
    #pass gifs data into template
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)