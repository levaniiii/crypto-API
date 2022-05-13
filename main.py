import requests
import sqlite3


conn = sqlite3.connect("coins.sqlite")
cursor = conn.cursor()




print("chose coin to get info: ")
print("[1] Bitcoin")
print("[2] Ethereum")
print("[3] Litecoin")

coin = input("Enter option: ")

c_coin = "btc"

if coin == '1':
    c_coin = "btc"
elif coin == '2':
    c_coin = "eth"
elif coin == '3':
    c_coin = "ltc"


url = f"https://api.cryptapi.io/{c_coin}/info"
r = requests.get(url)
data = r.json()



cursor.execute('''create table if not exists coin_info
                (id integer primary key autoincrement,
                coin varchar (100),
                logo varchar (1000),
                minimum_transaction integer,
                minimum_transaction_coin float);''')


coin_data = (data["coin"], data["logo"], data["minimum_transaction"], data["minimum_transaction_coin"])
query = "insert into coin_info (coin, logo, minimum_transaction, minimum_transaction_coin) values (?, ?, ?, ?)"
cursor.execute(query, coin_data)
conn.commit()

print("Coin info saved to database.")


conn.close()