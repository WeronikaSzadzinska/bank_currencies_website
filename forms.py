
import requests, csv

def get_data():
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


def give_price(currency,amount):
    with open("bank_currencies.csv",  encoding='ISO-8859-2') as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter = ';')
            #csv_reader = [row for row in csv_reader if row]
            for row in csv_reader:
                #print(row['currency'])
                if row['currency'] == currency:
                    price = float(amount) * float(row['ask'])
                    price = round(price,2)
                    return price

f=give_price('euro',10)
print(f)