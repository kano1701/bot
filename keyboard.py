from telebot import types

def inline_keyboard(text, data):
    keyboard = types.InlineKeyboardMarkup()
    for line in range(len(text)):
        buttons = []
        for key in range(len(text[line])):
            buttons.append(types.InlineKeyboardButton(text=text[line][key], callback_data=data[line][key]))
        keyboard.row(*buttons)
    return keyboard

def reply_keyboard(text):
    print('reply_keyboard')
    keyboard = types.ReplyKeyboardMarkup()
    for line in range(len(text)):
        buttons = []
        for key in range(len(text[line])):
            buttons.append(text[line][key])
        keyboard.row(*buttons)
    return keyboard