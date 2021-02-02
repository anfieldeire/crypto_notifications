# crypto_notifications
# Summary: Program that connects to Coingecko API to get crypto data and send notifications

* Input: Text file containing cryptocurrency porfolito data for users with the coin symbol and the amount held.
  * Format: A list of lists. Each user is in a list. The first part of each list is the user information, the second part is the users portfolio information.
* The program connects to the coingecko API and retrieves data for each coin specified in each users portfolio
* Metrics retrieved:
  * Percentage Price Change 24H
  * Percentage Price Change 7D
  * Percentage Price Change 14D
  * Percentage Price Change 30D
  * Price ATH
  * Portfolio Totals and Subtotals for each user
* Output: The program alerts the user via Twilio sms if any coin breached their alert percentage. It will show the subtotal in USD held of that coin.
  
  
