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
        self.data = Crypto.connection(self)
        print("self data")
      #  print(self.data)

        self.portfolio_amounts = Crypto.read_config_file(self)

        print("portfolio amounts")
        print(self.portfolio_amounts)

        self.portfolio_data = Crypto.get_portfolio_data(self)
        print("self portfolio data")
        print(self.portfolio_data)


        self.portfolio_subtotals = Crypto.get_portfolio_subtotals(self)


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
        """ Read configuration file into a list of dictionaries with crypto symbols and amounts """
        with open('..\portfolio.txt') as f:

            allusers_portfolio = []

            print("read config file")
            contents = f.read()
            file_data = ast.literal_eval(contents)
            print(file_data)
            for user_list in file_data:
                user_data = user_list[0]
                user_porfolio = user_list[1]
                allusers_portfolio.append(user_list)

        return allusers_portfolio

    def get_portfolio_data(self):
        """ Return list of dictionaries for the coin symbols listed in portfolio data keys """

        portfolio_data = []
        # print("Inside retrieve data func")

        for each_list in self.portfolio_amounts:
            user_portfolio = [each_list[0]]

            for coin in self.data:
                if coin['symbol'] in each_list[1]:

                    user_portfolio.append(coin)

            portfolio_data.append(user_portfolio)
        return portfolio_data

    def get_price_ath(self):
        """ Return list of dictionaries with coin symbol and all time high price """
        title = "Price ATH (USD)"
        returned_data_ath = []

        for each_list in self.portfolio_data:
            user_list = []
            user_data = each_list[0]

            for coin in range(1, len(each_list)):

                user_list.append({'id': each_list[coin]['symbol'], 'ath': each_list[coin]['ath']})
            user_list = sorted(user_list, key=itemgetter('ath'), reverse=True)
            user_list.insert(0, user_data)
            returned_data_ath.append(user_list)

        return returned_data_ath, title

    def get_price_change24h(self):
        """ Return list of dictionaries with coin symbol and percentage price change 24H """
        returned_data_price_change24h = []
        title = "% Price Change 24H"

        for each_list in self.portfolio_data:
            user_list = []
            user_data = each_list[0]

            for coin in range(1, len(each_list)):

                user_list.append({'id': each_list[coin]['symbol'], 'price_change_24h': each_list[coin]['price_change_percentage_24h']})
            user_list = sorted(user_list, key=itemgetter('price_change_24h'), reverse=True)
            user_list.insert(0, user_data)
            returned_data_price_change24h.append(user_list)

        print("Title {} ".format(title))
        print(returned_data_price_change24h)
        return returned_data_price_change24h, title

    def get_price_change7d(self):
        """ Return list of dictionaries with coin symbol and percentage price change 7D """
        returned_data_price_change7d = []
        title = '% Price Change 7D'

        for each_list in self.portfolio_data:
            user_list = []
            user_data = each_list[0]

            for coin in range(1, len(each_list)):
                user_list.append({'id': each_list[coin]['symbol'],
                                  'price_change_perc_7d': round(each_list[coin]
                                                                ['price_change_percentage_7d_in_currency'], 2)})
            user_list = sorted(user_list, key=itemgetter('price_change_perc_7d'), reverse=True)
            user_list.insert(0, user_data)
            returned_data_price_change7d.append(user_list)

        return returned_data_price_change7d, title

    def get_price_change14d(self):
        """ Return list of dictionaries with coin symbol and percentage price change 14d"""
        returned_data_price_change14d = []
        title = '% Price Change 14D'

        for each_list in self.portfolio_data:
            user_list = []
            user_data = each_list[0]

            for coin in range(1, len(each_list)):
                user_list.append({'id': each_list[coin]['symbol'],
                                  'price_change_perc_14d': round(each_list[coin]
                                                                 ['price_change_percentage_14d_in_currency'],2) })
            user_list = sorted(user_list, key=itemgetter('price_change_perc_14d'), reverse=True)
            user_list.insert(0, user_data)
            returned_data_price_change14d.append(user_list)

        return returned_data_price_change14d, title

    def get_price_change30d(self):
        """ Return list of dictionaries with coin symbol and percentage price change 30d"""
        returned_data_price_change30d = []
        title = '% Price Change 30D'

        for each_list in self.portfolio_data:
            user_list = []
            user_data = each_list[0]

            for coin in range(1, len(each_list)):
                user_list.append({'id': each_list[coin]['symbol'],
                                  'price_change_perc_30d': round(each_list[coin]
                                                                 ['price_change_percentage_30d_in_currency'],2) })
            user_list = sorted(user_list, key=itemgetter('price_change_perc_30d'), reverse=True)
            user_list.insert(0, user_data)
            returned_data_price_change30d.append(user_list)

        return returned_data_price_change30d, title

    def get_current_price(self):
        """ Return Subtotal amounts for each coin in portfolio based on amount multiple by current price per coin """
        title = 'Portfolio Current Prices (USD)'
        current_price = []


        user_list_number = 0
        for each_list in self.portfolio_data:
            user_list = []
            user_coin = []

            user_data = each_list[0]

            for coin in range(1, len(each_list)):

                user_list.append({'id': each_list[coin]['symbol'], 'current_price': round(each_list[coin]
                                                                                          ['current_price'], 2)})
            user_list.insert(0, user_data)
            current_price.append(user_list)
        print("Current Price")
        print(current_price)


    def get_portfolio_subtotals(self):
        """ Return Subtotal amounts for each coin in each users portfolio based on amount multiplied by current price
         per coin """
        title = 'Portfolio Subtotals For Each Coin (USD)'

        coin_subtotals = []
        user_list_number = 0

        for each_list in self.portfolio_data:
            user_coin = []
            user_data = each_list[0]

            for coin in range(1, len(each_list)):

                coin_amounts = [[[(key, value) for key, value in the_dict.items() if key == each_list[coin]['symbol']]
                                 for the_dict in the_lists[1:]] for the_lists in self.portfolio_amounts]
                coin_amount = coin_amounts[user_list_number][0][0][1]
                coin_price = each_list[coin]['current_price']
                coin_subtotal = coin_price * coin_amount
                user_coin.append({'id': each_list[coin]['symbol'], 'coin_subtotal': coin_subtotal})

            user_list_number = user_list_number + 1
            user_coin.insert(0, user_data)
            coin_subtotals.append(user_coin)

        return coin_subtotals, title

    def get_portfolio_total(self):
        """ Get Portfolio total value for each user. Input is portfolio subtotals of each crypto coin
        Output is a list of dicts for each user. First one with user info, second one with the portfolio total"""

        title = 'Portfolio Total (USD)'

        portfolio_subtotals = self.portfolio_subtotals[0]
        all_users_totals = []

        for each_list in portfolio_subtotals:

            user_portfolio_total = 0
            each_user = []

            for each_dict in each_list[1:]:
                user_data = each_list[0]
                user_portfolio_total = user_portfolio_total + each_dict['coin_subtotal']
            each_user.append({'portfolio_total': user_portfolio_total})
            each_user.insert(0, user_data)

            all_users_totals.append(each_user)
        return all_users_totals, title

    def input_metric(self):
        """ The list defined here in requested metrics, will serve as input to the printer function"""
        requested_metrics = ['24h', '7d']

        returned_data_price_change = []
        for i in requested_metrics:
            if i == '24h':
                returned_data, title = Crypto.get_price_change24h(self)
                coin.print_data(returned_data, title)
                excel_writer(returned_data, title)

            elif i == '7d':
                returned_data, title = Crypto.get_price_change7d(self)
           #     coin.print_data(returned_data, title)
           #     excel_writer(returned_data, title)

            elif i == '14d':
                returned_data, title = Crypto.get_price_change14d(self)
            #    coin.print_data(returned_data, title)

            elif i == '30d':
                returned_data, title = Crypto.get_price_change30d(self)
            #    coin.print_data(returned_data, title)

            elif i == 'ath':
                returned_data, title = Crypto.get_price_ath(self)
             #   coin.print_data(returned_data, title)

            elif i == 'subtotals':
                returned_data, title = Crypto.get_portfolio_subtotals(self)
             #   coin.print_data(returned_data, title)

            elif i == 'totals':
                returned_data, title = Crypto.get_portfolio_total(self)
             #   coin.print_data(returned_data, title)


    def print_data(self, returned_data, title):
        """ Generic printer function that will print metrics to screen """
        print('\n{}'.format(title))

        for a_list in returned_data:
            for a_dict in a_list:

                for key, value in a_dict.items():
                    if key == 'name':
                        print("\nPortfolio info for {}\n".format(a_dict['name']))
                    elif key == 'id':
                        print("Symbol: {}".format(a_dict['id']), end="" ', ' )
                    elif key != 'phone':
                        print(value)

if __name__ == '__main__':

    coin = Crypto(api_url)
    coin.get_portfolio_data()
    coin.get_current_price()
#    coin.get_portfolio_total()
    coin.input_metric()
