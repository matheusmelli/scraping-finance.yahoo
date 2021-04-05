from flask import Flask
from flask import request
from scraping import *
from flask import jsonify
from flask_caching import Cache 

app = Flask(__name__)
cache = Cache(config={'CACHE_TYPE': 'SimpleCache'})
cache.init_app(app)

@app.route('/stocks', methods=['GET'])
@cache.cached(timeout=193)
def stocks():
    region = request.args.get('region')
    symbol = scraping(region)
    
    return jsonify(symbol)

app.run(debug=True, host='0.0.0.0')
