import random
import time

from send import sms
from base import acc
import os
from loguru import logger
import json
#find telehon sessions in directory
ses = []
temp_ses = os.listdir(path="../")
print(os.getcwd())
#print(temp_ses)
for temp_acc in temp_ses:
    if temp_acc[-7:-1] == 'sessio':
        ses.append(temp_acc)
print('base of sessions: ',ses)
messages = ['test send'] #base of messages

#selecting base of users
variant = input("Введите файл базы: ")
if variant[-1] == 't':
    base = acc(variant)
    users = base.get_base_txt()
if variant[-1] == 'v':
    base = acc(variant)
    users = base.get_base_csv()

#vars
user = 0
count_apis = 0
account = 0
myClass = ''
hh = ''

#main program
while True:
    while hh != 'PeerFloodError': #while okey do ->
        if user + 1 > len(users):
            logger.critical(f'Пользователи кончились!') #check users
            time.sleep(120)
            break
        else:
            if count_apis % 50 == 0: #change api_id and hash_id
                json_file = ses[account].replace('session', 'json')
                with open(json_file) as f:
                    data = json.load(f)
                api_cur = data['app_id']
                hash_cur = data['app_hash']
            print(api_cur, hash_cur, ses[account])
            msg = random.choice(messages) #choose message from list
            myClass = sms(ses[account], api_cur, hash_cur, users[user], msg) #send message
            #print(myClass)
            hh = myClass.start()
            if myClass.client.is_user_authorized(): #check to valid sess
                pass
            else:
                account += 1
                print('nor')
            print(hh)
            user += 1
            count_apis += 1

            if hh == 'PeerFloodError' or hh == 'ban': #check errors of spam or ban
                if account+1 > len(ses):
                    logger.critical(f'Аккаунты для спама кончились')
                    time.sleep(120)
                    break
                else:
                    account += 1