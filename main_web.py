from flask import Flask, request
from telebot import types
import telebot
import os

app = Flask(__name__)
TOKEN = os.environ.get('TOKEN')
bot = telebot.TeleBot('5416512263:AAFvQ7A8kR1AyqQN15IO4BWkOgqYaEzLBXA')

with open('courses.txt') as file:
    courses = [item.split(',') for item in file]

with open('schedule.txt') as file:
    courses_plan = {
        'start': [],
        'pro': [],
        'other': []
    }

    for item in file:
        if 'start' in item.lower():
            courses_plan['start'].append(item)
        elif 'pro' in item.lower():
            courses_plan['pro'].append(item)
        else:
            courses_plan['other'].append(item)

my_dict = {'AT-AT': 1.40, 'AT-BE': 1.40, 'AT-CH': 1.75, 'AT-CZ': 1.40, 'AT-DE': 1.40, 'AT-DK': 1.75, 'AT-ES': 1.46,
           'AT-FR': 1.75, 'AT-GB': 1.75, 'AT-HU': 1.64, 'AT-IT': 1.28, 'AT-NL': 1.40, 'AT-PL': 1.02, 'AT-RO': 1.99,
           'AT-LT': 1.40, 'AT-LV': 1.40, 'AT-EE': 1.40, 'AT-BG': 1.69, 'AT-GR': 1.69, 'AT-HR': 1.64, 'AT-SE': 1.87,
           'AT-SL': 1.40, 'AT-SK': 1.40, 'BE-AT': 1.40, 'BE-BE': 1.40, 'BE-CH': 1.75, 'BE-CZ': 1.40, 'BE-DE': 1.40,
           'BE-DK': 1.87, 'BE-ES': 1.34, 'BE-FR': 1.81, 'BE-GB': 1.75, 'BE-HU': 1.58, 'BE-IT': 1.28, 'BE-NL': 1.40,
           'BE-PL': 1.34, 'BE-RO': 1.69, 'BE-LT': 1.34, 'BE-LV': 1.34, 'BE-EE': 1.34, 'BE-BG': 1.69, 'BE-GR': 1.69,
           'BE-HR': 1.64, 'BE-SE': 1.87, 'BE-SL': 1.40, 'BE-SK': 1.40, 'CH-AT': 1.05, 'CH-BE': 1.05, 'CH-CH': 1.40,
           'CH-CZ': 1.05, 'CH-DE': 1.05, 'CH-DK': 1.75, 'CH-ES': 1.05, 'CH-FR': 1.28, 'CH-GB': 1.64, 'CH-HU': 1.05,
           'CH-IT': 1.05,  'CH-NL': 1.05, 'CH-PL': 0.99, 'CH-RO': 1.69, 'CH-LT': 1.17, 'CH-LV': 1.17, 'CH-EE': 1.17,
           'CH-BG': 1.40, 'CH-GR': 1.40, 'CH-HR': 1.40, 'CH-SE': 1.64, 'CH-SL': 1.05, 'CH-SK': 1.05, 'CZ-AT': 1.40,
           'CZ-BE': 1.40, 'CZ-CH': 1.75, 'CZ-CZ': 1.40, 'CZ-DE': 1.40, 'CZ-DK': 1.87, 'CZ-ES': 1.40, 'CZ-FR': 1.81,
           'CZ-GB': 1.75, 'CZ-HU': 1.58, 'CZ-IT': 1.28, 'CZ-NL': 1.40, 'CZ-PL': 1.05, 'CZ-RO': 1.69, 'CZ-LT': 1.17,
           'CZ-LV': 1.17, 'CZ-EE': 1.17, 'CZ-BG': 1.69, 'CZ-GR': 1.69, 'CZ-HR': 1.64, 'CZ-SE': 1.87, 'CZ-SL': 1.40,
           'CZ-SK': 1.40, 'DE-AT': 1.40, 'DE-BE': 1.40, 'DE-CH': 1.75, 'DE-CZ': 1.40, 'DE-DE': 1.40, 'DE-DK': 1.75,
           'DE-ES': 1.34, 'DE-FR': 1.76, 'DE-GB': 1.75, 'DE-HU': 1.58, 'DE-IT': 1.23, 'DE-NL': 1.40, 'DE-PL': 0.99,
           'DE-RO': 1.69, 'DE-LT': 0.93, 'DE-LV': 0.93, 'DE-EE': 0.93, 'DE-BG': 1.69, 'DE-GR': 1.69, 'DE-HR': 1.64,
           'DE-SE': 1.87, 'DE-SL': 1.52, 'DE-SK': 1.52, 'DK-AT': 1.05, 'DK-BE': 0.93, 'DK-CH': 1.05, 'DK-CZ': 0.93,
           'DK-DE': 1.05, 'DK-DK': 1.40, 'DK-ES': 1.05, 'DK-FR': 1.40, 'DK-GB': 1.40, 'DK-HU': 1.40, 'DK-IT': 1.05,
           'DK-NL': 0.93, 'DK-PL': 0.99, 'DK-RO': 1.69, 'DK-LT': 1.05, 'DK-LV': 1.05, 'DK-EE': 1.05, 'DK-BG': 1.40,
           'DK-GR': 1.40, 'DK-HR': 1.40, 'DK-SE': 1.40, 'DK-SL': 1.17, 'DK-SK': 1.17, 'ES-AT': 1.34, 'ES-BE': 1.46,
           'ES-CH': 1.75, 'ES-CZ': 1.40, 'ES-DE': 1.46, 'ES-DK': 1.75, 'ES-ES': 1.40, 'ES-FR': 1.69, 'ES-GB': 1.75,
           'ES-HU': 1.52, 'ES-IT': 1.34, 'ES-NL': 1.34, 'ES-PL': 1.34, 'ES-RO': 1.52, 'ES-LT': 1.28, 'ES-LV': 1.28,
           'ES-EE': 1.28, 'ES-BG': 1.64, 'ES-GR': 1.64, 'ES-HR': 1.64, 'ES-SE': 1.64, 'ES-SL': 1.40, 'ES-SK': 1.40,
           'FR-AT': 1.05, 'FR-BE': 0.99, 'FR-CH': 1.52, 'FR-CZ': 0.99, 'FR-DE': 1.04, 'FR-DK': 1.40, 'FR-ES': 1.11,
           'FR-FR': 1.40, 'FR-GB': 1.75, 'FR-HU': 1.16, 'FR-IT': 1.05, 'FR-NL': 0.99, 'FR-PL': 1.05, 'FR-RO': 1.64,
           'FR-LT': 1.17, 'FR-LV': 1.17, 'FR-EE': 1.17, 'FR-BG': 1.40, 'FR-GR': 1.40, 'FR-HR': 1.40, 'FR-SE': 1.40,
           'FR-SL': 1.05, 'FR-SK': 1.05, 'GB-AT': 1.05, 'GB-BE': 1.05, 'GB-CH': 1.17, 'GB-CZ': 1.05, 'GB-DE': 1.05,
           'GB-DK': 1.40, 'GB-ES': 1.05, 'GB-FR': 1.05, 'GB-GB': 1.40, 'GB-HU': 1.05, 'GB-IT': 1.05, 'GB-NL': 1.05,
           'GB-PL': 1.05, 'GB-RO': 1.52, 'GB-LT': 1.40, 'GB-LV': 1.05, 'GB-EE': 1.05, 'GB-BG': 1.40, 'GB-GR': 1.40,
           'GB-HR': 1.40, 'GB-SE': 1.40, 'GB-SL': 1.05, 'GB-SK': 1.05, 'HU-AT': 1.17, 'HU-BE': 1.28, 'HU-CH': 1.75,
           'HU-CZ': 1.23, 'HU-DE': 1.23, 'HU-DK': 1.40, 'HU-ES': 1.28, 'HU-FR': 1.65, 'HU-GB': 1.75, 'HU-HU': 1.40,
           'HU-IT': 1.28, 'HU-NL': 1.23, 'HU-PL': 0.93, 'HU-RO': 1.87, 'HU-LT': 1.17, 'HU-LV': 1.17, 'HU-EE': 1.17,
           'HU-BG': 1.58, 'HU-GR': 1.58, 'HU-HR': 1.52, 'HU-SE': 1.87, 'HU-SL': 1.40, 'HU-SK': 1.40, 'IT-AT': 1.52,
           'IT-BE': 1.52, 'IT-CH': 1.75, 'IT-CZ': 1.52, 'IT-DE': 1.58, 'IT-DK': 1.75, 'IT-ES': 1.52, 'IT-FR': 1.75,
           'IT-GB': 1.75, 'IT-HU': 1.52, 'IT-IT': 1.40, 'IT-NL': 1.52, 'IT-PL': 1.34, 'IT-RO': 1.69, 'IT-LT': 1.52,
           'IT-LV': 1.52, 'IT-EE': 1.52, 'IT-BG': 1.69, 'IT-GR': 1.75, 'IT-HR': 1.52, 'IT-SE': 1.64, 'IT-SL': 1.64,
           'IT-SK': 1.64, 'NL-AT': 1.40, 'NL-BE': 1.40, 'NL-CH': 1.75, 'NL-CZ': 1.40, 'NL-DE': 1.40, 'NL-DK': 1.87,
           'NL-ES': 1.46, 'NL-FR': 1.81, 'NL-GB': 1.75, 'NL-HU': 1.52, 'NL-IT': 1.28, 'NL-NL': 1.40, 'NL-PL': 1.34,
           'NL-RO': 1.69, 'NL-LT': 1.46, 'NL-LV': 1.46, 'NL-EE': 1.46, 'NL-BG': 1.69, 'NL-GR': 1.69, 'NL-HR': 1.64,
           'NL-SE': 1.87, 'NL-SL': 1.40, 'NL-SK': 1.52, 'PL-AT': 1.46, 'PL-BE': 1.46, 'PL-CH': 1.81, 'PL-CZ': 1.40,
           'PL-DE': 1.46, 'PL-DK': 1.75, 'PL-ES': 1.46, 'PL-FR': 1.58, 'PL-GB': 1.75, 'PL-HU': 1.58, 'PL-IT': 1.23,
           'PL-NL': 1.40, 'PL-PL': 1.40, 'PL-RO': 1.75, 'PL-LT': 1.64, 'PL-LV': 1.64, 'PL-EE': 1.64, 'PL-BG': 1.87,
           'PL-GR': 1.87, 'PL-HR': 1.46, 'PL-SE': 1.64, 'PL-SL': 1.46, 'PL-SK': 1.52, 'RO-AT': 0.93, 'RO-BE': 0.93,
           'RO-CH': 1.34, 'RO-CZ': 0.93, 'RO-DE': 0.93, 'RO-DK': 0.93, 'RO-ES': 1.11, 'RO-FR': 1.40, 'RO-GB': 1.40,
           'RO-HU': 1.34, 'RO-IT': 0.93, 'RO-NL': 0.93, 'RO-PL': 0.88, 'RO-RO': 1.40, 'RO-LT': 1.05, 'RO-LV': 1.11,
           'RO-EE': 1.11, 'RO-BG': 1.40, 'RO-GR': 1.40, 'RO-HR': 1.40, 'RO-SE': 0.06, 'RO-SL': 0.93, 'RO-SK': 0.93,
           'LT-AT': 0.99, 'LT-BE': 0.93, 'LT-CH': 1.17, 'LT-CZ': 0.93, 'LT-DE': 0.99, 'LT-DK': 1.23, 'LT-ES': 1.11,
           'LT-FR': 1.34, 'LT-GB': 1.58, 'LT-HU': 1.52, 'LT-IT': 2.16, 'LT-NL': 0.93, 'LT-PL': 1.17, 'LT-RO': 1.52,
           'LT-LT': 1.34, 'LT-LV': 1.34, 'LT-EE': 1.34, 'LT-BG': 1.64, 'LT-GR': 1.81, 'LT-HR': 1.34, 'LT-SE': 1.58,
           'LT-SL': 1.17, 'LT-SK': 1.28, 'LV-AT': 1.05, 'LV-BE': 0.99, 'LV-CH': 1.23, 'LV-CZ': 0.99, 'LV-DE': 1.05,
           'LV-DK': 1.28, 'LV-ES': 1.17, 'LV-FR': 1.40, 'LV-GB': 1.75, 'LV-HU': 1.58, 'LV-IT': 1.05, 'LV-NL': 0.99,
           'LV-PL': 1.17, 'LV-RO': 1.52, 'LV-LT': 1.40, 'LV-LV': 1.40, 'LV-EE': 1.40, 'LV-BG': 1.69, 'LV-GR': 1.87,
           'LV-HR': 1.40, 'LV-SE': 1.64, 'LV-SL': 1.23, 'LV-SK': 1.34, 'EE-AT': 0.99, 'EE-BE': 0.93, 'EE-CH': 1.23,
           'EE-CZ': 0.93, 'EE-DE': 0.99, 'EE-DK': 1.28, 'EE-ES': 1.11, 'EE-FR': 1.34, 'EE-GB': 1.69, 'EE-HU': 1.52,
           'EE-IT': 0.99, 'EE-NL': 0.93, 'EE-PL': 1.11, 'EE-RO': 1.52, 'EE-LT': 1.34, 'EE-LV': 1.34, 'EE-EE': 1.34,
           'EE-BG': 1.64, 'EE-GR': 1.81, 'EE-HR': 1.34, 'EE-SE': 1.58, 'EE-SL': 1.17, 'EE-SK': 1.28, 'BG-AT': 1.11,
           'BG-BE': 1.11, 'BG-CH': 1.40, 'BG-CZ': 1.11, 'BG-DE': 1.11, 'BG-DK': 1.40, 'BG-ES': 1.17, 'BG-FR': 1.40,
           'BG-GB': 1.40, 'BG-HU': 1.23, 'BG-IT': 1.11, 'BG-NL': 1.11, 'BG-PL': 0.88, 'BG-RO': 1.52, 'BG-LT': 1.11,
           'BG-LV': 1.11, 'BG-EE': 1.11, 'BG-BG': 1.40, 'BG-GR': 1.87, 'BG-HR': 1.40, 'BG-SE': 1.40, 'BG-SL': 1.11,
           'BG-SK': 1.17, 'GR-AT': 1.11, 'GR-BE': 1.11, 'GR-CH': 1.40, 'GR-CZ': 1.11, 'GR-DE': 1.11, 'GR-DK': 1.40,
           'GR-ES': 1.17, 'GR-FR': 1.40, 'GR-GB': 1.40, 'GR-HU': 1.23, 'GR-IT': 1.05, 'GR-NL': 1.11, 'GR-PL': 0.88,
           'GR-RO': 1.52, 'GR-LT': 0.99, 'GR-LV': 1.05, 'GR-EE': 1.05, 'GR-BG': 1.40, 'GR-GR': 1.40, 'GR-HR': 1.28,
           'GR-SE': 1.40, 'GR-SL': 1.11, 'GR-SK': 1.17, 'HR-AT': 1.17, 'HR-BE': 1.17, 'HR-CH': 1.40, 'HR-CZ': 1.17,
           'HR-DE': 1.17, 'HR-DK': 1.40, 'HR-ES': 1.28, 'HR-FR': 1.40, 'HR-GB': 1.40, 'HR-HU': 1.28, 'HR-IT': 1.17,
           'HR-NL': 1.17, 'HR-PL': 0.93, 'HR-RO': 1.52, 'HR-LT': 1.17, 'HR-LV': 1.17, 'HR-EE': 1.17, 'HR-BG': 1.87,
           'HR-GR': 1.87, 'HR-HR': 1.40, 'HR-SE': 1.40, 'HR-SL': 1.64, 'HR-SK': 1.40, 'SE-AT': 0.93, 'SE-BE': 0.93,
           'SE-CH': 1.17, 'SE-CZ': 0.93, 'SE-DE': 0.93, 'SE-DK': 1.40, 'SE-ES': 1.17, 'SE-FR': 1.40, 'SE-GB': 1.40,
           'SE-HU': 0.93, 'SE-IT': 0.93, 'SE-NL': 0.93, 'SE-PL': 1.17, 'SE-RO': 1.64, 'SE-LT': 1.40, 'SE-LV': 1.40,
           'SE-EE': 1.40, 'SE-BG': 1.87, 'SE-GR': 1.87, 'SE-HR': 1.64, 'SE-SE': 1.40, 'SE-SL': 0.93, 'SE-SK': 0.93,
           'SL-AT': 1.40, 'SL-BE': 1.40, 'SL-CH': 1.75, 'SL-CZ': 1.40, 'SL-DE': 1.28, 'SL-DK': 1.64, 'SL-ES': 1.40,
           'SL-FR': 1.75, 'SL-GB': 1.75, 'SL-HU': 1.40, 'SL-IT': 1.17, 'SL-NL': 1.40, 'SL-PL': 1.75, 'SL-RO': 1.64,
           'SL-LT': 1.46, 'SL-LV': 1.46, 'SL-EE': 1.46, 'SL-BG': 1.87, 'SL-GR': 1.87, 'SL-HR': 2.10, 'SL-SE': 1.87,
           'SL-SL': 1.40, 'SL-SK': 1.40, 'SK-AT': 1.40, 'SK-BE': 1.40, 'SK-CH': 1.75, 'SK-CZ': 1.40, 'SK-DE': 1.28,
           'SK-DK': 1.64, 'SK-ES': 1.40, 'SK-FR': 1.75, 'SK-GB': 1.75, 'SK-HU': 1.40, 'SK-IT': 1.17, 'SK-NL': 1.28,
           'SK-PL': 0.99, 'SK-RO': 1.64, 'SK-LT': 1.28, 'SK-LV': 1.28, 'SK-EE': 1.28, 'SK-BG': 1.64, 'SK-GR': 1.64,
           'SK-HR': 1.40, 'SK-SE': 1.87, 'SK-SL': 1.40, 'SK-SK': 1.40}
title = ''


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    new_route = types.KeyboardButton('/start')
    markup.add(new_route)
    bot.send_message(message.chat.id,
                     f"привет {message.from_user.first_name},\nПо братски напиши от куда и куда едешь ?",
                     reply_markup=markup)
    bot.register_next_step_handler(message, km)


def km(message):
    if str(message.text).upper() in my_dict:
        global title
        title = str(message.text).upper()
        bot.send_message(message.chat.id, f"Сколько км тулить?")
        bot.register_next_step_handler(message, my_calc)
    else:
        bot.send_message(message.chat.id, f"not sure the route is correct\ntry again")
        exit()


def my_calc(message):
    if str(message.text).isdigit():
        res = my_dict[f'{title}'] * float(message.text)
        bot.send_message(message.chat.id, f'{title} - {my_dict[f"{title}"]}\n{my_dict[f"{title}"]} * '
                                          f'{float(message.text)} = {res}')
    else:
        bot.send_message(message.chat.id, f"try again")
        exit()


@app.route('/' + TOKEN, methods=['POST'])
def get_message():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "Python Telegram Bot 25-11-2022", 200


@app.route('/')
def main():
    bot.remove_webhook()
    bot.set_webhook(url='https://first-my-bot.herokuapp.com/' + TOKEN)
    return "Python Telegram Bot", 200


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
