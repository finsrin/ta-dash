import argparse
from datetime import date
from src.analyse import get_dashboard_data
import warnings


warnings.filterwarnings("ignore")
ascii_logo = """
  _____ _     ___   _   ___ _  _ 
 |_   _/_\   |   \ /_\ / __| || |
   | |/ _ \  | |) / _ \\__ \ __ |
   |_/_/ \_\ |___/_/ \_\___/_||_|
                                 
"""

print (ascii_logo)

parser = argparse.ArgumentParser(description="A python based tool to generate technical analysis charts for a given ticker using data from yfinance.")
parser.add_argument("-t", "--ticker", required=True, type=str, help="The stock ticker you want to analyse")
parser.add_argument("-w", "--window", type=int, help="The moving window to analyze [in days] (default:20)")
parser.add_argument("-s", "--start_date", type=str, help="The date from which you want to analyse [in yyyy-mm-dd] (default: '2025-01-01')")
parser.add_argument("-e", "--end_date", type=str, help="The date from which you want to analyse [in yyyy-mm-dd] (default: today's date)")

args = parser.parse_args()

ticker = args.ticker

if args.window:
  window = args.window
else:
  window = 20

if args.start_date:
  start_date = args.start_date
else:
  start_date = '2025-01-01'

if args.end_date:
  end_date = args.end_date
else:
  current_date = date.today()
  end_date = current_date.strftime("%Y-%m-%d")

print("Analysing ",ticker," from ",start_date," to ",end_date," on a rolling window of ",window," days. \n")

current_val,result = get_dashboard_data (ticker, window, start_date, end_date)

print ("--- TA Vitals ---")
print ("Price: ",current_val["price"])
print ("Simple Moving Avg: ",current_val["sma"])
print ("Bollinger Bands: ",current_val["boll_up"]," and ",current_val["boll_down"])
print ("Relative Strength Index: ",current_val["rsi"])
print ("------")
print ("\n")
print ("---Results---")
print ("Relative Strength Index: ",result["rsi"])
print ("Bollinger Band: ", result["boll"])
print ("------")
