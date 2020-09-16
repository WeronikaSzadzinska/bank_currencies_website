from flask import Flask, request, render_template, redirect, url_for
import requests, csv
import forms 
    

app = Flask(__name__)

@app.route("/currency_calc", methods = ["GET","POST"])
def currency():
    if request.method == "POST":
        forms.get_data()
        data = request.form
        currency = data.get("currency")
        currency = str(currency)
        amount = data.get("quantity")
        price = forms.give_price(currency,amount)
        return render_template("currency.html", currency=currency, amount=amount, price=price)


    else:
        return render_template("currency_template.html")

