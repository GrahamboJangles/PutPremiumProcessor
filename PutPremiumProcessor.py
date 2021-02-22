import wallstreet
from wallstreet import *
import pandas as pd 
 
# ticker = 'CVM'

"""
Tickers are currently passed not as a list, but as a string of tickers separated by spaces and/or tabs.
This is because it's easier to copy and past a list of tickers found from a table on the internet.
"""
# tickers = ['CVM', 'CCIV', 'CLOV', 'CAN', 'MVIS', 'WBAI', 'BTBT', 'FCEL', 'GME', 'VSPR', 'MARA', 'EBIX'] 
tickers = 'CVM CCIV CLOV CAN MVIS WBAI BTBT FCEL GME VSPR MARA EBIX'
tickers += ' '
tickers += 'CVM  YY  TME BLOK    MJ  APHA    XNET    PDD BILI    HUYA    MUX SSYS    MOMO    DBX TDC GILT    TLRY    ZTO BIDU    VKTX    NRG AGTC    XXII    QTT MRVL    TXMD'
tickers += ' '
tickers += 'SNDL    VZ  AMD QS  GSAT    MSFT    WMT BP  AAL TWTR    MARA    DNN F   FB  BABA    BAC UBER    VALE    CCIV    TLRY    GME GOLD    BA  BB  NVDA    C   AMC NCLH    FCX DIS FUTU    CBAT    XOM RIOT    CVS EBON    SQ  FUBO    NOK WBA PSTH    GE  XPEV    FSR X   DKNG    PLUG    INTC    ET  APHA    JD  FSLY    PFE BIDU    BLNK    FCEL    PTON    NXTD    WKHS    LODE    ZM  NNDM    CVX LI  RKT SPCE    NFLX    ACB LVS SBUX    PYPL    SENS    QCOM    GM  BNGO    MU  CRM MRK JPM IDEX    SHOP    AR  CSCO    SOS CLOV    TIGR    TGT MRVL    GSX UAL MGM MVIS'
# tickers = tickers.split('   ')
# tickers = tickers.split('  ')
tickers = tickers.split(' ')

# tickers = ['CVM']
 
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
return_per_day_list = []
return_per_year_list = []
option_prices_list = []
underlying_price_list = []
 
# for letter in alphabet:
def getdata(option):
  print(f"\t {option}")
 
  if option.volume == 0:
    print("No option volume")
    return scores, strikes_list, expiration_list
 
  price = option.bid
  if price == 0:
    # price = 0.01
    print('Price is 0')
    return scores, strikes_list, expiration_list
  price = price * 100
    
  price_delta = option.underlying.price - option.strike
 
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
    return scores, strikes_list, expiration_list
 
  collateral = option.strike * 100
  return_perc = ((collateral + price) - collateral) / collateral
  return_per_day = (return_perc / days_to_expiration) * 100
  # if return_per_day < 0.06849315068:
  return_per_year = (return_per_day * 365)
  if return_per_year < 41:
    print(f'Return per year: {return_per_day*365} not enough')
 
    return scores, strikes_list, expiration_list
  return_per_year_list.append(return_per_year)
 
  #print(f"Return%: {return_perc} / price delta {price_delta}")
 
  score = (option.underlying.price / option.strike) / return_per_year
  # score2 = option.underlying.change / ((price_delta * return_per_day) / days_to_expiration)
  # score = (score1 + score2) / 2
  scores.append(score)
 
  underlying_price_list.append(option.underlying.price)
 
  option_prices_list.append(price/100)
 
  tickers_list.append(option.ticker)
 
  strikes_list.append(option.strike)
 
  expiration_list.append(option.expiration)
  # print(f"expiration_list: {expiration_list}")
  # print(f"strikes_list: {strikes_list}")
  # print(f"Scores: {scores}")
  #print(f"score: {score}")
  #print()
 
  return scores, strikes_list, expiration_list
 
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
    except LookupError as e: 
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
 
    print(f'Iterations: {i}')
    print(f"Expirations: {expirations}")
    print(f"Strikes: {strikes}")
 
    # Create the pandas DataFrame 
    df = pd.DataFrame(
                      {'scores': scores,
                      'strikes': strikes_list,
                      'expirations': expiration_list,
                      'ticker': tickers_list,
                      'return_per_year': return_per_year_list,
                      'option prices': option_prices_list,
                      'underlying price': underlying_price_list
                      })
 
    # dropping duplicate rows 
    df.drop_duplicates(keep=False, inplace=True) 
 
    # print dataframe. 
    sort_by_score = df.sort_values('scores', ascending=False)
    display(sort_by_score.head(n=50))
 
    for strike in strikes:
      
      print(f"{ticker} {day}/{month}/{year}, strike: {strike}")
      
      try: option = Put(ticker, d=day, m=month, y=year, strike=strike)
      except LookupError: 
        print("No options listed for this stock.")
        continue
      except Exception as e: print(e)
 
      try: scores, strikes_list, expiration_list = getdata(option)
      except LookupError: 
        print("No options listed for this stock.")
        continue
      except Exception as e: print(e)
