import pymysql.cursors


connection = pymysql.connect(host='localhost', user='root', password='zaq12wsx', database="PROJEKT1")

print("#" * 20)
print("1. Add user.")
print("2. Delete user.")
print("3. Modify user.")
print("4. Show all users.")
print("#" * 20)
user_input = input("Pleas input what do yopu want to do: ")

with connection:
    with connection.cursor() as cursor:
        # sql = "CREATE TABLE Employees (id INT AUTO_INCREMENT PRIMARY KEY, FirstName VARCHAR(30), LastName VARCHAR(30), DepartmentCode INT)"
        # sql = "INSERT INTO Employee(LastName, FirstName, DepartmentCode) VALUES (%s, %s, %s)"
        sql = "SELECT * FROM Employees"
        # cursor.execute(sql, ('Jan', 'Kos', 4))
        #sql = "DROP TABLE IF EXISTS {}".format("customers")
        b = cursor.execute(sql)
        print(b)
    connection.commit()



# class Menu:
#     pass
#
# class DBin:
#     pass
#
# class DBout:
#     pass
