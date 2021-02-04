import pymysql.cursors


class DBconnection:
    def __init__(self):
        self.connection = pymysql.connect(host='localhost', user='root', password='zaq12wsx', database="PROJEKT1")

con_DB = DBconnection()

connect = con_DB.connection



class Operations:
    def __index__(self):
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
        # old_FirstName = input("Input First Name to change: ")
        new_FirstName = input("Input New First Name: ")
        sql = "UPDATE Employees SET FirstName=(%s) WHERE id=2"
        return cursor.execute(sql, new_FirstName)


    def fourOption(self):
        sql = "SELECT * FROM Employees"
        cursor.execute(sql)
        b = cursor.fetchall()
        for _ in b:
            print(_)
        return connect.commit()

class Menu():
    def menuList(self):
        print("#" * 20)
        print("1. Add user.")
        print("2. Delete user.")
        print("3. Modify user.")
        print("4. Show all users.")
        print("5: Quit.")
        print("#" * 20)

with connect:
    with connect.cursor() as cursor:
        # sql = "CREATE TABLE Employees (id INT AUTO_INCREMENT PRIMARY KEY, FirstName VARCHAR(30), LastName VARCHAR(30), DepartmentCode INT)"
        menu = Menu()
        menu.menuList()
        operation = Operations()
        user_input = int(input("Pleas input what do your want to do: "))

        while user_input != 5:
            if user_input == 1:
                operation.oneOption()
            elif user_input == 2:
                operation.twoOption()
            elif user_input == 3:
                operation.treeOption()
            elif user_input == 4:
                operation.fourOption()
            menu.menuList()
            user_input = int(input("Pleas input what do your want to do: "))
    connect.commit()




