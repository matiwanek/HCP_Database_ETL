import psycopg2
from sql_queries import *
from data_collector import DataCollector
import yaml


class FillDatabase(DataCollector):

    with open('config.yaml') as f:
        my_dict = yaml.safe_load(f)

    def __int__(self):
        conn = psycopg2.connect(database=self.my_dict['database_credentials']['database'],
                                user=self.my_dict['database_credentials']['user'],
                                password=self.my_dict['database_credentials']['password'],
                                host=self.my_dict['database_credentials']['host'])

        conn.set_session(autocommit=True)
        cur = conn.cursor()
        collector = DataCollector()
        data = collector.load_data()

        # insert doctors records
        for a in list(data.values):
            cur.execute(doctors_table_insert, a)
        conn.cursor()
