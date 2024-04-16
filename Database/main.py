#Name: Jackson Shangraw
#Date: 03/04/24
#Purpose: Database
import database
connection = database.create_connection("items.db")
database.create_table(connection,"Items",["first TEXT","second TEXT","amount REAL"])
#database.insert_db(connection,"Items",["first","second","amount"],["ball","net",15])
database.update_db(connection,"Items",["first='toy'"],"id=1")
database.delete_db(connection,"Items",["first='ball'"],"id=1",1)

results = database.select_db(connection,"Items").fetchall()
results = database.select_db(connection,"Items",["first='ball'"]).fetchall()

for r in results:
    print(f"Items:{r[1]} {r[2]} {r[3]}")