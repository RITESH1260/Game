# we import mysql as a databse connector to connect to the database and perform operations
import mysql.connector as conn

# we create a class called Agent which will have the attributes name, email and phone number of the agent
class Agent:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def save_to_db(self):  # Save the agent's information to the database #
        try:
            connection = conn.connect(host='localhost', database='real_estate', user='root', password='root')
            cursor = connection.cursor()
            insert_query = "INSERT INTO agents (name, email, phone) VALUES (%s, %s, %s)"
            cursor.execute(insert_query, (self.name, self.email, self.phone))
            connection.commit()
        except conn.Error as error:
            print(f"Failed to insert record into agents table: {error}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()


if __name__ == "__main__":
    
    # agent1 is already saved.
    
    agent2 = Agent("Ritesh", "ritesh1r@gmail.com", "971780652")
    agent3 = Agent("Swati ", "swati@gmail.com", "9855632214")
    agent4 = Agent("Rohit ", "rohit@gmail.com", "987654321")
    
    agent2.save_to_db() 
    agent3.save_to_db()
    agent4.save_to_db()  
    