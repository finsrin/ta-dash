import numpy as np 
import pandas as df 

def get_rsi_df (price_df,window=20):
    difference = price_df.diff()
    gain = (difference.where(difference>0,0)).rolling(window).mean()
    loss = (difference.where(difference<0,0)).rolling(window).mean().abs()
    normalised_loss = loss.replace(0,np.nan)
    strength = gain/normalised_loss
    rsi = 100 - (100/(1+strength))
    return rsi