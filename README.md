## Title: Cryptocurreny API Notification Program
## Summary: Program that connects to Coingecko API to get crypto data and send notifications based on alert thresholds

* Input: Text file containing cryptocurrency porfolito data for users with the coin symbol and the amount held.
  * Format: A list of lists. Each user is in a list. The first part of each list is the user information, the second part is the users portfolio information. (see the sample file portfolio.txt for more information)
* The program connects to the coingecko API and retrieves data for each coin specified in each users portfolio
* Metrics retrieved:
  * Percentage Price Change 24H
  * Percentage Price Change 7D
  * Percentage Price Change 14D
  * Percentage Price Change 30D
  * Price ATH
  * Portfolio Totals and Subtotals for each user
* Run instructions: 
     *  Install your virtual environment
     *  Install the requirements.txt file by running pip freeze > requirements.txt
     *  Copy the portfolio.txt file into your environment root directory. Change data as necessary.
     *  Create a twilio account with a phone number. Use that number as the from number in the twilio_message.py file
     *  Add the environment variables to your system before running the program - TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN
* Tested: This was tested in a windows virtual environment. Python version 3.6     
* Output: The program alerts the user via Twilio sms if any coin breached their alert percentage. It will show the subtotal in USD held of that coin.  
  
