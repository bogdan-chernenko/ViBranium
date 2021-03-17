

class Beautiful:
    def __init__(self, datas):
        self.clone_datas = []
        self.datas = datas
        self.str_datas = ""
        self.new_str_datas = ""

        self.balance = []

        self.str_with_out = []

        self.max_of_rows = []
        self.round_of_rows = []

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
                "| " + i.replace("  ", " ") + " |\n" +
                ("+" + "-" * (len(self.str_datas.split("\n")[0])) + "+") + "\n"
            )

        self.new_str_datas = "{}\n".format(
            "+" + "-" * (len(self.new_str_datas.split("\n")[0])  - 2) + "+"
        ) + self.new_str_datas


        for i in self.new_str_datas.split("\n"):
            self.balance.append(i.split("|"))

        del self.balance[0]
        del self.balance[-1]

        for i in self.balance:
            del i[0]
            if len(i) > 0:
                del i[-1]#

        for i in self.balance:
            lst = []
            for str_ in i:
                lst.append(len(str_))#

            if len(lst) > 0:
                self.max_of_rows.append(max(lst))
            lst = []

        #print(self.max_of_rows)
        for i in self.balance:
            lst = []
            for s in i:
                s = s.replace(" ", "")
                lst.append(s)

            self.str_with_out.append(lst)
            lst = []

        for i in self.str_with_out:
            rrr = []
            for elem in i:
                rrr.append(len(elem))
            if len(rrr) > 0:
                self.round_of_rows.append(max(rrr))
            rrr = []
 
        for i in self.new_str_datas.split("\n"):
            i = i.replace(" ", "")
            i = i.replace("|", "|{}".format(" " * 4))
            i = i.replace("|", "{}|".format(" " * 4))


        self.clone_datas = self.new_str_datas

        self.dich = self.clone_datas.split("\n")



        for i in self.new_str_datas.split("\n"):
            i = i.replace(" ", " "* 4)
            print(i)

        return self.new_str_datas#new_str_datas


#test = Beautiful((["Hello", "world", "!"], [4, 5, 6], [1, 2, 3], [4, 5, 6]))
#print(test.show())

"""
+-------------------------+
| 'Hello' | 'world' | '!' |
+-------------------------+
|     4   |    5    |  6  |
+-------------------------+
|     1   |    2    |  3  |
+-------------------------+
|     4   |    5    |  6  |
+-------------------------+
"""