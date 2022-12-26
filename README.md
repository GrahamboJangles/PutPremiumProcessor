[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1kss_pt74teFy_Do2QmsrAdawAjlTj_74?usp=sharing)

# PutPremiumProcessor
PutPremiumProcessor is a Python option screener built off of the robin_stocks module. I created this to find puts that pay good premium for the risk.

The table generated is sorted by each put for it's risk/return.

You can put whatever stock symbols you want to scan in. 

### If you have problems running this:
I created this in Google Colab. Easiest way to make this work is to use the Colab link above.

The python file has more features and is the most up-to-date.

## TODO:


## DONE:
- Functionality to resume the scan if there is a keyboard interruption or error
- Fetch symbols automatically
- Speed things up (find a faster way to get option data for free?)
- Orders the put with the highest score automatically



outdated todo:
- Incorporate `option.underlying.change` into the custom score formula
