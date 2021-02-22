# PutPremiumProcessor
PutPremiumProcessor is a Python option screener built off of the wallstreet module. I created this to find puts that pay good premium for the risk.

The table generated is sorted by a scoring each put for it's risk/return. It's just something I came up with.

The formula is `score = (option.underlying.price / option.strike) / return_per_year`

The score isn't perfect, but does a good job of putting some worthwhile puts to look over.

The list of ticker symbols was from a website that listed stocks by IV Rank, but is not updated. You can put whatever stock symbols you want to scan in. I might look into fetching these symbols automatically in the future.
