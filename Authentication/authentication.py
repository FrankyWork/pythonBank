import json


def get_date(identification, authentication):
    with open("Authentication/data_file.json", "r") as authorization_date:
        data = json.load(authorization_date)
        try:
            if identification == data[identification]["login"]:
                print("Authorization successfully")
            if authentication == data[identification]["password"]:
                print("Hello", data[identification]["name"], data[identification]["lastName"], "!!!" "\nYour login:",
                      data[identification]["login"], "\nYour balance:", data[identification]["balance"])
        except KeyError:
            print("Authorization failed!")
