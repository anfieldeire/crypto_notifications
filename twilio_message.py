import os
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure

def message_config(find_percentage):

    for each_list in find_percentage:
        # print("each list {}".format(each_list))
        user_data = each_list[0]
        # print("user data {}".format(user_data))

        main_body = ''

        for each_dict in each_list[1:]:
            # print(each_dict)
            # print(each_dict['current_price'])

            main_body = main_body + "\nCoin {} is {} {}%, in 24hrs, current price is now ${}" \
                                    "\nCoin Subtotal went from ${} to ${}".format(each_dict['id'],
            each_dict['direction'], each_dict['price_change_24'], each_dict['current_price'],
            each_dict['coinsubtotal_24hago'], each_dict['coinsubtotal_now'])

            greeting = 'Hello {}. Crypto Alerts Notification:'.format(user_data['name'])
            number = user_data['phone']

        print(greeting)
        print(main_body)
        print(number)
        return greeting, main_body, number


def send_message():

    greeting, main_body, number = message_config()
    print("from send message")
    print(greeting)
    print(main_body)
    print(number)

    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']

    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                         body="TEST MESSAGE",
                         from_='+1',
                         to='+1'
                     )

    print(message.sid)

#send_message()


if __name__ == '__main__':
    message_config()