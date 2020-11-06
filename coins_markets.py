import requests
import json
from operator import itemgetter
import ast

# global - price, market cap, volume

api_url = 'https://api.coingecko.com/api/v3/coins/markets'
parameters = {
    'vs_currency': 'usd',
    'per_page': 250,
    'price_change_percentage': '1h,24h,7d,14d,30d,200d,1y'}


returned_data_market_cap = []
returned_data_values = []
portfolio_totals = {}
portfolio_percentages = {}


class Crypto:

    def __init__(self, api_url):

        self.api = api_url
        print("Inside init")
        data = Crypto.connection(self)
        self.data = data
        portfolio_amounts = Crypto.read_config_file(self)

        self.portfolio_amounts = portfolio_amounts
        # print("from init print portfolio amounts")
        # print(self.portfolio_amounts)

    def connection(self):
        """ Connect to the coin gecko api and return data for all coins """

        print("inside connect")
        response = requests.get(api_url, params=parameters, timeout=10)
        if response.status_code != 200:
            print("API not available - try again later")
        else:
            data = json.loads(response.text)
            # print(data)
            return data

#            Crypto.get_portfolio_data(self, data)

    def read_config_file(self):
        """ Read configuration file into a dictionary with crypto symbols and amounts """
        with open('portfolio.txt') as f:
            contents = f.read()
            portfolio_amounts = ast.literal_eval(contents)
            print(portfolio_amounts)
        return portfolio_amounts

    def get_portfolio_data(self):
        """ Return list of dictionaries for the coin symbols listed in portfolio data keys """

        portfolio_amounts = Crypto.read_config_file(self)
        portfolio_data = []
        print("Inside retrieve data func")
        for coin in self.data:
            if coin['symbol'] in portfolio_amounts:
                portfolio_data.append(coin)
        print("portfolio data")
        print(portfolio_data)
        return portfolio_data

    def get_current_price(self):
        """ Return list of dictionaries with coin symbol and current price per coin """
        returned_data_price = []
        portfolio_data = Crypto.get_portfolio_data(self)

        for coin in portfolio_data:
            returned_data_price.append({'id': coin['symbol'], 'current_price': coin['current_price']})

        sorted_crypto_price = sorted(returned_data_price, key=itemgetter('current_price'), reverse=True)
        print("\nPortfolio Prices Per Coin\n")

        for dict in sorted_crypto_price:
            for key, value in dict.items():
                if key == 'id':
                    print("Symbol: {}".format(dict['id']), end="")
                else:
                    print(", ${}".format(dict['current_price']))

    def get_price_change24h(self):
        """ Return list of dictionaries with coin symbol and percentage price change 24H"""
        returned_data_price_change24h = []
        portfolio_data = Crypto.get_portfolio_data(self)

        for coin in portfolio_data:
            returned_data_price_change24h.append({'id': coin['symbol'], 'price_change_24h': round(coin['price_change_percentage_24h'], 2)})

        returned_data_price_change24h = sorted(returned_data_price_change24h, key=itemgetter('price_change_24h'),
                                               reverse=True)

        print("\nPercentage Price Change, 24H Descending\n")
        print(returned_data_price_change24h)
        # for dict in returned_data_price_change24h:
        #     for key, value in dict.items():
        #         if key == 'id':
        #             print("Symbol: {}".format(dict['id']), end="")
        #         else:
        #             print(", {}%".format(dict['price_change_24h']))

    def get_price_change7d(self):
        """ Return list of dictionaries with coin symbol and percentage price change 7D """
        returned_data_price_change7d = []
        portfolio_data = Crypto.get_portfolio_data(self)

        for coin in portfolio_data:
            returned_data_price_change7d.append({'id': coin['symbol'], 'price_change_perc_7d': round(
                coin['price_change_percentage_7d_in_currency'], 2)})

        returned_data_price_change7d = sorted(returned_data_price_change7d, key=itemgetter('price_change_perc_7d'), reverse=True)
        print("\nPercentage Price Change, 7D Descending\n")
        for dict in returned_data_price_change7d:
            for key, value in dict.items():
                if key == 'id':
                    print("Symbol: {}".format(dict['id']), end="")
                else:
                    print(", {}%".format(dict['price_change_perc_7d']))

    def get_price_change14d(self):
        """ Return list of dictionaries with coin symbol and percentage price change 14d"""
        returned_data_price_change14d = []
        portfolio_data = Crypto.get_portfolio_data(self)

        for coin in portfolio_data:
            returned_data_price_change14d.append({'id': coin['symbol'], 'price_change_perc_14d': round(
                coin['price_change_percentage_14d_in_currency'], 2)})

        returned_data_price_change14d = sorted(returned_data_price_change14d, key=itemgetter('price_change_perc_14d'), reverse=True)
        print("\nPercentage Price Change, 14D Descending\n")
        for dict in returned_data_price_change14d:
            for key, value in dict.items():
                if key == 'id':
                    print("Symbol: {}".format(dict['id']), end="")
                else:
                    print(", {}%".format(dict['price_change_perc_14d']))

    def get_price_change30d(self):
        """ Return list of dictionaries with coin symbol and percentage price change 30d"""
        returned_data_price_change30d = []
        portfolio_data = Crypto.get_portfolio_data(self)

        for coin in portfolio_data:
            returned_data_price_change30d.append({'id': coin['symbol'], 'price_change_perc_30d': round(
                coin['price_change_percentage_30d_in_currency'], 2)})

        returned_data_price_change30d = sorted(returned_data_price_change30d, key=itemgetter('price_change_perc_30d'),
                                               reverse=True)

        print("\nPercentage Price Change, 30D Descending\n")
        for dict in returned_data_price_change30d:
            for key, value in dict.items():
                if key == 'id':
                    print("Symbol: {}".format(dict['id']), end="")
                else:
                    print(", {}%".format(dict['price_change_perc_30d']))

    def portfolio_subtotals(self):
        """ Return Subtotal amounts for each coin in portfolio based on amount multiple by current price per coin """
        portfolio_amounts = Crypto.read_config_file(self)

        print([portfolio_amounts['btc']])
        returned_subtotals = []
        portfolio_data = Crypto.get_portfolio_data(self)

        for coin in portfolio_data:
            symbol = coin['symbol']
            current_price = coin['current_price']
            #print("Current price 1st: {}".format(current_price))

        for key, value in portfolio_amounts.items():
            for y in portfolio_data:
                if y['symbol'] == key:
                    # print("keys :{}".format(key))
                    coin_subtotal = value * y['current_price']
                    print("Coin amount: {}, by price per coin {}".format(value, y['current_price']))
                    print("Coin subtotal: ${}".format(round(coin_subtotal, 2)))


if __name__ == '__main__':
    coin = Crypto(api_url)
    coin.read_config_file()
  #  coin.
    # coin.get_current_price()
    coin.get_price_change24h()
    # coin.get_price_change7d()
    # coin.get_price_change14d()
    # coin.get_price_change30d()
    # coin.portfolio_subtotals()

    # data = Crypto.connection(coin)
    # if data is not None:
    #     print("from main")
    #     retrieve_data(data)

