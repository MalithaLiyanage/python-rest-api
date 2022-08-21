from flask import Flask;
from flask import jsonify;
import requests;

from bs4 import BeautifulSoup

def get_currency(in_currency, out_currency):
  url = f'https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount=1'
  content = requests.get(url).text
  soup = BeautifulSoup(content, 'html.parser')
  rate = soup.find("span", class_="ccOutputRslt").get_text()
  rate = float(rate[:-4])
  
  return rate
app = Flask(__name__)


@app.route('/')
def home():
    return '<h1>Welcome to Currency Rate API</hi>'

@app.route('/api/v1/<input_curr>-<output__curr>')
def api(input_curr, output__curr):
    rate = get_currency(input_curr, output__curr)
    result_dictionary = {'input_currency': input_curr, 'output__currency': output__curr, 'rate': rate}
    return jsonify(result_dictionary)
app.run(host='127.0.0.1')