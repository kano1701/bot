from botConfig import bot
from datetime import datetime
from manager import manager

dataIn = {"id": "", "type": "", "text": "", "messageId": ""}

@bot.message_handler(content_types=['text'])
def bot_send_message(message):
    print('____________________________')
    dataIn["id"] = message.from_user.id
    dataIn["type"] = "text"
    dataIn["text"] = message.text
    new = manager(dataIn)
    new.manager()

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    print('____________________________')
    dataIn["id"] = call.from_user.id
    dataIn["type"] = "text"
    dataIn["text"] = call.data
    dataIn['messageId'] = call.message.message_id
    new = manager(dataIn)
    new.manager()

@bot.message_handler(content_types=['photo'])
def bot_send_message(message):
    print('____________________________')
    file_info = bot.get_file(message.photo[0].file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    src = 'img/' + str(message.from_user.id) + '.jpg'
    with open(src, 'wb') as new_file:
        new_file.write(downloaded_file)
    dataIn["id"] = message.from_user.id
    dataIn["type"] = "image"
    dataIn["text"] = src
    new = manager(dataIn)
    new.manager()

@bot.message_handler(content_types=['document'])
def bot_send_message(message):
    print('____________________________')
    file_info = bot.get_file(message.document.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    src = 'doc/' + message.document.file_name;
    with open(src, 'wb') as new_file:
        new_file.write(downloaded_file)
    dataIn["id"] = message.from_user.id
    dataIn["type"] = "document"
    dataIn["text"] = src
    new = manager(dataIn)
    new.manager()

bot.polling()
