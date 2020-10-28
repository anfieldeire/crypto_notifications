import requests
import json
from operator import itemgetter
import ast

from excel_writer import excel_writer

# global - price, market cap, volume
# cryptobot - username - crypto_alerts27_bot

api_url = 'https://api.coingecko.com/api/v3/coins/markets'
parameters = {
    'vs_currency': 'usd',
    'per_page': 250,
    'price_change_percentage': '1h,24h,7d,14d,30d,200d,1y'}


class Crypto:

    def __init__(self, api_url):

        self.api = api_url
        data = Crypto.connection(self)
        self.data = data

        portfolio_amounts = Crypto.read_config_file(self)
        self.portfolio_amounts = portfolio_amounts

        portfolio_data = Crypto.get_portfolio_data(self)
        self.portfolio_data = portfolio_data

    def connection(self):
        """ Connect to the coin gecko api and return data for all coins """

        # print("inside connect")
        response = requests.get(api_url, params=parameters, timeout=10)
        if response.status_code != 200:
            print("API error - {} code returned".format(response.status_code))
        else:
            data = json.loads(response.text)
            return data

    def read_config_file(self):
        """ Read configuration file into a dictionary with crypto symbols and amounts """
        with open('portfolio.txt') as f:
            contents = f.read()
            portfolio_amounts = ast.literal_eval(contents)
        return portfolio_amounts

    def get_portfolio_data(self):
        """ Return list of dictionaries for the coin symbols listed in portfolio data keys """

        portfolio_data = []
        # print("Inside retrieve data func")
        for coin in self.data:
            if coin['symbol'] in self.portfolio_amounts:
                portfolio_data.append(coin)

        return portfolio_data

    def get_price_ath(self):
        """ Return list of dictionaries with coin symbol and all time high price """
        title = "Price ATH (USD)"
        returned_data_ath = []
#        portfolio_data = Crypto.get_portfolio_data(self)

        for coin in self.portfolio_data:
            returned_data_ath.append({'id': coin['symbol'], 'ath': coin['ath']})

        returned_data_ath = sorted(returned_data_ath, key=itemgetter('ath'), reverse=True)
        return returned_data_ath, title

    def get_price_change24h(self):
        """ Return list of dictionaries with coin symbol and percentage price change 24H """
        returned_data_price_change24h = []
        title = "% Price Change 24H"

        for coin in self.portfolio_data:
            returned_data_price_change24h.append(
                {'id': coin['symbol'], 'price_change_24h': round(coin['price_change_percentage_24h'], 2)})

        returned_data_price_change24h = sorted(returned_data_price_change24h, key=itemgetter('price_change_24h'),
                                               reverse=True)
        return returned_data_price_change24h, title

    def get_price_change7d(self):
        """ Return list of dictionaries with coin symbol and percentage price change 7D """
        returned_data_price_change7d = []
        title = '% Price Change 7D'

        for coin in self.portfolio_data:
            returned_data_price_change7d.append({'id': coin['symbol'], 'price_change_perc_7d': round(
                coin['price_change_percentage_7d_in_currency'], 2)})

        returned_data_price_change7d = sorted(returned_data_price_change7d, key=itemgetter('price_change_perc_7d'),
                                              reverse=True)
        return returned_data_price_change7d, title

    def get_price_change14d(self):
        """ Return list of dictionaries with coin symbol and percentage price change 14d"""
        returned_data_price_change14d = []
        title = '% Price Change 14D'

        for coin in self.portfolio_data:
            returned_data_price_change14d.append({'id': coin['symbol'], 'price_change_perc_14d': round(
                coin['price_change_percentage_14d_in_currency'], 2)})

        returned_data_price_change14d = sorted(returned_data_price_change14d, key=itemgetter('price_change_perc_14d'), reverse=True)
        return returned_data_price_change14d, title

    def get_price_change30d(self):
        """ Return list of dictionaries with coin symbol and percentage price change 30d"""
        returned_data_price_change30d = []
        title = '% Price Change 30D'

        for coin in self.portfolio_data:
            returned_data_price_change30d.append({'id': coin['symbol'], 'price_change_perc_30d': round(
                coin['price_change_percentage_30d_in_currency'], 2)})

        returned_data_price_change30d = sorted(returned_data_price_change30d, key=itemgetter('price_change_perc_30d'),
                                               reverse=True)
        return returned_data_price_change30d, title

    def get_portfolio_subtotals(self):
        """ Return Subtotal amounts for each coin in portfolio based on amount multiple by current price per coin """
        returned_coin_subtotals = []
        title = 'Portfolio Subtotals (USD)'

        for coin in self.portfolio_data:
            symbol = coin['symbol']
            current_price = coin['current_price']

        for key, value in self.portfolio_amounts.items():
            for y in self.portfolio_data:
                if y['symbol'] == key:
                    # print(y['symbol'])
                    coin_subtotal = round(value * y['current_price'], 2)
                    returned_coin_subtotals.append({'id': y['symbol'], 'coin_subtotal': coin_subtotal})
        # print("coin subtotals")
        # print(returned_coin_subtotals)
        return returned_coin_subtotals, title

    def get_portfolio_total(self):
        portfolio_subtotals = Crypto.get_portfolio_subtotals(self)
        portfolio_total = 0
        title = 'Portfolio Total (USD)'

        for coin in portfolio_subtotals:
            portfolio_total = round(portfolio_total + coin['coin_subtotal'], 2)
        print("Portfolio Total $ {}".format(portfolio_total))
        return portfolio_total, title

    def input_metric(self):
        """ The list defined here in requested metrics, will serve as input to the printer function"""
      #  requested_metrics = ['24h']
        requested_metrics = ['24h', '7d', '14d', '30d', 'ath', 'subtotals', 'total']
        returned_data_price_change = []
        for i in requested_metrics:
            if i == '24h':
                returned_data, title = Crypto.get_price_change24h(self)
                coin.print_data(returned_data, title)
            #    excel_writer(returned_data, title)

            elif i == '7d':
                returned_data, title = Crypto.get_price_change7d(self)
                coin.print_data(returned_data, title)
             #   excel_writer(returned_data, title)

            elif i == '14d':
                returned_data, title = Crypto.get_price_change14d(self)
                coin.print_data(returned_data, title)

            elif i == '30d':
                returned_data, title = Crypto.get_price_change30d(self)
                coin.print_data(returned_data, title)

            elif i == 'ath':
                returned_data, title = Crypto.get_price_ath(self)
                coin.print_data(returned_data, title)

            elif i == 'subtotals':
                returned_data, title = Crypto.get_portfolio_subtotals(self)
                coin.print_data(returned_data, title)

            elif i == 'totals':
                returned_data, title = Crypto.get_portfolio_total(self)
                coin.print_data(returned_data, title)

    def send_to_excel(self):
        requested_metrics = ['24h', '7d']
      #  requested_metrics = ['24h', '7d', '14d', '30d', 'ath', 'subtotals', 'total']
        j = 0

        for i in requested_metrics:
            j = j + 1
            if i == '24h':
                returned_data, title = Crypto.get_price_change24h(self)
                excel_writer(returned_data, title, j)

            elif i == '7d':
                j = j + 1
                returned_data, title = Crypto.get_price_change7d(self)
                excel_writer(returned_data, title, j)

            elif i == '14d':
                j = j +1
                returned_data, title = Crypto.get_price_change14d(self)
                excel_writer(returned_data, title, j)

            elif i == '30d':
                j = j + 1
                returned_data, title = Crypto.get_price_change30d(self)
                excel_writer(returned_data, title, j)

            elif i == 'ath':
                j = j + 1
                returned_data, title = Crypto.get_price_ath(self)
                excel_writer(returned_data, title, j)

            elif i == 'subtotals':
                j = j + 1
                returned_data, title = Crypto.get_portfolio_subtotals(self)
                excel_writer(returned_data, title, j)

            elif i == 'totals':
                j = j + 1
                returned_data, title = Crypto.get_portfolio_total(self)
                excel_writer(returned_data, title, j)


    def print_data(self, returned_data, title):
        """ Generic printer function that will print metrics to screen """
        print('\n{}\n'.format(title))
       # print("\nPercentage Price Change, {} Descending\n".format(i))
        for dict in returned_data:
            for key, value in dict.items():
                if key == 'id':
                    print("Symbol: {}".format(dict['id']), end="")
                else:
                    print(", {}".format(value))


if __name__ == '__main__':

    coin = Crypto(api_url)
    coin.read_config_file()
 #   coin.input_metric()
    coin.send_to_excel()
#    excel_writer()
    # coin.get_price_ath()
    # coin.get_portfolio_subtotals()