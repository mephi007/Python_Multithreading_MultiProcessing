create_table = ''' CREATE TABLE IF NOT EXISTS fetched_file_details (
      id varchar(255) NOT NULL,
      file_url varchar(1000) NOT NULL,
      content_type varchar(255),
      content_length varchar(255),
      last_modified varchar(255),
      PRIMARY KEY (id, file_url, last_modified)
    ) '''

postgres_insert_query = ''' INSERT INTO fetched_file_details (id, file_url, content_type, content_length, last_modified) VALUES (%s,%s,%s,%s,%s) '''
