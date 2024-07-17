#Task 2.1 SQL Between Usage
from connect_mysql import connect_database

conn = connect_database()

def get_members_in_age_range(start_age, end_age):
    if conn is not None:
        try:
            cursor = conn.cursor()
            list_of_members = []

            query = "SELECT * FROM Members WHERE age BETWEEN %s AND %s"
            value_tuple = (start_age, end_age)
            
            cursor.execute(query, value_tuple)
            for member in cursor.fetchall():
                list_of_members.append(member)
            
            if not list_of_members:
                print("No members found in age range you are searching for.")
            else:
                print(f"List of Members Between {str(start_age)} and {str(end_age)}:")
                for index, member_tuple in enumerate(list_of_members, 1):
                    print(f"Search Result {str(index)}\nMember ID: {member_tuple[0]}\nName: {member_tuple[1]}\nAge: {member_tuple[2]}")
                    print("\n")

        except Exception as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()

'''
First we establish a connection to the database by using the imported connect_database function. Then after using an if statement to ensure the connection is succesful in a try block I instantiate cursor using the conn.cursor method.
I also istantiate an empty list of members. In query I use an SQL statement to return all columns from the Members table where the values for age are between placeholders for start and end age. Then I assign our two inputs to a tuple I call value tuple.
I then use the cursor.execute method with the string for query and the tuple for value_tuple. I then use a for loop and the fetchall() method to append every tuple of member info it returns onto our list of members.
If the list_of_members is empty I use an if not statement to print that no members were found in the age range the user is searching for. In the else statement I use f-strings to print the List of Members between the two ages and a for loop with the enumerate method to
print each search result number (with index), each member ID, name, and age (using the syntax of member_tuple[tuple_index]) separated by new line breaks.
'''