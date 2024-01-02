from telethon import *
from telethon.tl.functions.account import UpdateProfileRequest
from telethon.tl.functions.photos import UploadProfilePhotoRequest
import asyncio
import json
import os

async def main(ses):
    json_file = ses.replace('session', 'json')
    with open(json_file) as f:
        data = json.load(f)
    client = TelegramClient(ses, data['app_id'], data['app_hash'])
    async with client:
        await client(UpdateProfileRequest(first_name="Manager"))
        await client(UpdateProfileRequest(last_name='Ivan'))
        await client(UpdateProfileRequest(about='22'))
        await client(UploadProfilePhotoRequest(file = await client.upload_file('temp2.jpg')))

allSessions = []
temp_ses = os.listdir(path="..")
for temp_acc in temp_ses:
    if temp_acc[-7:-1] == 'sessio':
        allSessions.append(temp_acc)
print('base of sessions: ', allSessions)

for current_session in allSessions:
    asyncio.get_event_loop().run_until_complete(main(current_session))