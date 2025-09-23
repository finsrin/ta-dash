def get_sma_df(price_df,window=20):
    return price_df.rolling(window).mean()

def get_sd_df(price_df,window=20):
    return price_df.rolling(window).std()

