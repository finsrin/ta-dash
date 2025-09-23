import matplotlib.pyplot as plt

def visualise_price (ticker,price_data_frame):
    plt.figure(figsize=(10, 6))
    plt.plot(price_data_frame, label='Closing Price', color='blue')
    title = "Stock Ticker: " + ticker
    plt.title(title)
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.grid()
    plt.savefig('Price.png')

def visualise_indicator (ticker,price_data_frame,indicator_name,indicator_dataframe):
    plt.figure(figsize=(10, 6))
    plt.plot(price_data_frame, label='Closing Price', color='blue')
    plt.plot(indicator_dataframe, label=indicator_name, color='red')
    title = indicator_name + " chart for " + ticker
    plt.title(title)
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.grid()
    file_name=indicator_name+".png"
    plt.savefig(file_name)

def visualise_index (ticker,price_data_frame,indicator_name,indicator_dataframe):
    plt.figure(figsize=(10, 6))
    plt.plot(indicator_dataframe, label=indicator_name, color='blue')
    plt.axhline(y=70, color='red', linestyle='-')
    plt.axhline(y=30, color='green', linestyle='-')
    title = indicator_name + " chart for " + ticker
    plt.title(title)
    plt.xlabel("Date")
    plt.ylabel("Percentage")
    plt.legend()
    plt.grid()
    file_name=indicator_name+".png"
    plt.savefig(file_name)

def visualise_bollinger_bands (ticker,price_data_frame,boll_top,boll_mid,boll_bottom):
    plt.figure(figsize=(10, 6))
    plt.plot(price_data_frame, label='Closing Price', color='blue')
    plt.plot(boll_top, label="Upper Bollinger Band", color='red')
    plt.plot(boll_mid, label="Middle Bollinger Band", color='black')
    plt.plot(boll_bottom, label="Lower Bollinger Band", color='green')
    title =  "Bollinger chart for " + ticker
    plt.title(title)
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.grid()
    file_name="Bollinger.png"
    plt.savefig(file_name)
