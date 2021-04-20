# from wallstreet import Put, Stock
import wallstreet
from wallstreet import *
import pandas as pd 

global return_per_year_target
return_per_year_target = 25

"""
Tickers are currently passed not as a list, but as a string of tickers separated by spaces and/or tabs.
This is because it's easier to copy and past a list of tickers found from a table on the internet.
https://www.barchart.com/options/iv-rank-percentile/stocks?viewName=main&orderBy=optionsImpliedVolatilityRank1y&orderDir=desc
"""

tickers = 'ESGC	HAE	GSX	IAC	RBLX	PLBY	OUST	LFMD	CLOV	MSTR	SNAP	TWLO	IIVI	FTCH	SPOT	RIDE	TWTR	FEYE	X	DOYU	AMKR	TROX	ETSY	Z	KTOS	PINS	INTC	EA	RTX	TAL	FNKO	INSG	PYPL	ARVL	TIGR	FSR	FSLR	DDOG	FB	VIAC	YETI	GIK	XXII	AGC	CVM	BTI	GOOG	SPWR	IQ	GOOGL	CSCO	DASH	NVTA	HUYA	UPS	AMAT	NVAX	ADI	STX	LOW	ENPH	CZR	LAC	SI	HBI	EBAY	GOEV	ATVI	BIDU	WDC	CLF	RVLV	ISRG	ROKU	SONO	WMT	BAX	TGT	DNMR	ASXC	ANGI	CLNE	ASML	BHC	AMD	RMO	UAA	BILI	BRK.B	W	TME	SQ	NUE	BYND	JMIA	SPLK	PSFE	FSLY	VIPS	KSU'
# tickers = tickers.split('   ')
# tickers = tickers.split('  ')
tickers = tickers.split('\t')
# tickers = tickers.split(' ')
 
#https://stackoverflow.com/questions/1801668/convert-a-python-list-with-strings-all-to-lowercase-or-uppercase
# Capitalize tickers
[ticker.upper() for ticker in tickers]
 
# Get rid of any duplicates
# tickers_no_duplicates = tickers
tickers_no_duplicates = []
for ticker in tickers:
  if ticker not in tickers_no_duplicates and (ticker != ''): # or ticker != ' ' or ticker != '  '
    tickers_no_duplicates.append(ticker) 
 
tickers = tickers_no_duplicates
 
print(tickers)
 
scores = []
strikes_list = []
expiration_list = []
tickers_list = []
# return_per_day_list = []
return_per_year_list = []
option_prices_list = []
underlying_price_list = []
option_volume_list = []
last_underlying = ""
last_average_pct_change = 0
 
def getdata(option):
  print(f"\t {option}")
 
  if option.volume <= 20:
    print('Option volume <= 20')
    return scores, strikes_list, expiration_list, tickers_list, return_per_year_list, option_prices_list, underlying_price_list, option_volume_list
  
 
  #print(f"Current put price: {option.price}")
 
  # if option.bid == 0:
  #   bid = 0.01
  # else: bid = option.bid
  # mid = (bid + option.ask) / 2
 
  # if option.price < mid:
  #   price = option.price
  # elif option.volume <= 20:
  #   price = option.bid
  # else: price = mid
 
  price = option.bid
  if price == 0:
    # price = 0.01
    print('Price is 0')
    return scores, strikes_list, expiration_list, tickers_list, return_per_year_list, option_prices_list, underlying_price_list, option_volume_list
  price = price * 100
 
  #print(f"Current put bid price: ${bid}")
 
  #print(f"Current implied_volatility: {option.implied_volatility()}")
 
  #print(f"Current delta: {option.delta():.5f}")
  # probability = (1 - option.delta())*100
  #print(f"Current probability: {probability:.2f}%")
  price_delta = option.underlying.price - option.strike
  #print(f"Current vega: {option.vega()}")
 
  #print(f"Current stock price: ${option.underlying.price}")
 
  from datetime import datetime
  from datetime import date
 
  # Returns the current local date 
  today = date.today() 
  #print("Today date is: ", today) 
 
  def days_between(d1, d2):
      d1 = datetime.strptime(d1, "%d-%m-%Y")
      d2 = datetime.strptime(d2, "%Y-%m-%d")
      return abs((d2 - d1).days)
 
  days_to_expiration = days_between(option.expiration, str(today))
  if days_to_expiration == 0:
    # days_to_expiration = 1
    print("0 Days to expiration")
    return scores, strikes_list, expiration_list, tickers_list, return_per_year_list, option_prices_list, underlying_price_list, option_volume_list
 
  collateral = option.strike * 100
  return_perc = ((collateral + price) - collateral) / collateral
  return_per_day = (return_perc / days_to_expiration) * 100

  return_per_year = (return_per_day * 365)
  global return_per_year_target
  if return_per_year < return_per_year_target:
    print(f'Return per year: {return_per_day*365} does not meet {return_per_year_target}% target')
 
    return scores, strikes_list, expiration_list, tickers_list, return_per_year_list, option_prices_list, underlying_price_list, option_volume_list
  
 
  #print(f"Return%: {return_perc} / price delta {price_delta}")
  try: last_underlying
  except: last_underlying = None
  try: last_average_pct_change
  except: last_average_pct_change = 0
  if option.underlying == last_underlying:
    average_pct_change = last_average_pct_change
  else:
    average_pct_change = option.underlying.historical(days_back=30, frequency='d')['Close'].pct_change().mean()
  last_underlying = option.underlying
  last_average_pct_change = average_pct_change
  # score = ((option.underlying.price / option.strike) / return_per_year) / days_to_expiration
  score = ((option.underlying.price / option.strike) / return_per_year)
  # score = ((option.underlying.price / option.strike) / return_per_year) / days_to_expiration / abs(average_pct_change)
  # score2 = option.underlying.change / ((price_delta * return_per_day) / days_to_expiration)
  # score = (score1 + score2) / 2
  scores.append(score)
 
  return_per_year_list.append(return_per_year)

  underlying_price_list.append(option.underlying.price)
 
  option_prices_list.append(price/100)
 
  tickers_list.append(option.ticker)
 
  strikes_list.append(option.strike)
 
  expiration_list.append(option.expiration)

  option_volume_list.append(option.volume)
  # print(f"expiration_list: {expiration_list}")
  # print(f"strikes_list: {strikes_list}")
  # print(f"Scores: {scores}")
  #print(f"score: {score}")
  #print()
 
  return scores, strikes_list, expiration_list, tickers_list, return_per_year_list, option_prices_list, underlying_price_list, option_volume_list
 
years = []
months = []
days = []
 
expirations_d = {"days":[],"months":[],"years":[]};
 
i = 0
 
for ticker in tickers:
  i += 1
  print(f'Ticker iteration: {i}')
  try: expirations = wallstreet.Put(ticker).expirations
  except IndexError as e:
    print(f'Expirations IndexError: {e}')
    continue
  except LookupError as e:
    print(f'Expirations LookupError: {e}')
    continue
  except Exception as e:
    print(f'Expirations Exception: {e}')
    continue
  
  # Select only first four expirations
  expirations = expirations[:4]

  # except Exction as e: 
  #   print(f"Error: {e}")
    # if "No options listed for given date" in str(e):
    #   tickers.remove(ticker)
 
  # except Exception as e: 
  #   print(f"Error: {e}")
  
  for expiration in expirations:
    split = expiration.split("-")
    day = int(split[0])
    month = int(split[1])
    year = int(split[2])
    try: strikes = wallstreet.Put(ticker, d=day, m=month, y=year).strikes
    # except LookupError as e: 
    except Exception as e:
      print(f'Strikes error: {e}')
      continue
    
    # # days.append(day)
    # expirations_d["days"].append(day)
    # # months.append(month)
    # expirations_d["months"].append(month)
    # # years.append(year)
    # expirations_d["years"].append(year)
 
    from IPython.display import clear_output 
    if i > 1:
      clear_output()  
 
    print(f'Current Ticker: {ticker}')
    print(f'Ticker iterations: {i}')
    print(f"Expirations: {expirations}")
    print(f"Strikes: {strikes}")
 
    try:
      # Create the pandas DataFrame 
      df = pd.DataFrame(
                        {'scores': scores,
                        'strikes': strikes_list,
                        'expirations': expiration_list,
                        'ticker': tickers_list,
                        'return_per_year': return_per_year_list,
                        'option prices': option_prices_list,
                        'underlying price': underlying_price_list,
                        'option volume': option_volume_list
                        })
    except Exception as e:
      print(e)
      # print(scores, strikes, expirations, ticker, return_per_year, option prices)
      # print(underlying price, option volume)

      # for each in yup:
      #   print(len(each))
      #   print(each)
        


 
    # dropping duplicate rows 
    df.drop_duplicates(keep=False, inplace=True) 
 
    # print dataframe. 
    sort_by_score = df.sort_values('scores', ascending=False)
    display(sort_by_score.head(n=60))
 
    for strike in strikes:
      
      print(f"{ticker} {day}/{month}/{year}, strike: {strike}")
      
      try: option = Put(ticker, d=day, m=month, y=year, strike=strike)
      except LookupError: 
        print("No options listed for this stock.")
        continue
      except Exception as e: print(e)
 
      try: scores, strikes_list, expiration_list, tickers_list, return_per_year_list, option_prices_list, underlying_price_list, option_volume_list = getdata(option)
      except LookupError: 
        print("No options listed for this stock.")
        continue
      except Exception as e: print(e)
