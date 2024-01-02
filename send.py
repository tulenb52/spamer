from telethon.sync import *
import sys
import logging
from loguru import logger
from telethon.sessions import StringSession
from telethon.errors.rpcerrorlist import PeerFloodError
sys.stderr = open('log.txt', 'w')

class sms:
    phone = ''
    api_id = ''
    api_hash = ''
    id = 0
    msg = ''
    client  = ''
    session_path = ''
    def __init__(self, session_path, api_id, api_hash, id, msg):
        self.session_path = session_path
        self.api_id = api_id
        self.api_hash = api_hash
        self.id = id
        self.msg = msg
        self.client = TelegramClient(session_path, api_id, api_hash)
        self.client.connect()
        if self.client.is_user_authorized():
            return("VALID")
        else:
            return ('NO VALID')


    async def main(self):
        try:
            await self.client.send_message(self.id, self.msg)
            logger.info(f'Отправил сообщение пользователю {self.id}')
        except Exception as E:
            if E == 'PeerFloodError':
                return E
            if E == '':
                return EE

    def start(self):
        with self.client:
            temp = self.client.loop.run_until_complete(self.main())
            return temp
    '''async def spam(self):
        with TelegramClient(self.phone, self.api_id, self.api_hash) as client:
            try:
                loop = asyncio.get_event_loop()
                loop.run_until_complete(client.send_message(self.id, self.msg))
                loop.close()
                print('ok')
                return 0
            except:
                pass


    def start(self):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.spam(self.phone, self.api_id, self.api_hash, self.id, self.msg))
        loop.close()
    def start(self):
        my_thread = threading.Thread(target=self.spam, args=())
        my_thread.start()
    '''