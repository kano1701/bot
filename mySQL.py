import pymysql


class mySQL():

    __host = 'localhost'
    __user = 'root'
    __password = ''
    __database = 'forBot'

    def connectToDB(self, text, type):
        print(text)
        connect = pymysql.connect(host=self.__host, user=self.__user, password=self.__password,
                                  database=self.__database, charset="utf8")
        sql = connect.cursor()
        sql.execute(text)
        if type == 'select':
            return sql.fetchall()
        elif type == 'update' or type == 'insert':
            connect.commit()

    def selectItem(self, item, tg):
        sql = "select {} from user where telegram_id = {}"
        result = self.connectToDB(sql.format(item, tg), 'select')
        try:
            result[0][0]
            if item == '*':
                return True
            elif item != '*':
                return result[0]
        except:
            return False

    def updateItem(self, update, tg):
        string = 'update user set '
        length = len(update)
        i = 1
        for value in update:
            string = string + value + ' = ' + str(update[value])
            if i < length:
                string = string + ', '
                i += 1

        sql = string + ' where telegram_id = ' + tg
        self.connectToDB(sql, 'update')

    def insert(self, columns, values):
        sql = 'insert into user ({}) values ({})'
        self.connectToDB(sql.format(columns, values), 'insert')

query = mySQL()
