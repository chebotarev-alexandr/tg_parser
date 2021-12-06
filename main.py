import asyncio
from telethon import TelegramClient, events
from db_operation.db import DB_Operation
from parce_fnc.parce_fnc import parce_message
from admitad_src.admitad_script import parce_admitad_data
from threading import Thread
import time
APP_ID = '3333633'
APP_HASH = '66de8082edcbd92e39970c7e7b4e9c11'
CHANAL_ID_1 = 'https://t.me/BESPIATNO' #Халява 2.0 
CHANAL_ID_2 = 'https://t.me/wow_free' #Халява!!
CHANAL_ID_3 = 'https://t.me/skidkavip' # Skidkavip|GodSkidonus
CHANAL_ID_4 = 'https://telega.in/tme/joinchat/SX1bIIYk48Y4ZWNi' #ХАЛЯВЩИК промокоды и скидки
CHANAL_ID_5 = 'https://t.me/farmimhalyvu' #ФАРМИМ ХАЛЯВУ
CHANAL_ID_6 = 'https://t.me/halyavalegion' #Халявный Легион
CHANAL_ID_7 = 'https://t.me/halyavniylis' #Халявный Лис 
CHANAL_ID_8 = 'https://t.me/free_coupons' #ХаК - Халява акции Купоны

client = TelegramClient('my_client', APP_ID, APP_HASH)

db_manager = DB_Operation()

async def parce_chanal(parce_func, chanal_name, limit=10):
    messages = await client.get_messages(await client.get_entity(chanal_name), limit=limit)
    for message in messages:
        res = parce_func(message.message, message.date)
        if res[0]:
            db_manager.add_subscription_and_cupon_to_database(message.message, res[0][0], chanal_name)

#getting only new messages 
@client.on(events.NewMessage(chats=('chat_name')))
async def normal_handler(event):
    print(event.message)
    print(event.message.to_dict()['message'])


async def parce_first_chanal():
    await parce_chanal(parce_message, CHANAL_ID_1, 50)        

async def parce_second_chanal():
    await parce_chanal(parce_message, CHANAL_ID_2, 50)
        
async def parce_third_chanal():
    await parce_chanal(parce_message, CHANAL_ID_3, 50)

async def parce_foreth_channal():
    await parce_chanal(parce_message, CHANAL_ID_4, 50)

async def parce_fives_chanal():
    await parce_chanal(parce_message, CHANAL_ID_5, 50) 

async def parce_six_chanal():
    await parce_chanal(parce_message, CHANAL_ID_6, 50)

async def parce_seven_chanal():
    await parce_chanal(parce_message, CHANAL_ID_7, 50)

# admitad_parce_list = parce_admitad_data()
# for code in admitad_parce_list:
#     db_manager.add_admitad_cupons_to_database(code['id'], code['name'], code['description'], code['date_start'], code['date_end'], code['promo'])

while True:

    with client:
        loop = asyncio.get_event_loop()
        tasks = [loop.create_task(parce_first_chanal()), loop.create_task(parce_second_chanal()),
        loop.create_task(parce_third_chanal()),
        loop.create_task(parce_fives_chanal()), loop.create_task(parce_six_chanal()), loop.create_task(parce_seven_chanal())]
        wait_tasks = asyncio.wait(tasks)
        loop.run_until_complete(wait_tasks)
    
    time.sleep(3600)


