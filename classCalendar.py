import locale
import calendar


class telegram_calendar():

    text_navi = ['⬅', '➡']
    data_navi = ['button_back', 'button_next']


    def __init__(self, user_id, input_text):
        self.user_id = user_id
        self.input_text = input_text
        self.result = {'text': [], 'data': []}

    def check_in_month(self, day, month, year):
        obj_month = calendar.monthrange(year, month)
        day_list = [i for i in range(obj_month[1])]
        return day in set(day_list)

    def send_calendar(self, language, year, month):
        print('class telegram_calendar | def send_calendar')

        if language == 'ru':
            locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')

        local_month = calendar.Calendar(0)
        days = local_month.monthdayscalendar(year, month)
        days_text = []
        days_date = []

        for x in range(len(days)):
            text = []
            date = []
            for y in range(7):
                if days[x][y] == 0:
                    text.append(' ')
                    date.append('ignore')
                else:
                    text.append(str(days[x][y]))
                    date.append(str(days[x][y]))
            days_text.append(text)
            days_date.append(date)

        print("days text\n", days_text)
        print("days data\n", days_date)

        self.result['text'] = [['<', calendar.month_name[month]+' '+str(year), '>']]
        self.result['data'] = [['button_back', 'ignore', 'button_next']]

        for loop in range(len(days)):
            self.result['text'].append(days_text[loop])
            self.result['data'].append(days_date[loop])

        print("days text\n", self.result['text'])
        print("days data\n",self.result['data'])
        return self.result