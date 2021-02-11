import pymysql.cursors


class DBconnection:
    def __init__(self):
        self.connection = pymysql.connect(host='localhost', user='root', password='zaq12wsx', database="PROJEKT1")

con_DB = DBconnection()

connect = con_DB.connection


class Operations:
    def __init__(self):
        pass

    def oneOption(self):
        u_FirstName = input("Enter First name of user: ")
        u_LastName = input("Enter Last name of user: ")
        u_DepartmentCode = input("Enter Department Code of user: ")
        sql = "INSERT INTO Employees (FirstName, LastName, DepartmentCode) VALUES (%s, %s, %s)"
        return cursor.execute(sql, (u_FirstName, u_LastName, u_DepartmentCode))

    def twoOption(self):
        u_FirstName = input("Enter First name of user: ")
        u_LastName = input("Enter Last name of user: ")
        sql = "DELETE FROM Employees WHERE FirstName=(%s) AND LastName=(%s)"
        return cursor.execute(sql, (u_FirstName, u_LastName))


    def treeOption(self):
        LastName = input("Input Last Name what you looking for: ")
        new_FirstName = input("Input New First Name: ")
        sql = "UPDATE Employees SET FirstName=(%s) WHERE LastName=(%s)"
        return cursor.execute(sql, (new_FirstName, LastName))


    def fourOption(self):
        sql = "SELECT * FROM Employees"
        cursor.execute(sql)
        b = cursor.fetchall()
        for _ in b:
            print(_)

    def checkTabelExists(self, tableName):
        sql = "SHOW TABLES"
        cursor.execute(sql)
        tables = cursor.fetchall()
        for (table_name,) in tables:
            if table_name == tableName:
                return table_name


class Menu:
    def menuList(self):

        print("#" * 20)
        print("1. Add user.")
        print("2. Delete user.")
        print("3. Modify user.")
        print("4. Show all users.")
        print("5: Quit.")
        print("#" * 20)
        print()
        # user_input = int(input("Pleas input what do your want to do: "))

menu = Menu()
operation = Operations()

with connect:
    with connect.cursor() as cursor:

        work_table = input("Input name of table with you wont to work: ")
        operation.checkTabelExists(work_table)

        if operation.checkTabelExists(work_table):
            menu.menuList()

        else:
            while operation.checkTabelExists(work_table) != work_table:
                print("Your tabel not existe! Select another table")
                work_table = input("Input name of table with you wont to work: ")
                operation.checkTabelExists(work_table)
                menu.menuList()


        while user_input != 0:
            user_input = int(input("Pleas input what do your want to do: "))
            if user_input == 1:
                operation.oneOption()
            elif user_input == 2:
                operation.twoOption()
            elif user_input == 3:
                operation.treeOption()
            elif user_input == 4:
                operation.fourOption()
            elif user_input == 5:
                print("Thank you for using this program Goodbye.")
                break
            else:
                print("Option not existe!")
            menu.menuList()
            user_input = int(input("Pleas input what do your want to do: "))
        connect.commit()





