import sqlite3

# connection = sqlite3.connect("practice.db")


# cursor = connection.cursor()


# creating a table

# sql_command = """

# CREATE TABLE  employee(
# staff_number INTEGER PRIMARY KEY,
# fname VARCHAR(20),
# lname VARCHAR(30),
# gender CHAR(1),
# joining DATE, 
# birth_date DATE);

# """

# cursor.execute(sql_command)

# -----------------------------------------


# manually inserting data into the table

# sql_command = """

# INSERT INTO employee(staff_number, fname, lname, gender, birth_date)

# VALUES (NULL, "WILLIAM", "SHAKESPEARE", "m", "1961-10-17");

# """

# cursor.execute(sql_command)

# sql_command = """

# INSERT INTO employee(staff_number, fname, lname, gender, birth_date)

# VALUES (NULL, "FRANK", "SCHILLER", "m", "1955-08-17");
# """

# cursor.execute(sql_command)


# ---------------------------------------------


# to make sure changes are saved include: 


# connection.commit()

# connection.close()


# -----------------------------------------


# insert data algorithmically 


# staff_data = [
# ("Frank", "Porthos", "m", "1984-03-12"),
# ("Frank", "Porthos", "m", "1984-03-12"),
# ("Zed","Rickenbacker", "m", "2000-01-19"),
# ("Frank", "Porthos", "m", "1984-03-12"),
# ("Mary", "Ozone", "f", "1912-02-20"),
# ("Frank", "Porthos", "m", "1984-03-12"),
# ("Zed","Rickenbacker", "m", "2000-01-19"),
# ("Mary", "Ozone", "f", "1912-02-20"),
# ("Mary", "Ozone", "f", "1912-02-20")]

# for info in staff_data: 
#     format_str = """
#     INSERT INTO employee (staff_number, fname, lname, gender, birth_date)
    
#     VALUES (NULL, "{first}", "{last}", "{gender}", "{birthdate}");
#     """
#     sql_command = format_str.format(first = info[0], last = info[1], gender = info[2], birthdate = info[3])

#     cursor.execute(sql_command)


# connection.commit()

# connection.close()

# ---------------------------------------------------



# query table


# connection = sqlite3.connect("practice.db")


# cursor = connection.cursor()


# cursor.execute(
# "SELECT * FROM employee"
# )

# print("fetchall:")
# result = cursor.fetchall()

# for r in result:
#     print(r)

# cursor.execute(
# "SELECT * FROM employee"
#     )

# print("\nfetch one:")

# res = cursor.fetchone()

# print(res)

# -------------------------------------------------------------

# checking number of tables in an sqlite database


connection = sqlite3.connect("pitchfork.sqlite")


cursor = connection.cursor()


sql_command = """
SELECT name
FROM sqlite_master
WHERE type = 'table'
ORDER BY name; 

"""


cursor.execute(sql_command)

print(cursor.fetchall())