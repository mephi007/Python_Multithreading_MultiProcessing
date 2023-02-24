import psycopg2
from queries import create_table, postgres_insert_query
import logging 

class Dump_to_db():
  def __init__(self):
    logging.basicConfig(filename="logs/std.log", 
					format='%(asctime)s %(message)s', 
					filemode='w') 
    self.logger=logging.getLogger() 
    self.logger.setLevel(logging.DEBUG)

    self.conn = psycopg2.connect(
      database="postgres", user='sumitroy', password='admin', host='127.0.0.1', port= '5432'
    )
    self.cursor = self.conn.cursor()
    data = self.cursor.execute(create_table)
    self.logger.info("Table created successfully........")

  def dump_to_db(self, file_to_db):
    record_to_insert = (file_to_db.id, file_to_db.file_url, file_to_db.content_type, file_to_db.content_length, file_to_db.last_modified)
    self.cursor.execute(postgres_insert_query, record_to_insert)
    self.logger.info(f'insert {file_to_db.file_url} to db')

  def __del__(self):
    self.conn.commit()
    self.conn.close()
