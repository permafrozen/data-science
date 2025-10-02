import json

import requests
import keyring
import getpass

login_url = "https://hypate.webuntis.com/WebUntis/j_spring_security_check"
token = ""

service_name = "webuntis_fetcher"
magic_username_key = "credentials_csv"


def get_header() -> str:
    return r"""
                  _                 _   _
    __      _____| |__  _   _ _ __ | |_(_)___
    \ \ /\ / / _ \ '_ \| | | | '_ \| __| / __|
     \ V  V /  __/ |_) | |_| | | | | |_| \__ \
      \_/\_/ \___|_.__/ \__,_|_| |_|\__|_|___/
    """


def get_keyring_credentials() -> dict[str, str] | None:
    credentials = keyring.get_password(service_name, service_name)

    if credentials is not None:
        credentials = json.loads(credentials)

    return credentials


def get_credential_dump(school: str, username: str, password: str) -> str:
    return json.dumps({"school": school, "username": username, "password": password})


def set_keyring_credentials(school: str, username: str, password: str) -> None:
    keyring.set_password(service_name, service_name, get_credential_dump(school, username, password))


def read_credentials() -> None:
    school = input("School: ")  # "htbla_wels"
    j_username = input("Username: ")
    j_password = getpass.getpass("Password: ")
    set_keyring_credentials(school, j_username, j_password)


def main():
    print(get_header())

    if get_keyring_credentials() is None:
        read_credentials()

    credentials = get_keyring_credentials()

    payload = {
        "school": credentials["school"],
        "j_username": credentials["username"],
        "j_password": credentials["password"],
        "token": token
    }

    s = requests.Session()
    s.headers.update({"Accept": "application/json"})

    login = s.post(login_url, data=payload)
    print(login.json()["state"])

    if login.json()["state"] == "SUCCESS":
        auth = s.get("https://hypate.webuntis.com/WebUntis/api/token/new").text
        s.headers.update({"Authorization": "Bearer " + auth}) # Token for authentification

        grid = s.get("https://hypate.webuntis.com/WebUntis/api/rest/view/v1/timetable/grid?timetableType=MY_TIMETABLE").json()
        print(grid)



if __name__ == "__main__":
    main()
