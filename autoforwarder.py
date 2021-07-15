from telethon.sync import TelegramClient, events

api_id=1381030
api_hash='ce6fe3fd77c440ca544eb4594c1326fb'

client = TelegramClient('abhi', api_id, api_hash)

@client.on(events.NewMessage)
async def handler(event):
 chat= await event.get_chat()
 chat_id = event.chat_id
 print("{}{}".format(chat_id,chat))


 if chat_id == -1001242185176:
     await client.send_message(1416757836,event.raw_text)

 if chat_id == -1001152070369:
     await client.send_message(1416757836,event.raw_text)

 if chat_id == -1001496705628:
     await client.send_message(1416757836,event.raw_text)

 if chat_id == -1001213232901:
     await client.send_message(1416757836,event.raw_text)

 if chat_id == -1001413587185:
     await client.send_message(1416757836,event.raw_text)

 if chat_id == -1001282253346:
     await client.send_message(1416757836,event.raw_text)

 if chat_id == -1001357275556:
     await client.send_message(1416757836,event.raw_text)

 if chat_id == -1001404980209:
     await client.send_message(1416757836,event.raw_text)

 if chat_id == -1001339088570:
     await client.send_message(1416757836,event.raw_text)
     
 if chat_id == -1001300233330:
     await client.send_message(1416757836,event.raw_text)
     


# chat_id == 1416757836




client.start()
client.run_until_disconnected()
