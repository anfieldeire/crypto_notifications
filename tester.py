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
        self.portfolio_amounts = Crypto.read_config_file(self)

        print("portfolio amounts")
        print(self.portfolio_amounts)

        self.portfolio_data = Crypto.get_portfolio_data(self)
        # print("self portfolio data")
        # print(self.portfolio_data)

        self.coin_metrics = Crypto.get_coin_metrics(self)
        print("self. coin metrics")
        print(self.coin_metrics)

        self.portfolio_totals = Crypto.get_portfolio_total(self)
        print("portfolio totals")
        print(self.portfolio_totals)


    def connection(self):
        """ Connect to the coin gecko api and return data for all coins """

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

            contents = f.read()
            file_data = ast.literal_eval(contents)
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

    def get_coin_metrics(self):
        """ Get select metrics for each user for each coin in their portfolio """
        title = 'All Coin Metrics Per User'
        coin_metrics = []
        user_list_number = 0

        for each_list in self.portfolio_data:
            user_list = []
            user_data = each_list[0]

            for coin in range(1, len(each_list)):
                coin_amounts = [[[(key, value) for key, value in the_dict.items() if key == each_list[coin]['symbol']]
                                 for the_dict in the_lists[1:]] for the_lists in self.portfolio_amounts]
                coin_amount = coin_amounts[user_list_number][0][0][1]
                coin_price = each_list[coin]['current_price']
                coin_subtotal = coin_price * coin_amount

                user_list.append({'id': each_list[coin]['symbol'], 'ath': each_list[coin]['ath'],
                                  'price_change_24h': each_list[coin]['price_change_percentage_24h'],
                                  'price_change_perc_7d': round(each_list[coin]
                                                                ['price_change_percentage_7d_in_currency'], 2),
                                  'price_change_perc_14d': round(each_list[coin]
                                                                 ['price_change_percentage_14d_in_currency'], 2),
                                  'price_change_perc_30d': round(each_list[coin]
                                                                 ['price_change_percentage_30d_in_currency'], 2),
                                  'current_price': round(each_list[coin]
                                                         ['current_price'], 2),
                                 'coin_subtotal': coin_subtotal})

            user_list_number = user_list_number + 1
            user_list.insert(0, user_data)
            coin_metrics.append(user_list)
     #   print("Coin metrics")
     #   print(coin_metrics, title)
        return coin_metrics, title

    def get_portfolio_total(self):
        """ Get Portfolio total value for each user. Input is portfolio subtotals of each crypto coin
        Output is a list of dicts for each user. First one with user info, second one with the portfolio total"""

        title = 'Portfolio Total (USD)'

        portfolio_totals = self.coin_metrics
        portfolio_totals = portfolio_totals[0]
        all_users_totals = []

        for each_list in portfolio_totals:

            user_portfolio_total = 0
            each_user = []

            for each_dict in each_list[1:]:

                user_data = each_list[0]
                user_portfolio_total = user_portfolio_total + each_dict['coin_subtotal']
            each_user.append({'portfolio_total': user_portfolio_total})
            each_user.insert(0, user_data)

            all_users_totals.append(each_user)
    #    print("Portfolio Totals")
    #    print(all_users_totals)
        return all_users_totals, title

    def find_percentage(self):
        coin_metrics = self.coin_metrics
        coin_metrics = coin_metrics[0]
        returned_list = []

        for each_list in coin_metrics:
            user_data = each_list[0]
            user_list = []

            for each_dict in each_list[1:]:
                price_change_24h = each_dict['price_change_24h']
                price_change_24h = str(price_change_24h)
                first_char = price_change_24h[0]
                print(price_change_24h)
                price_change_24h = float(price_change_24h)
                print("first char minus {}, {}".format(price_change_24h, type(price_change_24h)))
                price_24h_ago = (100 + price_change_24h)
                print("price 24h ago {}".format(price_24h_ago))
                print("ID: {},current price: {},price % 24h ago {}".format(each_dict['id'], each_dict['current_price'], price_24h_ago))

                if price_24h_ago < 100:
                    coinsubtotal_24h_ago = (each_dict['current_price'] / 100) * price_24h_ago
                    print("Price 24 ago {}".format(coinsubtotal_24h_ago))
                    user_list.append({'id': each_dict['id'], 'price_24h_ago': coinsubtotal_24h_ago})
                else:
                    coinsubtotal_24h_ago = (each_dict['current_price'] / price_24h_ago) * 100
                    user_list.append({'id': each_dict['id'], 'price_24h_ago': coinsubtotal_24h_ago})

            user_list.insert(0, user_data)
            returned_list.append(user_list)
        print(returned_list)




    def input_metric(self):
        """ The list defined here in requested metrics, will serve as input to the printer function"""
        requested_metrics = ['24h']

        returned_data_price_change = []




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
#    coin.get_current_price()
    coin.get_coin_metrics()
#    coin.get_portfolio_total()
    coin.input_metric()
    coin.find_percentage()
