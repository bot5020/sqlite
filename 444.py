import sqlite3

def test(sql):
    try:
        connection = sqlite3.connect("test.db")
        cursor = connection.cursor()
        cursor.execute(sql)
        a = cursor.fetchall()
        connection.commit()
        return(a)
        print(a)
        connection.close()
    except Exception as e:
        print(e)
print(test("CREATE TABLE table_name (`id` INTEGER PRIMARY KEY AUTOINCREMENT, `column2` text, `column3` text);"))

