import calendar
from keyboard import *


def calendarRender(lang, year, month):

    local_month = calendar.Calendar(0)
    days = local_month.monthdayscalendar(year, month)
    text = []
    data = []

    for week in days:
        localText = []
        localData = []
        for day in week:
            if day == 0:
                localText.append(' ')
                localData.append('ignore')
            else:
                localText.append(day)
                localData.append(day)
        text.append(localText)
        data.append(localData)

    text.append(['⬅', '➡'])
    data.append(['cbb', 'cbn'])

    return inline_keyboard(text, data)

# calendarRender('ru', 2019, 2)