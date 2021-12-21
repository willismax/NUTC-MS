from flask  import Flask, render_template, request, jsonify
import requests
import json


app = Flask(__name__)


def get_cinema_income():
    url = 'https://boxoffice.tfi.org.tw/api/export?start=2021/12/06&end=2021/12/12'
    res = requests.get(url)
    return res.json()

def save_josn_data():
    data = get_cinema_income()
    with open('./static/data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def load_json_data():
    try:
        with open('./static/data.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data
    except:
        print('load json data error')
    

data = load_json_data()


@app.route('/')
def index():
    return '<h1>電影票房API</h1>'

@app.route('/api/all')
def all():
    return jsonify(data)


@app.route('/api/<search_key>')
def country(search_key):
    data = load_json_data()
    data = [ i for i in data['list'] for k,v in i.items() if v == search_key ]
    return jsonify(data)

# @app.route('/api/<name>')
# def country(name):
#     data = load_json_data()
#     data = [ i for i in data['list'] for k,v in i.items() if v == country ]
#     return jsonify(data)


if __name__ == '__main__':
    app.debug = True
    app.run()
