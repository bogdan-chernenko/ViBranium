__package__ = __name__
__all__ = [
    "Helper", "Logger", "ConnectDB"
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

class DataBaseError(Exception):
    def __init__(self, non_exist_db):
        print("Data base is not exists: ", non_exist_db)


class ConnectDB:
    """

    """
    def __init__(self, DB = " ", dbname =  " ", user = " ", password = " ", host = " ", port = 0):
        self.DB = DB
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port

        self.DB_exist = False

        self.connect()

    def connect(self):
        if self.DB == "PostgreSQl":
            self.db = psycopg2.connect(
                dbname = self.dbname,
                user = self.user, 
                password = self.password,
                host = self.host,
                port = self.port    
            )
            self.cursor = self.db.cursor()
            self.DB_exist = True
        elif self.DB == "SQlite3":
            self.dbname = self.dbname

            self.db = sqlite3.connect(self.dbname)
            self.cursor = self.db.cursor()
            self.DB_exist = True
        else:
            raise DataBaseError(self.DB)

    def close(self):
        self.cursor.close()

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
        self.output_datas = []

        for elem, name in enumerate(columns_name):
            self.output_datas.append(f"{name} {columns_type[elem]}")

        self.sql_request = """
            CREATE TABLE IF NOT EXISTS {} ({})
            """.format(table_name, ", ".join(self.output_datas))

        if self.DB_exist:
            self.cursor.execute(self.sql_request)
            self.db.commit()

    def select(
            self, fetch = 'one', search_data = '*', table_name = "",
            each_column = None, char = '=', by_ = None
        ):
        if self.DB_exist:
            if each_column is None:
                self.cursor.execute(f"SELECT {search_data} FROM {table_name}")
                if fetch == "one":
                    return self.cursor.fetchone()
                elif fetch == "all":
                    return self.cursor.fetchall()
            else:
                self.cursor.execute(f"SELECT {search_data} FROM {table_name} WHERE {each_column} {char} {by_}")
                if fetch == "one":
                    return self.cursor.fetchone()
                elif fetch == "all":
                    return self.cursor.fetchall()

    def delete(self, table_name, each_column = None, char = '=', by_ = None):
        if self.DB_exist:
            self.delete_request = """DELETE FROM {} WHERE {} {} {}""".format(
                table_name, each_column,
                char, by_
                )
            self.cursor.execute(self.delete_request)
            self.db.commit()

    def update(self, table_name, column_name, value, each_column = None, char = '=', by_ = None):
        if self.DB_exist:
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