import asyncio
from asyncio.tasks import create_task
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
CHANAL_ID_9 = 'https://t.me/nalicniy' #Наличный
CHANAL_ID_10 = 'https://t.me/sezonhalyavi' #Сезон халявы
CHANAL_ID_11 = 'https://t.me/pochtizadarom2021' #Халява! Скидки|Акции|Промокоды
CHANAL_ID_12 = 'https://t.me/vse_besplantno' #Бесплатно или Почти
CHANAL_ID_13 = 'https://t.me/hotprice' #HotPrice от Pepper.ru
CHANAL_ID_14 = 'https://t.me/promokod1y' #Промокоды | Самокат | Перекресток | Пятерочк
CHANAL_ID_15 = 'https://t.me/free_alyans' #Халявный Альянс
CHANAL_ID_16 = 'https://t.me/zzaec' #Заяц | Акции | Распродажа
CHANAL_ID_17 = 'https://t.me/skidkanow' #SkidkaNow | Промокоды
CHANAL_ID_18 = 'https://t.me/bez_zatrat1' #Без затрат🏷
CHANAL_ID_19 = 'https://t.me/Hacupon' #Промокоды | Самокат | Перекресток | Пятерочк
CHANAL_ID_20 = 'https://t.me/LOWCS' #LowCoster
CHANAL_ID_21 = 'https://t.me/pikabu_deals' #Пикабу Скидки
CHANAL_ID_22 = 'https://t.me/find_promo' #Нашли промокод
CHANAL_ID_23 = 'https://t.me/thats_free' #Халявщина 🛍


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


async def parce1():
    await parce_chanal(parce_message, CHANAL_ID_1, 50)        

async def parce2():
    await parce_chanal(parce_message, CHANAL_ID_2, 50)
        
async def parce3():
    await parce_chanal(parce_message, CHANAL_ID_3, 50)

async def parce4():
    await parce_chanal(parce_message, CHANAL_ID_4, 50)

async def parce5():
    await parce_chanal(parce_message, CHANAL_ID_5, 50) 

async def parce6():
    await parce_chanal(parce_message, CHANAL_ID_6, 50)

async def parce7():
    await parce_chanal(parce_message, CHANAL_ID_7, 50)

async def parce8():
    await parce_chanal(parce_message, CHANAL_ID_8, 50)

async def parce9():
    await parce_chanal(parce_message, CHANAL_ID_9, 50)

async def parce10():
    await parce_chanal(parce_message, CHANAL_ID_10, 50)

async def parce11():
    await parce_chanal(parce_message, CHANAL_ID_11, 50)

async def parce12():
    await parce_chanal(parce_message, CHANAL_ID_12, 50)

async def parce13():
    await parce_chanal(parce_message, CHANAL_ID_13, 50)

async def parce14():
    await parce_chanal(parce_message, CHANAL_ID_14, 50)

async def parce15():
    await parce_chanal(parce_message, CHANAL_ID_15, 50)

async def parce16():
    await parce_chanal(parce_message, CHANAL_ID_16, 50)

async def parce17():
    await parce_chanal(parce_message, CHANAL_ID_17, 50)

async def parce18():
    await parce_chanal(parce_message, CHANAL_ID_18, 50)

async def parce19():
    await parce_chanal(parce_message, CHANAL_ID_19, 50)

async def parce20():
    await parce_chanal(parce_message, CHANAL_ID_20, 50)

admitad_parce_list = parce_admitad_data()
for code in admitad_parce_list:
    db_manager.add_admitad_cupons_to_database(code['id'], code['name'], code['description'], code['date_start'], code['date_end'], code['promo'])

while True:

    with client:
        loop = asyncio.get_event_loop()
        tasks = [loop.create_task(parce1()), loop.create_task(parce2()),
        loop.create_task(parce3()), loop.create_task(parce5()),
        loop.create_task(parce6()), loop.create_task(parce7()), loop.create_task(parce8()),
        loop.create_task(parce9()), loop.create_task(parce10()), loop.create_task(parce11()),
        loop.create_task(parce12()), loop.create_task(parce13()), loop.create_task(parce14()), 
        loop.create_task(parce15()), loop.create_task(parce16()), loop.create_task(parce17()),
        loop.create_task(parce18()), loop.create_task(parce19()), loop.create_task(parce20())]
        wait_tasks = asyncio.wait(tasks)
        loop.run_until_complete(wait_tasks)
    
    time.sleep(3600)


