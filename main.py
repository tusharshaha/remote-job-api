from flask import Flask, request, jsonify
from careerjet_api_client import CareerjetAPIClient

app = Flask(__name__)

# Define the Careerjet API client with the default locale 'en_GB'
cj = CareerjetAPIClient("en_GB")

# Define the base URL for search results
BASE_URL = 'http://www.example.com/jobsearch?q={keywords}&l={location}'

@app.route('/api/jobs', methods=['GET'])
def search():
    # Get keywords and location from the query parameters
    keywords = request.args.get('keywords', '')
    location = request.args.get('location', '')

    # Perform the Careerjet search
    result_json = cj.search({
        'location': location,
        'keywords': keywords,
        'affid': '213e213hd12344552',
        'user_ip': '11.22.33.44',
        'url': BASE_URL.format(keywords=keywords, location=location),
        'user_agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:31.0) Gecko/20100101 Firefox/31.0'
    })

    # Return the search results as JSON
    return jsonify(result_json)

if __name__ == '__main__':
    app.run(debug=True)
