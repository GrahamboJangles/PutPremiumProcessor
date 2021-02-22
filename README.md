# PutPremiumProcessor
PutPremiumProcessor is a Python option screener built off of the wallstreet module. I created this to find puts that pay good premium for the risk.

The table generated is sorted by a scoring each put with a custom formula for it's risk/return.

The formula is `score = (option.underlying.price / option.strike) / return_per_year`

The score isn't perfect, but does a good job of sorting to find some worthwhile puts to look over.

The list of ticker symbols was from a website that listed stocks by IV Rank, but is not updated. You can put whatever stock symbols you want to scan in. 

## TODO:
- Fetch symbols automatically
- Functionality to resume the scan if there is a keyboard interruption or error
- Speed things up (find a faster way to get option data for free)
- Incorporate `option.underlying.change` into the custom score formula
