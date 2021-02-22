# PutPremiumProcessor
PutPremiumProcessor is a Python option screener built off of the wallstreet module. I created this to find puts that pay good premium for the risk.

The table shown is sorted by a scoring each put for it's risk/return. The formula is `score = (option.underlying.price / option.strike) / return_per_year`
The score isn't perfect, but does a good job of putting some worthwhile puts to look over.
