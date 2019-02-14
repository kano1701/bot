from mySQL import query


def checkUser(id):

    if query.selectItem('*', id) is False:
        createUser(id)

    return query.selectItem('lang, status', id)


def createUser(id):

    try:
        query.insert('telegram_id', id)
    except:
        return False
