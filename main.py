from scripts.functions import get_access_token, create_connection, get_save_sublink

"""The run script"""


if __name__ == "__main__":
    start = int(input("start number: "))
    end = int(input("end number: "))
    data = int(input("users data: "))
    data = data * 1024 * 1024 * 1024       # Converting GB to bytes

    get_access_token()
    create_connection(data, start, end)
    get_save_sublink(start, end)