from flask import Flask, jsonify, request, render_template
import pandas as pd

app = Flask(__name__)

dati_clienti = pd.read_csv('data/dati_clienti.csv')

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/get_countries', methods=['GET'])
def get_countries():
    countries = sorted(list(set(dati_clienti['Country'])))
    return jsonify(countries)

@app.route('/get_cities/<country>', methods=['GET'])
def get_cities(country):
    cities_info = dati_clienti[dati_clienti['Country'] == country]
    city_counts = cities_info['City'].value_counts().sort_values(ascending=False).to_dict()
    return jsonify(city_counts)

@app.route('/get_customers', methods=['GET'])
def get_customers():
    city = request.args.get('city')
    customers_info = dati_clienti[dati_clienti['City'] == city]
    return jsonify(customers_info.to_dict(orient='records'))

@app.route('/add_customers', methods=['POST'])
def add_customers():
    if request.method == 'GET':
        return "The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST':
        customer_id= int(result.json['id'])
        CustomerName = folat(result.json['username'])
        Contact_Name = float(result.json['name'])
        Address = folat(result.json['address'])
        City = float(result.json['city'])
        PostalCode = folat(result.json['cap'])
        Country = folat(result.json['country'])
        return jsonify()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=32457, debug=True)