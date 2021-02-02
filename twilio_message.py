import os
from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure

def message_config(find_percentage):

    returned_list = []

    for each_list in find_percentage:

        user_data = each_list[0]
        main_body = ''
        user_list = []

        for each_dict in each_list[1:]:

            main_body = main_body + "\nCoin {} is {} {}%, in 24hrs, current price is now ${}" \
                                    "\n{} Subtotal went from ${} to ${}".format(each_dict['id'],each_dict['direction'],
            each_dict['price_change_24'], each_dict['current_price'], each_dict['id'],
            each_dict['coinsubtotal_24hago'], each_dict['coinsubtotal_now'])
            greeting = 'Hello {}. Crypto Alerts Notification:'.format(user_data['name'])
            number = user_data['phone']
        user_list.append(main_body)
        user_list.insert(0, number)
        user_list.insert(1, greeting)
        returned_list.append(user_list)
    print(returned_list)
    send_message(returned_list)


def send_message(returned_list):

    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']

    client = Client(account_sid, auth_token)

    for alert_data in returned_list:
        phone_number = alert_data[0]
        greeting = alert_data[1]
        message_body = alert_data[2]

        message = client.messages \
                        .create(
                         body='{}, \n {}'.format(greeting, message_body),
                         from_='+12017785820 ',
                         to='{}'.format(phone_number)
                     )

    print(message.sid)


if __name__ == '__main__':
    message_config()