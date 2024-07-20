#Task 1.2 Add a Workout Session

from connect_mysql import connect_database

conn = connect_database()

def add_workout(session_id, member_id, session_date, session_time, activity):
    if conn is not None:
        try:
            cursor = conn.cursor()

            new_session = (session_id, member_id, session_date, session_time, activity)

            query = "INSERT INTO Members (session_id, member_id, session_date, sesssion_time, activity) VALUES (%s, %s, %s, %s, %s)"

            cursor.execute(query, new_session)
            conn.commit()
            print("New session succesfully added")
        
        except Exception as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()

'''
Our add_workout function works very similarly to the add_members function. It takes inputs for all 5 columns (including a members_id foreign key) in the WorkoutSessions database and once a connection is established through importing and running connect_database(), it starts by instantiating a cursor
It then places all 5 inputs into a tuple where the inputs are associated to their appropriate location in the database table. Then in query we use %s placeholders in values and proper SQL syntax to insert our inputs into the appropriate cplumns as values.
We then use the .execute method with our cursor object taking our tuple and string inputs to complete the insertion, followed by the .commit method to commit this change to the database. We then print a success statement for user feedbak. I also have a Exception block to catch any errors in our process, and a finally block to close the cursor and connection.
'''
