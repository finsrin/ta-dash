def get_bollinger_result(bollinger_upper,bollinger_lower,most_recent_price):
    result = "Neutral"
    most_recent_boll_up = bollinger_upper.iloc[-1]['Close'].values[0]
    most_recent_boll_low = bollinger_lower.iloc[-1]['Close'].values[0]
    if (most_recent_price > most_recent_boll_up):
        result = "Overbought"
    elif (most_recent_price < most_recent_boll_low):
        result = "Oversold"
    else:
        result = "Neutral"
    return most_recent_boll_up,most_recent_boll_low,result


