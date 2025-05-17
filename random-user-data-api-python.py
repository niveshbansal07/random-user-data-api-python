import requests

# Fetches user data from a public API
def fetch_data_with_API():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    data = response.json()

    if data["data"] and "data" in data:
        user_data = data["data"]
        return (
            user_data["login"]["username"],
            user_data["phone"],
            user_data["email"],
            user_data["location"]["country"]
        )
    else:
        raise Exception("Request was not successful. Try again!")

def main():
    try:
        user_name, user_phone, user_email, user_country = fetch_data_with_API()
        print(f"User Name: {user_name}")
        print(f"User Phone No.: {user_phone}")
        print(f"User Email: {user_email}")
        print(f"User Country: {user_country}")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()
