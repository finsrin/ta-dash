def get_current_data_obj(most_recent_price,most_recent_sma,most_recent_rsi,most_recent_boll_up,most_recent_boll_low):
    result_obj = {
        "price":float(most_recent_price),
        "sma":float(most_recent_sma),
        "rsi":float(most_recent_rsi),
        "boll_up":float(most_recent_boll_up),
        "boll_down":float(most_recent_boll_low)
    }
    return result_obj