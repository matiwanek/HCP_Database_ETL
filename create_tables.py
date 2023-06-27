import psycopg2
from sql_queries import doctors_table_create, doctors_table_drop
import yaml


class ManageDatabase:
    with open('config.yaml') as f:
        my_dict = yaml.safe_load(f)

    # connect to default database
    conn = psycopg2.connect(database=my_dict['default_database_credentials']['database'],
                            user=my_dict['default_database_credentials']['user'],
                            password=my_dict['default_database_credentials']['password'],
                            host=my_dict['default_database_credentials']['host'])
    conn.set_session(autocommit=True)
    cur = conn.cursor()

    cur.execute("DROP DATABASE IF EXISTS hcpdatabase")
    cur.execute("CREATE DATABASE hcpdatabase WITH ENCODING 'utf8' TEMPLATE template0")
    conn.close()

    # connect to hcp database
    conn = psycopg2.connect(database=my_dict['database_credentials']['database'],
                            user=my_dict['database_credentials']['user'],
                            password=my_dict['database_credentials']['password'],
                            host=my_dict['database_credentials']['host'])
    cur = conn.cursor()

    def drop_tables(self):

        self.cur.execute(doctors_table_drop)
        self.conn.commit()

    def create_tables(self):

        self.cur.execute(doctors_table_create)
        self.conn.commit()