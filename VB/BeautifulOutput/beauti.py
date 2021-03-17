

class Beautiful:
    def __init__(self, datas, columns):
        self.datas = datas
        self.columns = columns

        self.str_datas = ""
        self.new_str_datas = ""
        self.len_rows = []
        self.len_of_row = []

    def show(self):
        for i in self.datas:
            self.str_datas += str(i)

        self.str_datas = self.str_datas.replace("][", "\n")
        self.str_datas = self.str_datas.replace("[", "")
        self.str_datas = self.str_datas.replace("]", "")

        self.str_datas = self.str_datas.replace(")(", "\n")
        self.str_datas = self.str_datas.replace("(", "")
        self.str_datas = self.str_datas.replace(")", "")

        self.str_datas = self.str_datas.replace(",", " | ")


        for i in self.str_datas.split("\n"):
            self.new_str_datas += (
                "|" + i.replace(" ", "") + "|\n"# +
#                ("+" + "-" * (len(self.str_datas.split("\n")[0])) + "+") + "\n"
            )

#        self.new_str_datas = "{}\n".format(
 #           "+" + "-" * (len(self.new_str_datas.split("\n")[0])  - 2) + "+"
  #      ) + self.new_str_datas


        for i in self.new_str_datas.split("\n"):
            self.len_rows.append(len(i))
        del self.len_rows[-1]

       # print(self.len_rows)

        ddd = self.new_str_datas.split("\n")
        del ddd[-1]
        for i in ddd:
            lst = []
            for elem in i.split("|"):
                lst.append(len(elem))
            del lst[0]
            del lst[-1]
            self.len_of_row.append(lst)
            lst = []

        del self.len_of_row[-1]

      #  print(self.len_of_row)


        testtt = ""


        for i in range(len(self.len_rows) - 1):
            for e in self.new_str_datas.split("|"):
                if len(e) > 7:
                    testtt += e
                else:
                    testtt += " " * ((7 - len(e)) // 2) + e + " " * ((7 - len(e)) // 2)
            break

        print(testtt)


 #       for i in self.new_str_datas.split("\n"):
 #           if len(i) == max(self.len_rows):
 #               print(i)
 #           elif len(i) <= max(self.len_rows):
 #              i = i.replace(" ", " " * ((max(self.len_rows) - len(i)) // self.columns))
 #               print(i)

        #return self.new_str_datas#new_str_datas


#test = Beautiful((["Hello", "world", "!"], [4, 1, 6], [1, 2, 3], [4, 5, 6]), 3)
#print(test.show())

"""
+-------------------------+
| 'Hello' | 'world' | '!' |
+-------------------------+
|    4    |    5    |  6  |
+-------------------------+
|    1    |    2    |  3  |
+-------------------------+
|    4    |    5    |  6  |
+-------------------------+
"""


#(7 - 1) // 2