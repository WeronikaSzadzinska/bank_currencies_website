import requests, csv

response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
data = response.json()
data_dict = data[0]
data_dict = data_dict['rates']

with open('bank_currencies.csv', 'w',  encoding="utf-8") as csvfile:
    fieldnames = ["currency", "code", "bid", "ask"]
    writer = csv.DictWriter(csvfile, delimiter =";", fieldnames=fieldnames)
    writer.writeheader()
    for x,n in enumerate(data_dict):
        writer.writerow(n)

from flask import Flask, request, render_template, redirect, url_for
import csv

app = Flask(__name__)

@app.route("/currency_calc", methods = ["GET","POST"])
def currency():
    if request.method == "POST":
        data = request.form
        currency = data.get("currency")
        currency = str(currency)
        amount = data.get("quantity")
        with open("bank_currencies.csv",  encoding='ISO-8859-2') as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter = ';')
            #csv_reader = [row for row in csv_reader if row]
            for row in csv_reader:
                print(row['currency'])
                if row['currency'] == currency:
                    price = float(amount) * float(row['ask'])
                    price = round(price,2)
            return f"za {amount} x {currency} zaplacisz {price} pln "


    else:
        return render_template("currency_template.html")

