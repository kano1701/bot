from botConfig import bot
from telebot import types

class telegram():

    def send_message(self, chat_id, text_of_message=None, keyboard=None, photo=None):
        if text_of_message==None:
            return
        if keyboard==None:
            print(1)
            bot.send_message(chat_id=chat_id, text=text_of_message)
        elif keyboard:
            bot.send_message(chat_id=chat_id, text=text_of_message, reply_markup=keyboard)
        if photo:
            print(5)
            bot.send_photo(chat_id=chat_id, photo=photo)

    def edit_message(self, chat_id, message_id, text_of_message=None, type=None, keyboard=None, photo=None):
        print("class telegram | def edit message",
              "\nmessage_id", message_id, "\ntext of message", text_of_message,
              "\ntype", type, "\nkeyboard", keyboard)
        if text_of_message==None:
            return
        if keyboard==None:
            print("not keybord")
            bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text_of_message)
        elif keyboard!=None:
            print("keyboard")
            bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text_of_message, reply_markup=keyboard)
        if photo:
            bot.send_photo(chat_id=id, photo=photo)

    def inline_keyboard(self, amount_line, text_key, data_key):
        print("\nclass telegram | def inline_keyboard")
        print("text_key\n", text_key)
        print("data_key\n", data_key)
        print("amount line", amount_line)

        keyboard = types.InlineKeyboardMarkup()
        for line in range(amount_line):
            buttons = []
            print("line", line)
            print("amount button", len(text_key[line]))
            for key in range(len(text_key[line])):
                print("text button", text_key[line][key])
                print("text button", type(text_key[line][key]))
                buttons.append(types.InlineKeyboardButton(text=text_key[line][key], callback_data=data_key[line][key]))
                print("list button", buttons)
            keyboard.row(*buttons)
        return keyboard

    def reply_keyboard(self, amount_line, text_key):
        keyboard = types.ReplyKeyboardMarkup()
        for line in range(len(amount_line)):
            buttons = []
            for key in range(len(text_key[line])):
                buttons.append(text_key[line][key])
            keyboard.row(*buttons)
        return keyboard

telegram = telegram()