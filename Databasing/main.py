#display to terminal, insert, delete,
import database
connection = database.create_connection("items.db")
database.create_table(connection,"Items",["first TEXT","second TEXT","amount REAL"])
database.insert_db(connection,"Items",["first","second","amount"],["ball","net",15])
result = database.select_db(connection,"Items").fetchall()
print(result)