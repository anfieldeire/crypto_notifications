import requests

# REF: https://medium.com/@ManHay_Hong/how-to-create-a-telegram-bot-and-send-messages-with-python-4cf314d9fa3e

# https://www.freecodecamp.org/news/telegram-push-notifications-58477e71b2c2/

bot_message = 'whaaasup'

def telegram_bot_sendtext(bot_message):
    bot_token = ''
    bot_chatID = '1314290365'

    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()


test = telegram_bot_sendtext(bot_message)
print(test)
