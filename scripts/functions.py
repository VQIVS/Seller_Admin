from scripts.model import UserManager, UserManagerError

user_obj = UserManager()

""" A function to create a new user """


def create_connection(data, start, end):
    for number in range(start, end):
        try:
            user_obj.creat(number, data)
            print("Success")
        except UserManagerError as e:
            print(f"Failed: {e}")


""" A function to get and save the user subscription link """

def get_save_sublink(start, end):
    try:
        with open("subscription_links.txt", "w") as file:
            for user_num in range(start, end):
                username = f"TN_{user_num}"
                try:
                    sub_link = user_obj.sublink(username)
                    file.write(f"{username} : {sub_link}\n")
                except UserManagerError as e:
                    print(f"Error for {username}: {e}")
    except Exception as e:
        print(f"Error writing to file: {e}")


"""" A function to retrieve the access token from the panel """

def get_access_token():
    try:
        user_obj.get_token()
        print("Token retrieved successfully")
    except UserManagerError as e:
        print(f"Error getting access token: {e}")
