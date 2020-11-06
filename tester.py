import requests
import json
from operator import itemgetter
import ast

#from excel_writer import excel_writer

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

        print("portfolio amounts")
        print(self.portfolio_amounts)

        portfolio_data = Crypto.get_portfolio_data(self)
        self.portfolio_data = portfolio_data
        print("self portfolio data")
        print(self.portfolio_data)

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

            allusers_portfolio = []

            print("read config file")
            contents = f.read()
            file_data = ast.literal_eval(contents)
            print(file_data)
            for user_list in file_data:
                user_data = user_list[0]
                user_porfolio = user_list[1]
                # print(type(user_data))
                # print(type(user_porfolio))
                # print("user data {}".format(user_data))
                # print("coin data {}".format(user_porfolio))
                allusers_portfolio.append(user_list)
                # print("user list")
                # print(user_list)
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

    def get_portfolio_subtotals(self):
        """ Return Subtotal amounts for each coin in portfolio based on amount multiple by current price per coin """
        returned_coin_subtotals = []
        title = 'Portfolio Subtotals (USD)'

        for a_list in self.portfolio_amounts:

            returned_coin_subtotals = []
            for each_dict in a_list[1:]:
                print("each dict")
                print(each_dict)

            for key, value in each_dict.items():
                coin_amount = value
                print("Coin amount {} ".format(coin_amount))


            for each_list in self.portfolio_data:
                for the_dict in each_list[1:]:
                    print("The dict {} ".format(the_dict))

                    if the_dict['symbol'] == key:
                        print(the_dict['symbol'])

                # for each_dict in each_list[1:]:
                #     print (each_dict['id'])
                # print(each_list(each_dict['id']))
                # if each_list['symbol'] == key:
                #     print("Match coin")
                #     print(coin)

                    # if coin['symbol'] == key:
                    #     print("match")
                    #     print(key)
                    #     print("coin value {}".format(coin_amount))

                            # if coin['symbol'] == key:
                            #     print("match")
                            #     print(key)
                            #     print("coin value {}".format(coin_amount))



        # for coin in self.portfolio_data:
        #     symbol = coin['symbol']
        #     current_price = coin['current_price']
        #
        # for key, value in self.portfolio_amounts.items():
        #     for y in self.portfolio_data:
        #         if y['symbol'] == key:
        #             # print(y['symbol'])
        #             coin_subtotal = round(value * y['current_price'], 2)
        #             returned_coin_subtotals.append({'id': y['symbol'], 'coin_subtotal': coin_subtotal})
        # print("coin subtotals")
        # print(returned_coin_subtotals)
       # return returned_coin_subtotals, title

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
        requested_metrics = ['24h']
      #  requested_metrics = ['24h', '7d', '14d', '30d', 'ath', 'subtotals', 'total']
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
                # print("returned data , title")
                # print(returned_data, title)
                coin.print_data(returned_data, title)

            elif i == 'subtotals':
                returned_data, title = Crypto.get_portfolio_subtotals(self)
                coin.print_data(returned_data, title)

            elif i == 'totals':
                returned_data, title = Crypto.get_portfolio_total(self)
                coin.print_data(returned_data, title)

    def send_to_excel(self):
        requested_metrics = ['7d', '14d']

        j = 0

        for i in requested_metrics:

            if i == '24h':

                j = j + 1
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

        # for dict in returned_data:
        #     for key, value in dict.items():
        #         if key == 'id':
        #             print("Symbol: {}".format(dict['id']), end="")
        #         else:
        #             print(", {}".format(value))


if __name__ == '__main__':

    coin = Crypto(api_url)
    coin.get_portfolio_data()
#    coin.get_price_ath()
#    coin.get_price_change24h()
#    coin.read_config_file()
 #   coin.input_metric()
 #   coin.get_price_change7d()
 #   coin.get_price_change14d()
 #   coin.get_price_change30d()
  #  coin.send_to_excel()
#    excel_writer()
    # coin.get_price_ath()
    coin.get_portfolio_subtotals()