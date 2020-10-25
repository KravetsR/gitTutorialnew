import sqlite3

class SQLighter:
    def __init__(self, datebase):
        ''' Connect to database '''
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()

    def get_subscriptions(self, status = True):
        ''' Get all active subscribers'''
        with self.connection:
            return self.cursor.execute("SELECT * FROM 'subscriptions' WHERE 'status' = ?",(status,)).fetchall()

    def subscriber_exists(self, user_id):
        ''' check if the user is in the database'''
        with self.connection:
            result = self.cursor.execute("SELECT * FROM 'subscripttions' WHERE 'user_id' = ?", (user_id)).fetchall()
            return bool(len(result))

    def add_subscriber(self, user_id, status = True):
        ''' add a new user '''
        with self.connection:
            return self.cursor.execute("INSERT INTO 'subscriptions' ('user_id', 'status') VALUES (?,?)", (user_id, status))

    def update_subscription(self, user_id, status):
        ''' update subscription status '''
        return self.cursor.execute("UPDATE 'subscriptions' SET 'status' = ? WHERE 'user_id' = ? ", (status, user_id))
    
    def close(self):
        ''' close the connection to the database '''
        self.connection.close()