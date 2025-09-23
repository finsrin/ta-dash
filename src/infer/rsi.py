import numpy as np 
import pandas as df 

def get_rsi_result (rsi_df):
    result = "Oversold"
    most_recent_rsi = rsi_df.iloc[-1]['Close'].values[0]
    if (most_recent_rsi > 70):
        result = "Overbought"
    elif (most_recent_rsi < 30):
        result = "Oversold"
    else:
        result = "Neutral"

    return most_recent_rsi,result
