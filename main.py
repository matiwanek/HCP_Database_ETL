from create_tables import ManageDatabase
from etl import FillDatabase


new_database = ManageDatabase()
insert_values = FillDatabase()

new_database.drop_tables()
new_database.create_tables()

insert_values.__int__()
