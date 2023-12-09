from scripts.model import UserManagerError

""" A function to create a new user """


def create_connection(user_obj, start, end, data):
    for number in range(start, end + 1):
        try:
            user_obj.create(number, data)
            print("Success")
        except UserManagerError as e:
            print(f"Failed: {e}")


""" A function to get and save the user subscription link """


def get_save_sublink(user_obj, start, end):
    try:
        with open("subscription_links.txt", "w") as file:
            for user_num in range(start, end + 1):
                username = f"USER{user_num}"
                try:
                    sub_link = user_obj.sublink(username)
                    file.write(f"{username} : {sub_link}\n")
                except UserManagerError as e:
                    print(f"Error for {username}: {e}")
    except Exception as e:
        print(f"Error writing to file: {e}")


"""" A function to retrieve the access token from the panel """


def get_access_token(user_obj):
    try:
        user_obj.get_token()
        print("Token retrieved successfully")
    except UserManagerError as e:
        print(f"Error getting access token: {e}")


"""A function to delete users from the panel"""


def delete_connection(user_obj, start, end):
    for number in range(start, end + 1):
        try:
            username = f"USER{number}"
            user_obj.delete(username)
            print("Deleted successfully")
        except UserManagerError as e:
            print(f"Failed: {e}")
