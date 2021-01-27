import requests, json, time
import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton


intro = ('CEK RESI EXPEDISI\n\n'
'Command\n'
'1. /sicepat [no resi]\n'
'2. /jnt [no resi]\n'
'3. /jne [no resi]\n'
'4. /pos [no resi]\n'
'5. /tiki [no resi]\n'
'6. /anteraja [no resi]\n'
'7. /wahana [no resi]\n'
'8. /ninja [no resi]\n'
'9. /lion [no resi]\n'
'10. /shopee express [no resi]\n\n'
'note : tidak usah menggunakan [ ]\n'
'example :\n'
'/sicepat 000805298253\n\n\n'
'Jika ada masalah dalam BOT hubungi @dikanaan'
)




def head(message):
    id_chat = message['chat']['id']
    command = message['text']
    dari = message['from']['id']
    nama = message['from']['first_name']
    uer = message['from']['username']
    print(nama+'\n'+uer+'\n'+command)
    api_bot.sendMessage(id_chat, 'Instagram : @dikanaan')
    if command == '/start' or command == '/help':
        content_type, chat_type, id_chat = telepot.glance(message)
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
                   [InlineKeyboardButton(text='Donasi', url='https://saweria.co/dikanaan')],])
        api_bot.sendMessage (id_chat, str(intro),reply_markup=keyboard)
        
        
    elif '/sicepat' in command:
      import requests, json
      resi = command[9:]
      print(resi)
      url = "https://api.binderbyte.com/v1/track?api_key=a8b0efaea4329e741aeaca527630d67b05288432b68af71da79a1a7c0085542d&courier=sicepat&awb="+str(resi)
      resp = requests.get(url)
      
      if resp.status_code == 200:
        json = resp.json()['data']
        summary = json['summary']
        courier = summary['courier']
        service = summary['service']
        status = summary['status']

        detail = json['detail']
        dari = detail['origin']
        destination = detail['destination']
        shipper = detail['shipper']
        receiver = detail['receiver']

        history = json['history'][0]
        date = history['date']
        desc = history['desc']
    
        api_bot.sendMessage(id_chat,'Expedisi\nKurir        : '+courier+'\nService   : '+service+'\nStatus    : '+status)
        api_bot.sendMessage(id_chat,'Detail\nDari     > '+dari+'\nTujuan   > '+destination+'\nPengirim > '+shipper+'\nPenerima > '+receiver)
        api_bot.sendMessage(id_chat,'Tracking\nTanggal   : '+date+'\nPosisi       : '+desc)
      if resp.status_code == 400:
        api_bot.sendMessage(id_chat,'No resi tidak terdaftar')
        
    elif '/jne' in command:
      import requests, json
      resi = command[5:]
      print(resi)
      url = "https://api.binderbyte.com/v1/track?api_key=a8b0efaea4329e741aeaca527630d67b05288432b68af71da79a1a7c0085542d&courier=jne&awb="+str(resi)
      resp = requests.get(url)
      json = resp.json()['data']
      summary = json['summary']
      courier = summary['courier']
      service = summary['service']
      status = summary['status']

      detail = json['detail']
      dari = detail['origin']
      destination = detail['destination']
      shipper = detail['shipper']
      receiver = detail['receiver']

      history = json['history'][0]
      date = history['date']
      desc = history['desc']
      
      print(courier)
      api_bot.sendMessage(id_chat,'Expedisi\nKurir        : '+courier+'\nService  : '+service+'\nStatus    : '+status)
      api_bot.sendMessage(id_chat,'Detail\nDari     > '+dari+'\nTujuan   > '+destination+'\nPengirim > '+shipper+'\nPenerima > '+receiver)
      api_bot.sendMessage(id_chat,'Tracking\nTanggal   : '+date+'\nPosisi       : '+desc)
      
        
    elif '/pos' in command:
      import requests, json
      resi = command[5:]
      print(resi)
      url = "https://api.binderbyte.com/v1/track?api_key=a8b0efaea4329e741aeaca527630d67b05288432b68af71da79a1a7c0085542d&courier=pos&awb="+str(resi)
      resp = requests.get(url)
      json = resp.json()['data']
      summary = json['summary']
      courier = summary['courier']
      service = summary['service']
      status = summary['status']

      detail = json['detail']
      dari = detail['origin']
      destination = detail['destination']
      shipper = detail['shipper']
      receiver = detail['receiver']

      history = json['history'][0]
      date = history['date']
      desc = history['desc']
      
      print(courier)
      api_bot.sendMessage(id_chat,'Expedisi\nKurir        : '+courier+'\nService  : '+service+'\nStatus    : '+status)
      api_bot.sendMessage(id_chat,'Detail\nDari     > '+dari+'\nTujuan   > '+destination+'\nPengirim > '+shipper+'\nPenerima > '+receiver)
      api_bot.sendMessage(id_chat,'Tracking\nTanggal   : '+date+'\nPosisi       : '+desc)
      
        
    elif '/jnt' in command:
      import requests, json
      resi = command[5:]
      print(resi)
      url = "https://api.binderbyte.com/v1/track?api_key=a8b0efaea4329e741aeaca527630d67b05288432b68af71da79a1a7c0085542d&courier=jnt&awb="+str(resi)
      resp = requests.get(url)
      json = resp.json()['data']
      summary = json['summary']
      courier = summary['courier']
      service = summary['service']
      status = summary['status']

      detail = json['detail']
      dari = detail['origin']
      destination = detail['destination']
      shipper = detail['shipper']
      receiver = detail['receiver']

      history = json['history'][0]
      date = history['date']
      desc = history['desc']
      
      print(courier)
      api_bot.sendMessage(id_chat,'Expedisi\nKurir        : '+courier+'\nService  : '+service+'\nStatus    : '+status)
      api_bot.sendMessage(id_chat,'Detail\nDari     > '+dari+'\nTujuan   > '+destination+'\nPengirim > '+shipper+'\nPenerima > '+receiver)
      api_bot.sendMessage(id_chat,'Tracking\nTanggal   : '+date+'\nPosisi       : '+desc)
      
        
    elif '/tiki' in command:
      import requests, json
      resi = command[6:]
      print(resi)
      url = "https://api.binderbyte.com/v1/track?api_key=a8b0efaea4329e741aeaca527630d67b05288432b68af71da79a1a7c0085542d&courier=tiki&awb="+str(resi)
      resp = requests.get(url)
      json = resp.json()['data']
      summary = json['summary']
      courier = summary['courier']
      service = summary['service']
      status = summary['status']

      detail = json['detail']
      dari = detail['origin']
      destination = detail['destination']
      shipper = detail['shipper']
      receiver = detail['receiver']

      history = json['history'][0]
      date = history['date']
      desc = history['desc']
      
      print(courier)
      api_bot.sendMessage(id_chat,'Expedisi\nKurir        : '+courier+'\nService  : '+service+'\nStatus    : '+status)
      api_bot.sendMessage(id_chat,'Detail\nDari     > '+dari+'\nTujuan   > '+destination+'\nPengirim > '+shipper+'\nPenerima > '+receiver)
      api_bot.sendMessage(id_chat,'Tracking\nTanggal   : '+date+'\nPosisi       : '+desc)
      
        
    elif '/anteraja' in command:
      import requests, json
      resi = command[10:]
      print(resi)
      url = "https://api.binderbyte.com/v1/track?api_key=a8b0efaea4329e741aeaca527630d67b05288432b68af71da79a1a7c0085542d&courier=anteraja&awb="+str(resi)
      resp = requests.get(url)
      json = resp.json()['data']
      summary = json['summary']
      courier = summary['courier']
      service = summary['service']
      status = summary['status']

      detail = json['detail']
      dari = detail['origin']
      destination = detail['destination']
      shipper = detail['shipper']
      receiver = detail['receiver']

      history = json['history'][0]
      date = history['date']
      desc = history['desc']
      
      print(courier)
      api_bot.sendMessage(id_chat,'Expedisi\nKurir        : '+courier+'\nService  : '+service+'\nStatus    : '+status)
      api_bot.sendMessage(id_chat,'Detail\nDari     > '+dari+'\nTujuan   > '+destination+'\nPengirim > '+shipper+'\nPenerima > '+receiver)
      api_bot.sendMessage(id_chat,'Tracking\nTanggal   : '+date+'\nPosisi       : '+desc)
      
        
    elif '/wahana' in command:
      import requests, json
      resi = command[8:]
      print(resi)
      url = "https://api.binderbyte.com/v1/track?api_key=a8b0efaea4329e741aeaca527630d67b05288432b68af71da79a1a7c0085542d&courier=wahana&awb="+str(resi)
      resp = requests.get(url)
      json = resp.json()['data']
      summary = json['summary']
      courier = summary['courier']
      service = summary['service']
      status = summary['status']

      detail = json['detail']
      dari = detail['origin']
      destination = detail['destination']
      shipper = detail['shipper']
      receiver = detail['receiver']

      history = json['history'][0]
      date = history['date']
      desc = history['desc']
      
      print(courier)
      api_bot.sendMessage(id_chat,'Expedisi\nKurir        : '+courier+'\nService  : '+service+'\nStatus    : '+status)
      api_bot.sendMessage(id_chat,'Detail\nDari     > '+dari+'\nTujuan   > '+destination+'\nPengirim > '+shipper+'\nPenerima > '+receiver)
      api_bot.sendMessage(id_chat,'Tracking\nTanggal   : '+date+'\nPosisi       : '+desc)
      
        
    elif '/ninja' in command:
      import requests, json
      resi = command[7:]
      print(resi)
      url = "https://api.binderbyte.com/v1/track?api_key=a8b0efaea4329e741aeaca527630d67b05288432b68af71da79a1a7c0085542d&courier=ninja&awb="+str(resi)
      resp = requests.get(url)
      json = resp.json()['data']
      summary = json['summary']
      courier = summary['courier']
      service = summary['service']
      status = summary['status']

      detail = json['detail']
      dari = detail['origin']
      destination = detail['destination']
      shipper = detail['shipper']
      receiver = detail['receiver']

      history = json['history'][0]
      date = history['date']
      desc = history['desc']
      
      print(courier)
      api_bot.sendMessage(id_chat,'Expedisi\nKurir        : '+courier+'\nService  : '+service+'\nStatus    : '+status)
      api_bot.sendMessage(id_chat,'Detail\nDari     > '+dari+'\nTujuan   > '+destination+'\nPengirim > '+shipper+'\nPenerima > '+receiver)
      api_bot.sendMessage(id_chat,'Tracking\nTanggal   : '+date+'\nPosisi       : '+desc)
      
        
    elif '/lion' in command:
      import requests, json
      resi = command[7:]
      print(resi)
      url = "https://api.binderbyte.com/v1/track?api_key=a8b0efaea4329e741aeaca527630d67b05288432b68af71da79a1a7c0085542d&courier=lion&awb="+str(resi)
      resp = requests.get(url)
      json = resp.json()['data']
      summary = json['summary']
      courier = summary['courier']
      service = summary['service']
      status = summary['status']

      detail = json['detail']
      dari = detail['origin']
      destination = detail['destination']
      shipper = detail['shipper']
      receiver = detail['receiver']

      history = json['history'][0]
      date = history['date']
      desc = history['desc']
      
      print(courier)
      api_bot.sendMessage(id_chat,'Expedisi\nKurir        : '+courier+'\nService  : '+service+'\nStatus    : '+status)
      api_bot.sendMessage(id_chat,'Detail\nDari     > '+dari+'\nTujuan   > '+destination+'\nPengirim > '+shipper+'\nPenerima > '+receiver)
      api_bot.sendMessage(id_chat,'Tracking\nTanggal   : '+date+'\nPosisi       : '+desc)
      
        
    elif '/shopee express' in command:
      import requests, json
      resi = command[15:]
      print(resi)
      url = "https://api.binderbyte.com/v1/track?api_key=a8b0efaea4329e741aeaca527630d67b05288432b68af71da79a1a7c0085542d&courier=spx&awb="+str(resi)
      resp = requests.get(url)
      json = resp.json()['data']
      summary = json['summary']
      courier = summary['courier']
      service = summary['service']
      status = summary['status']

      detail = json['detail']
      dari = detail['origin']
      destination = detail['destination']
      shipper = detail['shipper']
      receiver = detail['receiver']

      history = json['history'][0]
      date = history['date']
      desc = history['desc']
      
      print(courier)
      api_bot.sendMessage(id_chat,'Expedisi\nKurir        : '+courier+'\nService  : '+service+'\nStatus    : '+status)
      api_bot.sendMessage(id_chat,'Detail\nDari     > '+dari+'\nTujuan   > '+destination+'\nPengirim > '+shipper+'\nPenerima > '+receiver)
      api_bot.sendMessage(id_chat,'Tracking\nTanggal   : '+date+'\nPosisi       : '+desc)
      
      
      
      
      

api_bot = telepot.Bot('Api Telegram Anda')
MessageLoop(api_bot, head).run_as_thread()
print('Running..')

while 1:
    time.sleep(10)
