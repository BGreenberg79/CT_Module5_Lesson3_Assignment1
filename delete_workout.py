from connect_mysql import connect_database

#Task 1.4 Delete a Workout Session

conn = connect_database()

def delete_workout_session(session_id):
    if conn is not None:
        try:
            cursor = conn.cursor()
            
            search_query = "SELECT session_id FROM WorkoutSessions"
            id_tup = ()

            cursor.execute(search_query)
            for id in cursor.fetchall():
                id_tup += id
            
            if session_id in id_tup:
                query = "DELETE FROM WorkoutSessions WHERE session_id = %s"

                cursor.execute(query, (session_id,))
                conn.commit()
                print(f"Workout ID {session_id} deleted from Workout Session Table")
            else:
                print("Please ensure the workout you are trying to delete is one that has already been added.")
        
        except Exception as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()

'''
The delete_workout_session function check if there is a connection from the connect_database imported function we call. Once it does that in a try block it instantiates the cursor and in search_query I enter the SQL statement to return all session_id's from the WorkoutSEssions table.
I then instantiate the empty id_tup tuple and execute the search_query. In a for loop I add and join each tuple the .fetchall() method returns to id_tup so we have a tuple with every session_id. Then if the input session_id is in our id_tup
I assign the variable query with the SQL statement to delete from the WorkoutSessions the value where the session_id column equals our input. I execute the query with the input session_id placed in a 1 item long tuple. I then commit the change and print a success message. In my else statement 
I print if the user is trying to delete a workout with a session that has not been first added to the database. I then have an except block where any exceptions are caught and a finally block to close the cursor and connection.
'''