from verification import *
from keyboard import *
from sendMessage import MessageWrapper
from jinja2 import Template
from calendarRender import calendarRender
from datetime import datetime
from exampleList import exampleList
from listRender import listRender
from qrcode_scaner import qrcode_scan

info = ['Информация', 'Information']
calendar = ['Календарь', 'Calendar']
sample_list = ['Список', 'List']
scaner = ["Сканирование QRcode", "Scaning QRcode"]
lang = ['Сменить язык', 'Change language']

nameMonth = {
        'ru': ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь',
               'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь'],
        'en': ['January', 'February', 'March', 'April', 'May', 'June',
               'July', 'August', 'September', 'October', 'November', 'December']
    }


class manager():

    output = {'text': [], 'keyboard': None, 'edit': False, 'photo': None}
    result = {}

    def __init__(self, dataIn):
        self.dataIn = dataIn

    def manager(self):
        print(self.dataIn)

        self.output['text'] = []
        self.output['keyboard'] = None
        self.output['edit'] = False
        self.output['photo'] = None

        if self.dataIn["type"] == "text":

            userInfo = checkUser(self.dataIn["id"])


            if self.dataIn['text'] == "/start":
                text = Template(open('localization/' + userInfo[0] + '/welcome', encoding='utf8').read())
                self.output['text'].append(text.render())
                text = [
                            ['Информация', 'Календарь', 'Список'],
                            ['Сканирование QRcode', 'Смена языка']
                         ]
                self.output['keyboard'] = reply_keyboard(text)

            elif self.dataIn['text'] in set(info):
                text = Template(open('localization/' + userInfo[0] + '/info', encoding='utf8').read())
                self.output['text'].append(text.render())

            elif self.dataIn['text'] in set(calendar):
                print("elif self.dataIn['text'] in set(calendar)")
                now = datetime.now()
                text = Template(open('localization/' + userInfo[0] + '/setDate', encoding='utf8').read())
                self.output['text'].append(text.render(month=nameMonth[userInfo[0]][now.month-1], year=now.year))
                self.output['keyboard'] = calendarRender(userInfo[0], now.year, now.month)
                query.updateItem({'year': now.year, 'month': now.month}, str(self.dataIn['id']))

            elif self.dataIn['text'] == 'cbb':
                userDate = query.selectItem('year, month', self.dataIn['id'])
                year = userDate[0]
                month = userDate[1]
                if month == 1:
                    year = year - 1
                    month = 12
                else:
                    month -= 1
                text = Template(open('localization/' + userInfo[0] + '/setDate', encoding='utf8').read())
                self.output['text'].append(text.render(month=nameMonth[userInfo[0]][month-1], year=year))
                self.output['edit'] = True
                self.output['keyboard'] = calendarRender(userInfo[0], year, month)
                query.updateItem({'year': year, 'month': month}, str(self.dataIn['id']))

            elif self.dataIn['text'] == 'cbn':
                userDate = query.selectItem('year, month', self.dataIn['id'])
                year = userDate[0]
                month = userDate[1]
                if month == 12:
                    year = year + 1
                    month = 1
                else:
                    month +=1
                text = Template(open('localization/' + userInfo[0] + '/setDate', encoding='utf8').read())
                self.output['text'].append(text.render(month=nameMonth[userInfo[0]][month-1], year=year))
                self.output['edit'] = True
                self.output['keyboard'] = calendarRender(userInfo[0], year, month)
                query.updateItem({'year': year, 'month': month}, str(self.dataIn['id']))

            elif self.dataIn['text'] in set(str(x) for x in range(1,32)):
                print("elif self.dataIn['text'] in set(x for x in range(1,32))")
                userDate = query.selectItem('year, month', self.dataIn['id'])
                text = Template(open('localization/' + userInfo[0] + '/yourDate', encoding='utf8').read())
                self.output['text'].append(text.render(day=self.dataIn['text'], month=userDate[1], year=userDate[0]))

            elif self.dataIn['text'] in set(sample_list):
                offset = query.selectItem('offset', self.dataIn['id'])
                print(offset[0])
                text = Template(open('localization/' + userInfo[0] + '/list', encoding='utf8').read())
                self.output['text'].append(text.render(country_list=exampleList[offset[0]:offset[0]+5]))
                self.output['keyboard'] = listRender(offset, exampleList[offset[0]:offset[0]+5])

            elif self.dataIn['text'] == 'button_back':
                offset = query.selectItem('offset', self.dataIn['id'])
                offset = offset[0] - 5
                query.updateItem({'offset': offset}, str(self.dataIn['id']))
                text = Template(open('localization/' + userInfo[0] + '/list', encoding='utf8').read())
                self.output['text'].append(text.render(country_list=exampleList[offset:offset + 5]))
                self.output['keyboard'] = listRender(offset, exampleList[offset:offset + 5])
                self.output['edit'] = True

            elif self.dataIn['text'] == 'button_next':
                offset = query.selectItem('offset', self.dataIn['id'])
                offset = offset[0] + 5
                query.updateItem({'offset': offset}, str(self.dataIn['id']))
                text = Template(open('localization/' + userInfo[0] + '/list', encoding='utf8').read())
                self.output['text'].append(text.render(country_list=exampleList[offset:offset + 5]))
                self.output['keyboard'] = listRender(offset, exampleList[offset:offset + 5])
                self.output['edit'] = True

            elif self.dataIn['text'] in set(scaner):
                self.output['text'].append(open('localization/' + userInfo[0] + '/scanning', encoding='utf8').read())

        elif self.dataIn["type"] == "photo" or "document":
            text = Template(qrcode_scan(self.dataIn['text']))
            self.output['text'].append(text.render())


        newMessage = MessageWrapper(self.dataIn['id'], self.output, self.dataIn['messageId'])
        newMessage.distribution()
