# Task 1.1 Add a member

from connect_mysql import connect_database

conn = connect_database()

def add_members(id, name, age):
    if conn is not None:
        try:
            cursor = conn.cursor()

            new_member = (id, name, age)

            query = "INSERT INTO Members (id, name, age) VALUES (%s, %s, %s)"

            cursor.execute(query, new_member)
            conn.commit()
            print("New member succesfully added")
        
        except Exception as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()

'''
This function works by taking inputs for Member ID, name, and age. If we can succesully establish the database connection by importing the connect_database() function then our program tries to initiate a cursor with that connection using the .cursor method
Once we succesfully instantiate the cursor, we take a tuple with our three inputs at new_member in the order our database is formatted. Then in query we type a string using the SQL syntax to insert our inputs into the Members table, identifying the columns in the correct order and using the %s placeholder until our tuple at new_member takes its place.
Then we use the .execute method with the cursor using the query string and new_member tuple. We then commit this change to the database using our connection and print the succesful result. An except block helps gracefully pick up any error messages to safeguard our process, and the finally block closes the cursor and connection we have established
'''

