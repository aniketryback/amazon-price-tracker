# %%

import pandas as pd
import matplotlib.pyplot as plt
import os
import 	requests
from bs4 import BeautifulSoup
from datetime import datetime

# %%
url = "https://www.amazon.in/ref=PS5BAU25QCPS5digital/dp/B0CY5QW186/?_encoding=UTF8&pd_rd_w=M2bYC&content-id=amzn1.sym.3b2d0011-a8ec-4315-a031-cca3c26cfcd6&pf_rd_p=3b2d0011-a8ec-4315-a031-cca3c26cfcd6&pf_rd_r=NRVNG717792V8GJ5F5S4&pd_rd_wg=rO1kJ&pd_rd_r=e0e34376-971e-4677-a367-84691a7713e0&ref_=pd_hp_d_atf_unk"
headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Accept-Language": "en-US,en;q=0.9"
    }
# %%
##Fetching the Data
def fetch_price():
    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.content, 'lxml')

    title = soup.find(id = "productTitle")
    price = soup.find("span", class_="a-price-whole")

    if not title or not price:
        raise Exception("Price or Title not found, Amazon may have blocked you")
    
    title_text = title.get_text(strip=True)
    price_text = price.get_text(strip=True).replace(",", "")

    return{
        "title" : title_text,
        "price" : float(price_text),
        "timestamp" : datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    print("✅ Data Successfully Fetched")

# %%
#Saving the output

def append_to_csv(record, filename = "price_tracker.csv"):

    df = pd.DataFrame([record])

    if not os.path.exists(filename):
        df.to_csv(filename, index = False)
    else:
        df.to_csv(filename, mode="a", header=False, index=False)
    print("✅ Data Saved to CSV Format")

# %%
#Plotting the Data

def plot_price(filename = "price_tracker.csv"):

    df = pd.read_csv(filename)
    df['timestamp'] = pd.to_datetime(df['timestamp'])

    last_10 = df.tail(10)

    plt.figure(figsize = (10,5))
    plt.plot(last_10['timestamp'],last_10['price'], color ='green', linestyle = '-', marker = 'o')
    plt.xlabel("Timestamp")
    plt.ylabel("Price")
    plt.title("Price over the time")
    plt.xticks(rotation = 45)


    os.makedirs("output", exist_ok= True)
    plt.savefig("output/price_trend.png")
    print("✅ Price trend chart saved to output/")

# %%
if __name__ == "__main__" :
    try:
        record = fetch_price()
        print(f"🛒 {record['title']}")
        print(f"₹ {record['price']}")
        append_to_csv(record)
        plot_price()
    except Exception as e:
        print(str(e))


