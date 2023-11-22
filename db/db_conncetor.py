import datetime
import mysql.connector

class Connector():
    def __init__(self, host, username, password, database):
        self.host = host
        self.username = username
        self.password = password
        self.db_name = database
        
        try:
            self.db = mysql.connector.connect(
                host=self.host,
                user=self.username,
                password=self.password,
                database=self.db_name,
                auth_plugin="mysql_native_password"
            )
            self.cursor = self.db.cursor()
            print("[Sucessfully Connected!]")
            
        except:
            raise ConnectionError

    def send(self, table_name, *args):
        """ Insert data at database """
        time = datetime.datetime.now().strftime("%Y-%m-%d %I:%M:%S")
        query = f'INSERT INTO {table_name}(time, cmd_string, arg_string, is_finish) VALUES (%s, %s, %s, %s)'
        data = (time, args[0], args[1], args[2])
        
        self.cursor.execute(query, data)
        self.db.commit()
        return

    def get(self, table_name, limit):
        """ Update database status """
        query = f'SELECT * FROM {table_name} ORDER BY TIME DESC LIMIT {limit}'
        self.cursor.execute(query)

        return_value = [[id, time, cmd_string, arg_string, is_finish] for (id, time, cmd_string, arg_string, is_finish) in self.cursor]
        self.db.commit()
        return return_value
    
    def delete(self, table_name, id):
        """ Delete column with specific id """
        query = f"DELETE FROM {table_name} WHERE id = %s"
        data = (id,)
        self.cursor.execute(query, data)
        self.db.commit()
    
    def close(self):
        """ Close connection (cursor and database) """
        self.cursor.close()
        self.db.close()

    
if __name__ == '__main__':
    # Connect to database
    try:
        connector = Connector(
            host="3.39.251.181",
            username="user",
            password="1234",
            database="driveDB",
        )
    except ConnectionError as e:
        print("Connection Error")
        exit(-1)

    connector.send(
        "command",
        "front",
        "argument",
        "0"
    )
    
    return_value = connector.get("command", 1)
    for return_list in return_value:
        print("\tData")
        print(f'\t\tid         : {return_list[0]}')
        print(f'\t\tdate       : {return_list[1].strftime("%Y-%m-%d %I:%M:%S")}')
        print(f'\t\tcmd_string : {return_list[2]}')
        print(f'\t\targ_string : {return_list[3]}')
        print(f'\t\tis_finish  : {return_list[4]}')
    
    # Select last id to delete the data that is inserted experimentally.
    id_last = return_value[-1][0]

    connector.delete("command", id_last)

    connector.close()

    

