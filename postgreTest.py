from VB.ViBranium import ConnectDB



cursor = ConnectDB("PostgreSQl", "test", "postgres", "root", "127.0.0.1", 5432)

cursor.create("table3", ['name', 'login'], ['BIGINT', 'TEXT'])

print(cursor.select(1, "all", "*", "table3"))

cursor.insert("table3", "name, login", "123, 'test'")
cursor.insert("table3", "name, login", "321, 'test2'")

print(cursor.select(1, "all", "*", "table3"))

cursor.update("table3", "name", "321", "name", "=", "123")

print(cursor.select(1, "all", "*", "table3"))

cursor.delete("table3", "name", "!=", "1")

print(cursor.select(1, "all", "*", "table3"))