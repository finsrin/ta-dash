import yfinance as yf


def get_price_dataframe(ticker,start_date,end_date):
   
    price_df = yf.download(ticker,start_date,end_date)
    price_df = price_df[['Close']]
    return price_df

