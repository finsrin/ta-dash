from .infer.bollinger import get_bollinger_result
from .infer.rsi import get_rsi_result
from .model.current_data import get_current_data_obj
from .model.result import get_result_data_obj
from .tools.bollinger import get_bollinger_bands
from .tools.rsi import get_rsi_df
from .tools.sma import get_sma_df
from .utils.price import get_price_dataframe
from .utils.visualise import visualise_price,visualise_indicator,visualise_index,visualise_bollinger_bands

def get_dashboard_data (ticker,mva,start_date,end_date):
    # Get Price Dataframe and Current Price
    price_df = get_price_dataframe(ticker,start_date,end_date)
    most_recent_price = price_df.iloc[-1]['Close'].values[0]
    # Get Simple Moving Average Dataframe and Current Simple Moving Average 
    sma_df = get_sma_df(price_df,mva)
    most_recent_sma = sma_df.iloc[-1]['Close'].values[0]
    #Get RSI Dataframe and Current RSI along with whether the security is oversold or oversold
    rsi_df = get_rsi_df(price_df,mva)
    most_recent_rsi,rsi_result = get_rsi_result(rsi_df)
    #Get Historical Bollinger Bands Dataframe and Current Bollinger Bands along with whether the security is overbought or oversold
    bollinger_upper_df,bollinger_middle_df,bollinger_lower_df = get_bollinger_bands(price_df,mva)
    most_recent_boll_up,most_recent_boll_low,boll_result = get_bollinger_result(bollinger_upper_df,bollinger_lower_df,most_recent_price)
    #Visualise all these dataframes as a chart
    visualise_price(ticker,price_df)
    visualise_indicator(ticker,price_df,"Simple Moving Average",sma_df)
    visualise_index(ticker,price_df,"RSI",rsi_df)
    visualise_bollinger_bands(ticker,price_df,bollinger_upper_df,bollinger_middle_df,bollinger_lower_df)

    #Store all the dataframes as csv for further analysis
    price_df.to_csv("price.csv")
    sma_df.to_csv("sma.csv")
    rsi_df.to_csv("rsi.csv")

    #Converting all the data into approp result model to be used by our flask application
    current_data_obj = get_current_data_obj(most_recent_price,most_recent_sma,most_recent_rsi,most_recent_boll_up,most_recent_boll_low)
    result_obj = get_result_data_obj(rsi_result,boll_result)

    return current_data_obj,result_obj
