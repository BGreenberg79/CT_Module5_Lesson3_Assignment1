from add_members import add_members
from add_workout_session import add_workout
from update_members import update_member_age
from delete_workout import delete_workout_session
from get_members_in_age_range import get_members_in_age_range

while True:
    try:
        print("Gym Management Database System:")
        print("1. Add a Member")
        print("2. Add a Workout")
        print("3. Update a member's age")
        print("4. Delete a workout session")
        print("5. Search for members between two ages")
        print("6. Quit")
        main_menu_input = input("Enter choice here (1-6): ")
        if main_menu_input == "1":
            new_id_input = int(input("Please enter ID of new member here: "))
            new_name_input= input("Please enter name here: ")
            new_age_input = int(input("Please enter new age: "))
            add_members(new_id_input, new_name_input, new_age_input)
        elif main_menu_input == "2":
            new_session_id = int(input("Please enter this workout's new session ID: "))
            member_id = int(input("Please enter the Member ID of the member who completed this workout: "))
            new_session_date = input("Please enter the date of this workout (YYYY-MM-DD): ")
            new_session_time = input("Please enter the time of this workout: ")
            new_activity = input("Please enter the activity completed: ")
            add_workout(new_session_id, member_id, new_session_date, new_session_time, new_activity)
        elif main_menu_input == "3":
            update_member_id = int(input("Enter the member ID for the member who's age you wish to update: "))
            updated_age = int(input("Please enter the new value for this member's age: "))
            update_member_age(update_member_id, updated_age)
        elif main_menu_input == "4":
            delete_session_input = int(input("Please enter the workout session Id for the entry you wish to delete: "))
            delete_workout_session(delete_session_input)
        elif main_menu_input == "5":
            search_start_age = int(input("Please enter the starting age of members you wish to search for: "))
            search_end_age = int(input("Please enter the ending age of members you wish to search for: "))
            get_members_in_age_range(search_start_age, search_end_age)
        elif main_menu_input == "6":
            break
        else:
            print("PLease enter a valid input of 1-6")
        
    except Exception as e:
        print(f"Error: {e}")


'''
The main module imports functions from the add_members, add_workout_session, update_members, delete_workouts, and get_members_in_age_range modules. In a while loop I print the 6 different choices for functions our users can call to modify or work with our Gym Management Database system.
If the user chooses option 1 they will be prompted for input's requesting our new entries ID, name, and age. The inputs for id and age are wrapped in int() functions to convert string to integer types. I then call the add_members function. Similarly in
choice 2 we take inputs for session ID, member ID, session date, session time, and activity. We convert those first two inputs to integer and then call the add_workout function with all 5 inputs.
In choice 3 we take inputs for which member ID we wish to update and the age we wish to set as the new value. Both numbers are converted to integers and then the update_member_age function is called.
In choice 4 we take an input asking which session ID we wish to delete and convert it into integer type. Once that is done we call delete_workout_sessions with that input.
In choice 5 we take inputs for the range of ages we wish to start and end our search between. We convert both values to integer type and then call get_members_in_age_range with the two inputs.
In choice 6 we break the while loop and an else statement catches any invalid inputs. Lastly an except block is used to catch any errors originating in this module.
'''