import requests
from flask import Flask
import json
import warnings

warnings.filterwarnings("ignore", category=UserWarning)
app = Flask(__name__)

@app.route("/")
def hello_world():
    text = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').text
    currencies = json.loads(text)
    html_output = "<h1>Текущие курсы валют:</h1>"

    for code, info in currencies['Valute'].items():
        name = info['Name']
        value = info['Value']
        html_output += f'{code}: {name} ({value} руб.)<br>'
    return html_output

if __name__ == '__main__':
    app.run(debug=True)

