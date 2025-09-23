from .sma import get_sma_df,get_sd_df

def get_bollinger_bands(price_df,window=20):
    sma_df = get_sma_df(price_df,window)
    sd_df = get_sd_df(price_df,window)
    upper_band = sma_df + (2 * sd_df)
    lower_band = sma_df - (2 * sd_df)
    return sma_df,upper_band,lower_band


