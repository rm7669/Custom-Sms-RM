# --------Api Owner Pikachu ---------#
#--------Tyoe : Half Custom sms ---------#
# ------Coded by Suyaib--------#
# ------tg : Termux Education Empire ---------#
import os
from os import system as Suyaib
try:
    import requests
except ModuleNotFoundError:
    Suyaib('pip install requests')
    import requests


def send_sms(phone_number, message):
    api_url = "https://www.pikachubd.co/API/csms.php"
    params = {
        "num": phone_number,
        "msg": message
    }

    response = requests.get(api_url, params=params)

    if response.status_code == 200:
        print("[ <> ] SMS sent successfully to", phone_number)
    else:
        print("[ <> ] Failed to send SMS")

if __name__ == '__main__':
    while True:
        suyaib = input("[ <> ] Enter Target number : ")
        bishnu = input("[ <> ] Enter your message : ")
        send_sms(suyaib, bishnu)

        restart = input("[ <> ] Do you want to send another SMS? (y/n): ")
        if restart.lower() != 'y':
            break