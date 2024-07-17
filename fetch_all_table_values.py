from  connect_mysql import connect_database

conn = connect_database()
if conn is not None:
    try:
        cursor = conn.cursor()
        query = "SELECT * FROM Members"
        cursor.execute(query)
        print("Members Table:")
        for row in cursor.fetchall():
            print(row)
        
        query_2 = "SELECT * FROM WorkoutSessions"
        cursor.execute(query_2)
        print("Workout Sessions Table:")
        for row in cursor.fetchall():
            print(row)    
                
    except Exception as e:
         print(f"Error: {e}")

    finally:
            cursor.close()
            conn.close()
            print("MySQL connection is closed.")


'''
This file was used to help me build my code in my functions and main module, returning all values from both tables. This also helped with checking my work.
'''