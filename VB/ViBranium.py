__package__ = __name__
__all__ = [
    "Helper", "Logger", "Encrypt",
    "CreateTable", "ConnectDB"
    ]
__version__ = "1.0.1"
__author__ = "M_O_D_E_R"
__doc__ = """------------------------------------------------------------------------
    ORM for working with Postgresql and SQlite 3

    write ViBranium.py help in console to get more information
------------------------------------------------------------------------"""


import psycopg2
import sqlite3
import logging
import hashlib
import random
import math
import sys
import os

#from BeautifulOutput import beauti


FILE_PATH = os.path.abspath(__file__)
BASE_PATH = "\\".join(FILE_PATH.replace("\\", "/").split("/")[0 : -1])





#def do_beauti(self, datas, columns):
#    return beauti.Beautiful(datas, columns)

"""
class Meta(type):
    def __new__(cls_, name, parents, attr):

        attr.update(
            {
                "beauti" : do_beauti
            }
        )

        return type(name, parents, attr)
"""



class Helper:
    """
        ViBranium(V&B) ORM

        ********&******

        ___               ___      ___________
        \  \             /  /     |  ______   \ 
         \  \           /  /      | |      \   \ 
          \  \         /  /       | |       |  |
           \  \       /  /        | |______/  /
            \  \     /  /         |  ______  |
             \  \   /  /          | |      \  \ 
              \  \_/  /           | |      |   |
               \     /            | |______/   /
                \___/             |___________/



    ----------------------------------------------------------------------------------

        params for file:
            help              - show all comands and class which have this lib
            createtable       - create new table if table is not exixsts, for this operation use class CreateTable
                more information about CreateTable you can find in this class  ->  print(CreateTable.__doc__)

                Example(this command create table users with two columns name: int and login: str):
                    main.py createtable_users_(name_BIGINT,login_TEXT)
                    
                    main.py createtable_{table name}_{(columns name columns type, columns name columns type, ...)}

                    table name -> it's name of table
                    columns name -> name of column don't repeat this name for each columns
                    columns type -> type of column must be followed by Postgresql types columns

                    more examples in CreateTable.__doc__



        All class for working with databases:
            Encrypt:
                this class can help with encode and decode data before writing in db

            CreateTable:
                for creating new tables

            ConnectDB:
                main class, which contain some helpfull methods such as: (select, delete, insert, update)

    ----------------------------------------------------------------------------------
    """
    def __init__(self): pass



class Logger:
    """
        class for work with logging which contain all function from module logging

        log_level   -> set logging level
        log_path    -> set path to log-file, if log_path is not indicated log-filr will be created near __main__


        Example:
            logger = Logger("info", "")
            logger.logger.info("Hello world")
    """
    def __init__(self, log_level, log_path):
        self.log_level = log_level
        self.log_path = log_path

        self.logger = logging.getLogger()
        self.logger.setLevel(self.set_level())

        self.fh = logging.FileHandler(self.log_path + "/data.log")
        self.formatter = self.set_formatter("[%(asctime)s]:[%(process)d-%(levelname)s]:[%(name)s]:[%(message)s]")

        self.fh.setFormatter(self.formatter)
        self.logger.addHandler(self.fh)
    
    def set_formatter(self, str_formatter):
        return logging.Formatter(str_formatter)

    
    def set_level(self):
        if self.log_level == "info":
            return logging.INFO
        elif self.log_level == "debug":
            return logging.DEBUG
        elif self.log_level == "warning":
            return logging.WARNING
        elif self.log_level == "error":
            return logging.ERROR
        elif self.log_level == "critical":
            return logging.CRITICAL
        else:
            raise LogLevelError(f"Не верный уровень логирования ->  {self.log_level}")



class NotFoundMode(Exception):
    def __init__(self, info):
        self.info = info


class SysArgError(Exception):
    def __init__(self, info_error):
        self.info_error = info_error
        print("Output info >>>", self.info_error)


class LogLevelError(Exception):
    def __init__(self, info_error):
        self.info_error = info_error





class Encrypt:
    """
        Here you can use hash-function for encrypt some data and then put data in database.


        Also class contain method for cheking some data with some hash,
        method return True if some hash == hash some data,
        False will be returned if some hash != hash some data.
        
        Example:
            >>> print(Encrypt.is_true("Hello world", b'>%\x96\ny\xdb\xc6\x9bgL\xd4\xecg\xa7,b'))
            >>> True

            >>> print(Encrypt.hash("Hello world"))
            >>> b'>%\x96\ny\xdb\xc6\x9bgL\xd4\xecg\xa7,b'


        Methods for encode and decode some informations:
            def encode(self) -> str: ...
            def decode(self) -> str: ...
    """
    def __init__(self): pass

    def turn_(self, string, num_of_turn         ):
        all_chars = "abcdefghijklmnopqrstuvwxyz 123456789!@#$%^&*()_+}{[]:;'|/,.<>?"
        string = str(string).lower()
        output_num_lst = []
        lst = []
        lenght = (len((all_chars) * 2) - 1)


        if num_of_turn > 123:
            new_range = num_of_turn // lenght
            
            formula = 0
            for i in range(new_range):
                formula += lenght
            
            new_encode_int = num_of_turn - formula

            for i in string:
                output_num_lst.append(all_chars.index((i)))

            for i in output_num_lst:
                if i + new_encode_int <= (len(all_chars) - 1):
                    lst.append(all_chars[i + new_encode_int])
                else:
                    new_num = i + new_encode_int - (len(all_chars) - 1) - 1

                    lst.append(all_chars[new_num])

            return "".join(lst)
        else:            
            for i in string:
                output_num_lst.append(all_chars.index((i)))

            for i in output_num_lst:
                if i + num_of_turn <= (len(all_chars) - 1):
                    lst.append(all_chars[i + num_of_turn])
                else:
                    new_num = i + num_of_turn - (len(all_chars) - 1) - 1

                    lst.append(all_chars[new_num])
            
            return "".join(lst)

    def encode(self, input_string, key):
        key = key.lower()
        input_string_copy = input_string
        chars = {
            'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5, 'f' : 6, 'g' : 7, 'h' : 8,
            'i' : 9, 'j' : 10, 'k' : 11, 'l' : 12, 'm' : 13, 'n' : 14, 'o' : 15, 'p' : 16,
            'q' : 17, 'r' : 18, 's' : 19, 't' : 20, 'u' : 21, 'v' : 22, 'w' : 23, 'x' : 24, 'y' : 25, 'z' : 26,
            ' ' : 27
        }
        all_chars = "abcdefghijklmnopqrstuvwxyz 123456789!@#$%^&*()_+}{[]:;'|/,.<>?"
        new_key = 0

        for i in key:
            new_key += chars.get(i)

        new_list = []

        input_string = list(input_string.lower())

        for i in input_string:
            new_list.append(chars.get(i))

        lenght = (len((all_chars) * 2) - 1)
        new_range = new_key // lenght    
        formula = 0
        for i in range(new_range):
            formula += lenght
        
        new_encode_int = new_key - formula

        returns_data = self.turn_(input_string_copy, new_key)
        return [
            returns_data, new_encode_int,
            [
                self.hash(returns_data),
                self.hash(new_key)
            ]
        ]
    
    def decode(self, some_string, key):
        new_range = key // 123

        formula = 0
        for i in range(new_range):
            formula += 123


        new_encode_int = key - formula
        
        return self.turn_(some_string, -new_encode_int)
    
    def crypto(self, string, key):
        import math

        string = string.lower()
        chars = "abcdefghijklmnopqrstuvwxyz 123456789!@#$%^&*()_+}{[]:;'|/,.<>?"

        encrypt = Encrypt()
        new_string = encrypt.encode(string, key)

        mas = []
        for i in new_string[0]:
            crypt = round((((math.pi*(chars.index(i) ** 2 % new_string[1])) + ((25 / math.pi) * (math.e ** 2)) + ((math.e ** math.pi) + (math.pi ** math.e)))) / (math.pi ** 2) * (math.e ** 2))
            mas.append(chr(crypt))

        return "".join(mas)

    #@staticmethod
    def hash(self, str_data: str):
        str_data = str(str_data)
        var = hashlib.md5()
        var.update(str_data.encode("utf-8"))
        return var.digest()

    #@staticmethod
    def is_true(self, try_data, hash_):
        data_ = hashlib.md5()
        data_.update(try_data.encode("utf-8"))
        
        if data_.digest() == hash_:
            return True
        else:
            return False

    def reverse_func(self, lst):
        for i in lst:
            lst = [i] + lst
        
        lst = lst[0 : len(lst) // 2]

        return lst

    def translate__from_2__to_10(self, num):
        result = 0
        num = str(num)

        kw = [i for i in range(len(num))]
        kw = self.reverse_func(kw)

        for i in range(len(num)):
            result += (int(num[i]) * (2 ** kw[i]))

        return result








class CreateTable:
    """
        it's SQL-request, and you need follow all SQL-rules 

            CREATE TABLE IF NOT EXISTS {table_name} {str_request}

            CreateTable("users", ['name', 'login'], ['BIGINT', 'TEXT'])
    """
    def __init__(self, table_name: str, columns_name: list, columns_type, cursor = None, db = None, DB = None):
        """
            age INT,
            name TEXT
        """
        self.DB = DB
        self.output_datas = []

        for elem, name in enumerate(columns_name):
            self.output_datas.append(f"{name} {columns_type[elem]}")

        self.sql_request = """
            CREATE TABLE IF NOT EXISTS {} ({})
            """.format(table_name, ", ".join(self.output_datas))

        if ((self.DB == "PostgreSQl") or (self.DB == "SQlite3")):
            cursor.execute(self.sql_request)
            db.commit()


class ConnectDB:
    """

    """
    def __init__(self, DB = " ", dbname =  " ", user = " ", password = " ", host = " ", port = 0):
        self.DB = DB
        if self.DB == "PostgreSQl":
            self.dbname = dbname

            self.db = psycopg2.connect(
                dbname = self.dbname,
                user = user, 
                password = password,
                host = host,
                port = port    
            )
            self.cursor = self.db.cursor()
        elif self.DB == "SQlite3":
            self.dbname = dbname

            self.db = sqlite3.connect(self.dbname)
            self.cursor = self.db.cursor()
    
    def use_json(self):
        import json

        with open(f"{BASE_PATH}\\settings.json", "r") as JsonFileRead:
            self.accept_data = json.load(JsonFileRead)

        self.DB = self.accept_data["ConnectDB"]["DB"]
        self.dbname = self.accept_data["ConnectDB"]["dbname"]
        self.user = self.accept_data["ConnectDB"]["user"]
        self.password = self.accept_data["ConnectDB"]["password"]
        self.host = self.accept_data["ConnectDB"]["host"]
        self.port = self.accept_data["ConnectDB"]["port"]

        if self.DB == "PostgreSQl":
            self.db = psycopg2.connect(
                dbname = self.dbname,
                user = self.user, 
                password = self.password,
                host = self.host,
                port = self.port
            )
            self.cursor = self.db.cursor()
        elif self.DB == "SQlite3":
            self.db = sqlite3.connect(self.dbname)
            self.cursor = self.db.cursor()


    def create(self, table_name: str, columns_name: list, columns_type: list):
        if self.DB == "PostgreSQl":
            CreateTable(table_name, columns_name, columns_type, self.cursor, self.db, self.DB)
        elif self.DB == "SQlite3":
            CreateTable(table_name, columns_name, columns_type, self.cursor, self.db, self.DB)

    def select(self, mode = 1, fetch = 'one', search_data = '*', table_name = None, each_column = None, char = '=', by_ = None):
        """
            for selecting some information from databases:
                have 2 mode such as (
                    1) SELECT {} FROM {}
                    2) SELECT {} FROM {} WHERE {} {} {}
                )

            SELECT {*} FROM {table} WHERE {user} {=} {123}


            Example:

                .select(mode = 1, fetch = "one", search_data = '*', table_name = 'users')
                .select(mode = 1, fetch = "all", search_data = '*', table_name = 'users')
                .select(1, "all", '*', 'users')

                .select(mode = 2, fetch = "one", search_data = '*', table_name = 'users', each_column = 'id', char = '!=', by_ = '7')
                .select(2, "one", '*', 'users', 'id', '!=', '7')
        """
        if ((self.DB == "PostgreSQl") or (self.DB == "SQlite3")):
            if mode == 1:
                if fetch == "one":
                    self.cursor.execute(f"SELECT {search_data} FROM {table_name}")
                    return self.cursor.fetchone()
                elif fetch == "all":
                    self.cursor.execute(f"SELECT {search_data} FROM {table_name}")
                    return self.cursor.fetchall()
                else:
                    raise NotFoundMode(f"arg fetch have some mistakes: fetch must be 'one' or 'all' not {fetch}")

            elif mode == 2:
                if fetch == "one":
                    self.cursor.execute(f"SELECT {search_data} FROM {table_name} WHERE {each_column} {char} {by_}")
                    return self.cursor.fetchone()
                elif fetch == "all":
                    self.cursor.execute(f"SELECT {search_data} FROM {table_name} WHERE {each_column} {char} {by_}")
                    return self.cursor.fetchall()
                else:
                    raise NotFoundMode(f"arg fetch have some mistakes: fetch must be 'one' or 'all' not {fetch}")
            else:
                raise NotFoundMode(f"arg mode have some mistakes: mode must be 1: int or 2: int not {mode}")

    def delete(self, table_name, each_column = None, char = '=', by_ = None):
        if ((self.DB == "PostgreSQl") or (self.DB == "SQlite3")):
            self.delete_request = """DELETE FROM {} WHERE {} {} {}""".format(
                table_name, each_column,
                char, by_
                )
            self.cursor.execute(self.delete_request)
            self.db.commit()


    def update(self, table_name, column_name, value, each_column = None, char = '=', by_ = None):
        if self.DB == "PostgreSQl":
            self.update_request = """UPDATE {} SET {} = {} WHERE {} {} {}""".format(
                table_name, column_name, value,
                each_column, char, by_
                )
            self.cursor.execute(self.update_request)
            self.db.commit()
        elif self.DB == "SQlite3":
            self.update_request = """UPDATE {} SET {} = {} WHERE {} {} {}""".format(
                table_name, column_name, value,
                each_column, char, by_
                )
            self.cursor.execute(self.update_request)
            self.db.commit()


    def insert(self, table_name: str, columns_name: str, columns_datas):
        if self.DB == "PostgreSQl":
            self.cursor.execute("""INSERT INTO {} (
                {}
            ) VALUES ({})""".format(table_name, columns_name, columns_datas))
            self.db.commit()

        elif self.DB == "SQlite3":
            dich = "?," * len(columns_datas.split(","))
            dich = dich[0 : len(dich) -1]

            self.cursor.execute("""INSERT INTO {} VALUES({})""".format(
                    table_name,
                    dich
                    ),
                    columns_datas.replace(" ", "").split(",")
            )
            self.db.commit()


sys_args = sys.argv
del sys_args[0]


if "help" in sys_args:
    print(Helper.__doc__)
elif "settings" in sys_args:
    import json

    if sys_args[1] == "set":
        print("\tConnectDB: ")
        i_DB = input("DB >>> ")
        i_dbname = input("dbname >>> ")
        i_user = input("user >>> ")
        i_password = input("password >>> ")
        i_host = input("host >>> ")
        try:
            i_port = int(input("port >>> "))
        except:
            print("You need to enter integer ")
        
        print("\tLogger: ")
        i_level = input("Level of logging >>> ")
        i_path = input("Path to log-file >>> ")


        with open("settings.json", "r") as file_R:
            data = json.load(file_R)
            data.update(
                {
                    "ConnectDB": {
                        "DB" : i_DB,
                        "dbname" : i_dbname,
                        "user" : i_user,
                        "password" : i_password,
                        "host" : i_host,
                        "port" : i_port
                    },
                    "CreateTable" : {},
                    "Logger" : {
                        "level" : i_level,
                        "path" : i_path
                    }
                }
            )

            with open(f"{BASE_PATH}\\settings.json", "w") as file_W:
                file_W.write(json.dumps(data, indent = 4))

                del file_R
                del file_W

    elif sys_args[1] == "show":
        with open(f"{BASE_PATH}\\settings.json", "r") as file_R:
            print(json.load(file_R))
            del file_R

elif "sqlite3" in sys_args:
    if sys_args[1] == "createdb":
        crtdb = sqlite3.connect(sys_args[2])

        del crtdb
elif "postgresql" in sys_args:
    pass
else:
    for i in sys_args:
        if "createtable" in i:
            i = i.replace("createtable", "")
            i = i.split("_(")
            i = (i[0].replace("_", ""), i[1].replace(")", ""))
            i = (i[0], i[1].split(","))

            break
        else:
            raise SysArgError(f"Not found arg -> {i}")

