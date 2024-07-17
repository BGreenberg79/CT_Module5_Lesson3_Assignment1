from connect_mysql import connect_database

# Task 1.3 Updating Member Info

conn = connect_database()

def update_member_age(member_id, new_age):
    if conn is not None:
        try:
            
            cursor = conn.cursor()

            search_query = "SELECT id FROM Members"
            id_tup = ()

            cursor.execute(search_query)
            for id in cursor.fetchall():
                id_tup += id

            if member_id in id_tup:
                query = "UPDATE Members SET age = %s WHERE id = %s"

                value_tuple = (new_age, member_id)

                cursor.execute(query, value_tuple)
                conn.commit()
                print("Member information updated succesfully.")
            else:
                print("Please ensure the Member ID you are attempting to update has first been added to the database.")

        except Exception as e:
            print(f"Error: {e}")

        finally:
            cursor.close()
            conn.close()

'''
update_member_age works by first checking if a connection is established. Once it is established through the connect_database imported function in a try block it instantiates cursor using the .cursor method.
I then assign the variable search_query and instantiate the empty id_tup tuple. I execute the search query using our cursor and then use the .fetchall method in a for loop where we join every tuple the fetchall returns.
After the loop is completed we can check if the user's member_id is in our id_tup tuple. If it is in the tuple, I assign a string to query where in an SQL query I update the Members Table by changing age at the specific row of a member_id number. In the query I use the %s placeholder.
I assign our two inputs new_age and member_id in their appropriate locations in the calue_tuple variable and then use the cursor.execute() method with the query string and value_tuple tuple, followed by commiting the update to the database.
I then print a success message. In my else statement I print a message if the user has entered an incorrect member_id or an id that hasn't been added yet to the database. Following the try block I have an except block that will handle any errors. Then I have a finally block that closes the cursor and connection
'''