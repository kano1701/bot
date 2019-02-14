from botConfig import bot


class MessageWrapper:

    def __init__(self, user, output, messageId):
        self.user = user
        self.output = output
        self.messageId = messageId

    def distribution(self):

        print('MessageWrapper | distribution')

        if self.output['edit'] is False:
            self.send_message()
        elif self.output['edit'] is True:
            self.edit_message()

    def send_message(self):

        for send in range(len(self.output['text'])):

            if self.output['keyboard'] is None:
                bot.send_message(self.user, self.output['text'][send])

            elif self.output['keyboard'] is not None:
                bot.send_message(self.user, self.output['text'][send], reply_markup=self.output['keyboard'])

            if self.output['photo'] is not None:
                bot.send_photo(self.user, photo=self.output['photo'])

    def edit_message(self):

        print('MessageWrapper | edit_message')
        print(self.user, self.messageId, self.output['text'])

        if self.output['keyboard'] is None:
            bot.edit_message_text(self.user, self.messageId, self.output['text'])

        elif self.output['keyboard'] is not None:
            # print(self.output['text'])
            bot.edit_message_text(chat_id=self.user, message_id=self.messageId, text=self.output['text'][0], reply_markup=self.output['keyboard'])
            # bot.edit_message_reply_markup(chat_id=self.user, message_id=self.messageId,
            #                               inline_message_id=None, reply_markup=self.output['keyboard'])
            # bot.edit_message_reply_markup(
            #     chat_id=self.user, message_id=self.messageId,
            #     reply_markup=self.output['keyboard']
            # )

        if self.output['photo'] is not None:
            bot.send_photo(self.user, photo=self.output['photo'])
