# crypto_notifications
Program that connects to Coingecko API to get crypto data and send notifications

* Input: Text file with a list of lists, each list for each user, each list containing dictionaries with user data and portfolio data
* The program connects to the coingecko API and retrieves data for each coing specified in each users portfolio
* Metrics retrieved:
  * Percentage Price Change 24H
  * Percentage Price Change 7D
  * Percentage Price Change 14D
  * Percentage Price Change 30D
  * Price ATH
  * Portfolio Totals and Subtotals for each user
