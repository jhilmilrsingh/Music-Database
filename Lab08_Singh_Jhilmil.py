import sqlite3

db_name = 'Music.db'

def select_all(db_cursor):
    sql_statement = 'SELECT * from music'
    result_set = db_cursor.execute(sql_statement)
    print("\nTable now has the following rows:")
    for row in result_set:
        print(row)
    print()
    
def db_steps():
    db_conn = sqlite3.connect(db_name)
    db_cursor = db_conn.cursor()
    print("Connected to DB.")

    sql_statement = 'DROP TABLE IF EXISTS music'
    db_cursor.execute(sql_statement)
    print("Dropped Table.")

    sql_statement = 'CREATE TABLE music (album TEXT, genre TEXT, artist TEXT, license INTEGER, track INTEGER, song TEXT)'
    db_cursor.execute(sql_statement)
    print("Created Table.")

    db_conn.commit()
    
    sql_statement = 'INSERT INTO music VALUES (?, ?, ?, ?, ?, ?)'
    tuple_of_field_values = ('Blessed', 'Romantic', 'Helen', 1, 10, 'Faith')
    
    db_cursor.execute(sql_statement, tuple_of_field_values)
    print("Inserted row into table.")

    tuple_of_field_values = ('Christmas', 'Pop', 'Troy', 2, 5, 'Jingle Bells')
    db_cursor.execute(sql_statement, tuple_of_field_values)
    print("Inserted row into table.")

    tuple_of_field_values = ('Tool', 'Metal', 'William', 3, 8, 'Drum')
    db_cursor.execute(sql_statement, tuple_of_field_values)
    print("Inserted row into table.")

    db_conn.commit()
    
    select_all(db_conn)
    
    sql_statement = 'SELECT * from music WHERE album = ?'
    tuple_of_key_value = ('Blessed', )
    result_set = db_conn.execute(sql_statement, tuple_of_key_value)
    print("Selected one row of key", 'Blessed')
    for row in result_set:
        print(row)
        
    sql_statement = 'UPDATE music SET track = ? WHERE track = ?'
    tuple_to_give = (6, 8)
    db_cursor.execute(sql_statement, tuple_to_give)
    print("\nUpdated row of key 6", tuple_to_give)
    db_conn.commit()
    
    select_all(db_conn)

    sql_statement = 'DELETE FROM music WHERE album = ?'
    tuple_of_key_value = ('Blessed', )
    db_cursor.execute(sql_statement, tuple_of_key_value)
    print("Deleted row of key", 'Blessed')
    db_conn.commit()

    select_all(db_conn)

    db_conn.close()

def main():
    db_steps()
main()
