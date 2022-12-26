#@title Log in
 
import pyotp
# This is the secret code located in the Google Authenticator app, or from the Aegis Authenticator app if you're cool.
# This isn't the code that changes every 30 seconds, it's the secret code that never changes.
totp    = pyotp.TOTP("YOUR-MFA-CODE-HERE").now()

print("Current OTP:", totp)

import robin_stocks.robinhood as r
email = "YOUR-EMAIL-HERE"#@param {type:"string"}
# Left password blank, it will ask for password when cell is run
login = r.login(email, p, mfa_code=totp)

"""
Puts or calls?
Leave blank for both
"""
#@title Leave blank for both
OPTION_SCAN_TYPE = "put" #@param ["put", "call", ""]

SPREAD_OR_SINGLE = "single" #@param ["single", "spread", ""]

"""Entering symbols"""
tickers = ''
tickers += 'SPY QQQ GLD SLV'

import re

string = """Symbol
Name
Last
Change
%Chg
Options Vol
Imp Vol
IV Rank
IV %
IV 1Yr High
Time
Details
Links
BOIL
Ultra Bloomberg Natural Gas ETF
21.54
-0.50
-2.27%
59,676
174.12%
54.70%
62%
239.73%
12/23/22
Details
ARKK
Ark Innovation ETF
30.97
-0.63
-1.99%
93,402
52.67%
53.11%
6%
91.27%
12/23/22
Details
KWEB
KS Trust KS CSI China Internet ETF
29.92
-0.76
-2.48%
76,941
48.63%
45.09%
10%
99.19%
12/23/22
Details
TLT
20+ Year Treas Bond Ishares ETF
102.16
-1.52
-1.47%
187,728
21.09%
42.27%
56%
29.76%
12/23/22
Details
SPY
S&P 500 SPDR
382.91
+2.19
+0.58%
6,742,766
20.08%
41.60%
28%
31.04%
12/23/22
Details
GDX
Vaneck Gold Miners ETF
28.87
+0.11
+0.38%
67,413
36.21%
41.54%
23%
49.70%
12/23/22
Details
SOXL
Semiconductor Bull 3X Direxion
9.77
-0.01
-0.10%
122,120
101.76%
38.30%
22%
146.42%
12/23/22
Details
TQQQ
Ultrapro QQQ ETF
17.59
+0.05
+0.29%
367,200
76.35%
38.09%
23%
116.62%
12/23/22
Details
QQQ
Nasdaq QQQ Invesco ETF
267.36
+0.60
+0.22%
2,030,052
25.66%
36.68%
21%
40.00%
12/23/22
Details
HYG
High Yield Corp Bond Ishares Iboxx $ ETF
74.39
+0.19
+0.26%
138,257
11.17%
34.24%
25%
24.32%
12/23/22
Details
SQQQ
Ultrapro Short QQQ ETF
53.50
-0.25
-0.47%
167,759
77.43%
30.93%
16%
129.30%
12/23/22
Details
SLV
Silver Trust Ishares
21.85
+0.16
+0.74%
93,286
28.61%
28.56%
44%
44.40%
12/23/22
Details
FXI
China Large-Cap Ishares ETF
27.80
-0.16
-0.57%
173,293
33.43%
27.28%
42%
56.13%
12/23/22
Details
DIA
Dow Industrials SPDR
331.93
+1.67
+0.51%
66,766
16.91%
24.28%
21%
28.24%
12/23/22
Details
IWM
Russell 2000 Ishares ETF
174.39
+0.79
+0.46%
460,555
23.38%
21.97%
12%
37.39%
12/23/22
Details
EWZ
Brazil Ishares MSCI ETF
28.79
+0.58
+2.06%
203,744
34.58%
20.56%
28%
61.22%
12/23/22
Details
XLE
S&P 500 Energy Sector SPDR
87.06
+2.69
+3.19%
146,407
30.61%
20.06%
8%
53.11%
12/23/22
Details
XLF
S&P 500 Financials Sector SPDR
33.95
+0.19
+0.56%
57,538
21.79%
13.66%
19%
43.42%
12/23/22
Details
UVXY
Trust Ultra VIX Short Term Futures ETF
7.06
-0.29
-3.95%
230,387
85.79%
6.18%
8%
229.77%
12/23/22
Details
GLD
Gold SPDR
167.26
+0.50
+0.30%
64,412
13.50%
5.18%
12%
30.57%
12/23/22
Details
"""

# Split the string into lines
lines = string.split("\n")

# Find the index of the 'Symbol' line
symbol_index = lines.index("Symbol")

# Extract the ticker symbols by taking every 13th line starting from the 'Symbol' line
ticker_symbols = [lines[i] for i in range(symbol_index + 13, len(lines), 12)]

tickers = [item for item in ticker_symbols if re.match('[a-zA-Z]+', item)]

# print(tickers)

# This was for extracting a list of tickers from a string
# tickers = re.split('[^a-zA-Z]', tickers)

# print(f'Raw data: {tickers}')
# print(len(tickers))

# tickers_filtered = []
# for ticker in tickers:
#     if ticker != '':
#         tickers_filtered.append(ticker)
tickers_filtered = [ticker for ticker in tickers if ticker != '']

tickers = tickers_filtered

# print(f'Filtered tickers: {tickers}')
# print(len(tickers))
 
#https://stackoverflow.com/questions/1801668/convert-a-python-list-with-strings-all-to-lowercase-or-uppercase
# Capitalize tickers
[ticker.upper() for ticker in tickers]
 
# Get rid of any duplicates
tickers_no_duplicates = []
for ticker in tickers:
    if ticker not in tickers_no_duplicates and (ticker != ''): # or ticker != ' ' or ticker != '    '
        tickers_no_duplicates.append(ticker) 
 
tickers = tickers_no_duplicates

# Enter Stocks to filter out of scan         
ticker_filter = []

tickers = [ticker for ticker in tickers if ticker not in ticker_filter]
 
print(f'Filtered out duplicates: {tickers}')
print(f"Scanning {len(tickers)} tickers")
 
# tickers = tickers[0]
symbol = tickers[0]
# print(symbol)
# print(len(tickers))
# tickers = tickers[:int(len(tickers)*.50)]
# print(len(tickers))

def order(df):
    # Select the first row
    best_put = df.iloc[0]

    # Retrieve the values you need to place the order
    ticker = best_put['ticker']
    expiration_date = best_put['expirations']
    strike_price = float(best_put['strikes'])
    credit = float(best_put['minimum credit'])

    # Place the order using the `orders.order_sell_put_option` function from the `robin_stocks` API
    # order_response = r.robinhood.orders.order_sell_put_option(ticker, expiration_date, strike_price, 1)
    print(credit, ticker, expiration_date, strike_price)
    print(type(credit), type(ticker), type(expiration_date), type(strike_price))
    order_response = r.orders.order_sell_option_limit(positionEffect="open", creditOrDebit="credit", price=credit,
                                                                symbol=ticker, quantity=1, expirationDate=expiration_date, 
                                                                strike=strike_price, optionType=OPTION_SCAN_TYPE, timeInForce='gtc', 
                                                                jsonify=True)

    # Print the response to check the status of the order
    print(order_response)

"""Getting option data"""
from tqdm import tqdm

import os
import time
import json

import re
import pandas as pd

# Define the regex pattern to match the csv files of a previous scan
pattern = r"^\[(?:'[A-Z]+',\s)+'[A-Z]+'\]\s\d{4}-\d{2}-\d{2}-\d{2}-\d{2}-\d{2}\s[AP]M\.csv$"

# Iterate through the files in the current directory
for filename in os.listdir():
    # Check if the file name matches the pattern
    if re.match(pattern, filename):
        answer = input(f"Found {filename}, do you want to load old scan? (y/n): ")
        if answer.lower() == 'y':
            # If the file exists, check its age. Return the age in seconds
            file_age = time.time() - os.path.getmtime(filename)
            # If the file is less than 48 hours old, load the CSV file using pandas
            if (file_age)/1000 < 3600*48:
                # Load the CSV file using pandas
                df = pd.read_csv(filename)
                order(df)
                exit()
    
# Check if the raw_option_list.txt file exists
if not os.path.exists(f'{tickers} raw_option_list.txt'):
    # If the file does not exist, run the raw_option_list assignment statement
    raw_option_list = list(map(lambda ticker : r.options.find_tradable_options(ticker, expirationDate=None, strikePrice=None, optionType=OPTION_SCAN_TYPE, info=None), tickers))
    
    # Save raw_option_list as a text file
    print("Saving raw_option_list.txt")
    with open(f'{tickers} raw_option_list.txt', 'w') as f:
        json.dump(raw_option_list, f)
else:
    # If the file exists, check its age. Return the age in seconds
    file_age = time.time() - os.path.getmtime(f'{tickers} raw_option_list.txt')
    # If the file is more than 48 hours old, run the raw_option_list assignment statement
    if (file_age)/1000 > 3600*48:
        raw_option_list = list(map(lambda ticker : r.options.find_tradable_options(ticker, expirationDate=None, strikePrice=None, optionType=OPTION_SCAN_TYPE, info=None), tickers))

        # Save raw_option_list as a text file
        print("Saving raw_option_list.txt")
        with open(f'{tickers} raw_option_list.txt', 'w') as f:
            json.dump(raw_option_list, f)
    else:
        # Load the contents of raw_option_list.txt into the raw_option_list variable
        with open(f'{tickers} raw_option_list.txt', 'r') as f:
            raw_option_list = json.load(f)


# Check if the raw_option_list.txt file exists
if not os.path.exists(f'{tickers} raw_option_list.txt'):
    # If the file does not exist, run the raw_option_list assignment statement
    raw_option_list = list(map(lambda ticker : r.options.find_tradable_options(ticker, expirationDate=None, strikePrice=None, optionType=OPTION_SCAN_TYPE, info=None), tickers))
    
    # Save raw_option_list as a text file
    print("Saving raw_option_list.txt")
    with open(f'{tickers} raw_option_list.txt', 'w') as f:
        json.dump(raw_option_list, f)
else:
    # If the file exists, check its age. Return the age in seconds
    file_age = time.time() - os.path.getmtime(f'{tickers} raw_option_list.txt')
    # If the file is more than 48 hours old, run the raw_option_list assignment statement
    if (file_age)/1000 > 3600*48:
        raw_option_list = list(map(lambda ticker : r.options.find_tradable_options(ticker, expirationDate=None, strikePrice=None, optionType=OPTION_SCAN_TYPE, info=None), tickers))

        # Save raw_option_list as a text file
        print("Saving raw_option_list.txt")
        with open(f'{tickers} raw_option_list.txt', 'w') as f:
            json.dump(raw_option_list, f)
    else:
        # Load the contents of raw_option_list.txt into the raw_option_list variable
        with open(f'{tickers} raw_option_list.txt', 'r') as f:
            raw_option_list = json.load(f)

"""Filtering out missing options"""
# print(len(raw_option_list))
# What happens when there are multiple [None]s?
try:
    print(tickers[raw_option_list.index([None])])
except: pass

try:
    tickers = [ticker for ticker in tickers if ticker != tickers[raw_option_list.index([None])]]
except: pass
no_missing_options2 = [chain for chain in raw_option_list if chain != [None]]
# print(len(no_missing_options2))

# combined_option_list = []
# for symbol_option_chains in no_missing_options2:
#     combined_option_list += symbol_option_chains
combined_option_list = [option for symbol_option_chains in no_missing_options2 for option in symbol_option_chains]

option_list = combined_option_list

underlying_prices = list(map(lambda ticker : float(r.stocks.get_latest_price(ticker, priceType=None, includeExtendedHours=True)[0]), tickers))

option_list = sorted(option_list, key = lambda option: (option['chain_symbol'], option['expiration_date'], option['strike_price']), reverse=OPTION_SCAN_TYPE=='put')

"""Filtering out options based on days to expiration"""
DAYS_OUT =    90#@param {type:"integer"}

def days_between(d1, d2):
    # d1 = datetime.strptime(d1, "%d-%m-%Y")
    d1 = datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.strptime(d2, "%Y-%m-%d")
    return abs((d2 - d1).days)

from datetime import datetime
from datetime import date

# Returns the current local date 
today = date.today()    

option_list_filtered = []

for option in option_list:
    try:
        expiration = option['expiration_date']
    except Exception as e: 
        print(e)
    days_to_expiration = days_between(str(expiration), str(today))
    
    if (days_to_expiration < DAYS_OUT):
        option_list_filtered.append(option)

option_list = option_list_filtered



"""Initializing lists"""
scores = []
strikes_list = []
expiration_list = []
 
tickers_list = []
return_per_year_list = []
option_prices_list = []
underlying_price_list = []
option_volume_list = []
 
ids = []

collateral_list = []
out_the_money_list = []
minimum_credit_list = []
distance_from_year_low_list = []
 
i = 0
j = 0


"""Save scan"""
save = False #@param {type:"boolean"}
if save:
    tickers_saved = tickers

    scores_saved = scores
    strikes_list_saved = strikes_list
    expiration_list_saved = expiration_list
 
    tickers_list_saved = tickers_list
    return_per_year_list_saved = return_per_year_list
    option_prices_lis_saved = option_prices_list
    underlying_price_list_saved = underlying_price_list
    option_volume_list_saved = option_volume_list
 
    ids_saved = ids
 
    i_saved = i
    j_saved = j
 
    df_saved = df
    option_list_saved = option_list
    raw_option_list_saved = raw_option_list
    underlying_prices_saved = underlying_prices
 
    print(len(df_saved))
    print(len(option_list_saved))
    print(f'{(((i*len(option_list)) + j) / len(option_list)**2) * 100:.2f}%')
    print('Scan saved.')

"""
Load scan
TODO: Make multiple save slots (maybe put each variable in a list?)
"""
load = False #@param {type:"boolean"}
if load:
    tickers = tickers_saved

    scores = scores_saved
    strikes_list = strikes_list_saved
    expiration_list = expiration_list_saved

    tickers_list = tickers_list_saved
    return_per_year_list = return_per_year_list_saved
    option_prices_list = option_prices_lis_saved
    underlying_price_list = underlying_price_list_saved
    option_volume_list = option_volume_list_saved

    ids = ids_saved

    i = i_saved
    j = j_saved

    df = df_saved
    option_list = option_list_saved
    raw_option_list = raw_option_list_saved
    underlying_prices = underlying_prices_saved

    print(len(df))
    print(len(option_list))
    print(f'{(((i*len(option_list)) + j) / len(option_list)**2) * 100:.2f}%')
    print('Scan loaded.')


"""And finally, scanning for options"""
#@title Scan
# %%capture
debug = False #@param {type:"boolean"}
# 2, 3
MIN_VOLUME = 3 #@param {type:"integer"}
# 0.65
OTM = 0.65 #@param {type:"number"}
# 25
MIN_RETURN =    10#@param {type:"integer"}
 
# Higher is safer
DISTANCE_FROM_YEAR_LOW =    30#@param {type:"integer"}
# this also works for calls, but is inversed from year high (100 - DISTANCE_FROM_YEAR_LOW)
 
def play_sound(sound):
    # print("placeholder function for sound")
    #send_email(error="Order filled")
    # https://stackoverflow.com/a/54295274/8142044
    # Play an audio beep. Any audio URL will do.
    from google.colab import output
    if sound=="filled":
        output.eval_js('new Audio("https://proxy.notificationsounds.com/notification-sounds/eventually-590/download/file-sounds-1137-eventually.ogg").play()')
    #if sound=="error":
        #output.eval_js('new Audio("https://proxy.notificationsounds.com/notification-sounds/point-blank-589/download/file-sounds-1136-point-blank.ogg").play()')

import traceback
import math
try:
    
    # 1 min interval so the output doesn't get filled up and crash the browser
    for option in tqdm(option_list[i:], mininterval=20, unit=' options', disable=debug):
 
        if i+j >= len(option_list):
            i = i + 1
            j = 1
        if debug:
            print(f'i: {i}')
            
        symbol = option['chain_symbol']

        expiration1 = option['expiration_date']
        
        id1 = option['id']
        
        try:
            # volume1 = int(r.options.get_option_market_data_by_id(id1, info='volume')[0])
            # Returns 'adjusted_mark_price', 'adjusted_mark_price_round_down', 'ask_price', 'ask_size', 'bid_price', 'bid_size', 'break_even_price', 'chance_of_profit_long', 'chance_of_profit_short', 'delta', 'gamma', 'high_fill_rate_buy_price', 'high_fill_rate_sell_price', 'high_price', 'implied_volatility', 'instrument', 'instrument_id', 'last_trade_price', 'last_trade_size', 'low_fill_rate_buy_price', 'low_fill_rate_sell_price', 'low_price', 'mark_price', 'occ_symbol', 'open_interest', 'previous_close_date', 'previous_close_price', 'rho', 'state', 'symbol', 'theta', 'updated_at', 'vega', 'volume'
            option_market_data = r.options.get_option_market_data_by_id(id1)[0]
            volume1 = int(option_market_data['volume'])
        except IndexError as e:
            # Sometimes options have no market data
            if debug:
                print(f'Volume IndexError: {e}')
            j = j + 1    
            continue
        except TypeError as e:
            # Soometimes server doesn't respond
            if debug:
                print(f'Volume get TypeError: {e}')
            continue

        if volume1 < MIN_VOLUME:
            if debug:
                print(f'Volume1: {volume1} too low')
            j = len(option_list)
            continue
        
        strike_price1 = float(option['strike_price'])
        
        if debug:
            print(f'Strikes: {strike_price1}')

        if OPTION_SCAN_TYPE == '':
            option_type1 = option_list[i]['type']
        else:
            option_type1 = OPTION_SCAN_TYPE

        if debug:
            print(f'i: {i}')

        try:
            underlying_price = underlying_prices[tickers.index(symbol)]
        except ValueError as e:
            print(f'Getting uderlying price error: {e}')

        # underlying_price = float(r.stocks.get_latest_price(symbol, priceType=None, includeExtendedHours=True)[0])
        if debug:
            print(f'Underlying price: {underlying_price}')

        if strike_price1 > underlying_price:
            if debug:
                print(f'First strike above underlying price')
            j = len(option_list)
            continue

        if (OPTION_SCAN_TYPE == 'put') or (option_type1 == 'put'):
            if strike_price1 > (underlying_price*OTM):
                if debug:
                    print(f'First strike not far enough OTM')
                j = len(option_list)
                continue
        else:
            if strike_price1 < (underlying_price/OTM):
                if debug:
                    print(f'First strike not far enough OTM')
                j = len(option_list)
                continue

        

        url = f'https://api.robinhood.com/fundamentals/{symbol}/'
        # Contains data about float, market_cap, shares_outstanding, high_52_weeks, low_52_weeks, dividend_yield, volume, average_volume, average_volume_2_weeks, average_volume_30_days
        try:
            stock_data = (r.helper.request_get(url, dataType='regular', payload=None, jsonify_data=True))
            year_low = float(stock_data['low_52_weeks'])
            year_high = float(stock_data['high_52_weeks'])
        except TypeError as e:
            print(f'Year low get TypeError: {e}')
        if debug:
            print(f'Year low: {year_low}')

        if (OPTION_SCAN_TYPE == 'put') or (option_type1 == 'put'):
            # Want our strike to be closer to year low
            if ((year_low / strike_price1) * 100) < DISTANCE_FROM_YEAR_LOW:
                j = len(option_list)
                continue
        elif (OPTION_SCAN_TYPE == 'call') or (option_type1 == 'call'):
            if debug:
                print(f'Year high: {year_high}')

            # Want our strike to be closer to year high
            if ((strike_price1 / year_high) * 100) > (100-DISTANCE_FROM_YEAR_LOW):
                j = len(option_list)
                continue

        collateral = (strike_price1) * 100

        try:
            # price1 = float(r.options.get_option_market_data_by_id(id1, info='high_fill_rate_sell_price')[0])
            price1 = float(option_market_data['high_fill_rate_sell_price'])
            if debug:
                print(f'Option price: {price1}')
        except:
            j = j + 1    
            continue
        if price1 == 0:
            # price1 = float(r.options.get_option_market_data_by_id(id1, info='bid_price')[0])
            price1 = float(option_market_data['bid_price'])
            if price1 == 0:
                # price1 = float(r.options.get_option_market_data_by_id(id1, info='adjusted_mark_price')[0])
                price1 = float(option_market_data['adjusted_mark_price'])

        price1 = price1 * 100

        credit = price1

        if credit <= 0:
            if debug:
                print(f'Credit {credit} <= 0')
            j = j + 1    
            continue

        if debug:
            print(f'Credit: {credit}, {id1}')

        try:
            return_perc = ((collateral + credit) - collateral) / collateral
        except ZeroDivisionError as e:
            if debug:
                print(f'Return % calculation ZeroDivisionError: {e}')
            j = j + 1    
            continue

        days_to_expiration = days_between(str(expiration1), str(today))
        if days_to_expiration == 0:
            days_to_expiration = 1

        if debug:
            print(f'DTE: {days_to_expiration}')
        
        return_per_day = (return_perc / days_to_expiration) * 100
        return_per_year = (return_per_day * 365)

        out_the_money = round(((strike_price1 - underlying_price) / underlying_price) * 100, 2)

        # Refactored return_per_year formula; used https://www.wolframalpha.com/widgets/view.jsp?id=4be4308d0f9d17d1da68eea39de9b2ce
        
        minimum_credit = math.ceil(((days_to_expiration * MIN_RETURN * collateral) / 36500)) / 100

        if return_per_year < MIN_RETURN:
            if debug:
                print(f'Return: {return_per_year} under minimum return limit {MIN_RETURN}')
            j = j + 1 
            continue
        
        # score = ((underlying_price / strike_price1) * return_per_year)
        # score = (((underlying_price / strike_price1) * (strike_price1 / return_per_year)) / return_per_year)
        # score = ((underlying_price / strike_price1) * (strike_price1 / return_per_year))
        # score = min(((underlying_price / strike_price1) * return_per_year), (underlying_price / strike_price1))
        # score = (underlying_price / strike_price1) + (return_per_year / underlying_price)
        score = underlying_price / strike_price1
        # This new score accounts for volatility
        score = (underlying_price / strike_price1) / ((year_high - year_low) / year_low)

        if debug:
            print(f'Score: {score}')
        import pandas as pd
        if return_per_year >= MIN_RETURN:
            scores.append(score)
            strikes_list.append(strike_price1)
            expiration_list.append(expiration1)
            tickers_list.append(symbol)
            return_per_year_list.append(round(return_per_year, 2))
            option_prices_list.append(credit/100) 
            underlying_price_list.append(underlying_price)
            option_volume_list.append(volume1)
            ids.append(id1)
            collateral_list.append(collateral)
            out_the_money_list.append(out_the_money)
            minimum_credit_list.append(minimum_credit)
            # distance_from_year_low_list.append((strike_price1 / year_low) * 100)
            distance_from_year_low_list.append((year_high - year_low) / year_low)
   
            new_option = pd.DataFrame(
                                        {'scores': score,
                                        'strikes': strike_price1,
                                        'expirations': expiration1,
                                        'ticker': symbol,
                                        'return_per_year': return_per_year,
                                        'credit': credit/100,
                                        'underlying price': underlying_price,
                                        'option volume': volume1,
                                        'collateral': collateral,
                                        'minimum credit': minimum_credit,
                                        'out the money': out_the_money,
                                        # Anything around 6.0 is pretty volatile
                                        'YTD volatility': ((year_high - year_low) / year_low),
                                        'id': id1
                                    }, index=[0])
                                    # somtimes we get a ValueError: If using all scalar values, you must pass an index.
                                    # index=[0] fixes this
            try:
                display(new_option)
            except:
                print(new_option)
            # pd.set_option("display.max_rows", None, "display.max_columns", None)
            # print(new_option)
            #display(score, [strike_price1, strike_price2], expiration1, symbol, return_per_year, credit/100, underlying_price, [volume1, volume2])
            
            #play_sound('filled')

except Exception as e:
    print(e)
    print(i)
    print(id1)
    print(traceback.format_exc())
except KeyboardInterrupt:
    pass
 
import pandas as pd
 
try:
    # Create the pandas DataFrame 
    df = pd.DataFrame(
                                        {'scores': scores,
                                        'strikes': strikes_list,
                                        'expirations': expiration_list,
                                        'ticker': tickers_list,
                                        'return_per_year': return_per_year_list,
                                        'credit': option_prices_list,
                                        'underlying price': underlying_price_list,
                                        'option volume': option_volume_list,
                                        'collateral': collateral_list,
                                        'OTM': out_the_money_list,
                                        'minimum credit': minimum_credit_list,
                                        'YTD volatility': distance_from_year_low_list,
                                        #'id': ids
                                        })
# try:
#     # Create the pandas DataFrame 
#     df = pd.DataFrame(
#                                         {'scores': scores,
#                                            "id's": ids
                                
#                                         })
except Exception as e:
    print(e)
 
# dropping duplicate rows 
# df.drop_duplicates(keep=False, inplace=True) 



# Check if the DataFrame is empty
if df.empty:
    print("The DataFrame is empty")
    print('################### DONE ###################')
else:
    # print dataframe. 
    sort_by_score = df.sort_values(['scores', 'return_per_year'], ascending=[OPTION_SCAN_TYPE == 'call', False])
    try:
        display(sort_by_score.head(n=60))
    except Exception as e:
        print(sort_by_score)
    # pd.set_option("display.max_rows", None, "display.max_columns", None)
    # print(sort_by_score)

    # Get the current date and time
    now = datetime.now()

    # Format the date and time as a string to be used in the file name
    timestamp = now.strftime("%Y-%m-%d-%I-%M-%S %p")
    sort_by_score.to_csv(f'{tickers} {timestamp}.csv', index=False)
    
    order(sort_by_score)
    
    print('################### DONE ###################')

