from datetime import datetime
import requests as req
import sys
from dotenv import load_dotenv
import os

load_dotenv()

USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')
VAFS_CLIENT_ID = os.getenv('VAFS_CLIENT_ID')


def get_date():
    return datetime.today().strftime("%d/%m/%Y")


def get_period():
    if int(datetime.today().strftime("%H")) >= 12:
        return "P"

    return "A"


def login_to_page():

    url = "https://vafs.nus.edu.sg/adfs/oauth2/authorize"

    params = {
        "response_type": "code",
        "client_id": VAFS_CLIENT_ID,
        "resource": "sg_edu_nus_oauth",
        "redirect_uri": "https://myaces.nus.edu.sg:443/htd/htd"
    }

    login_info = {"AuthMethod": "FormsAuthentication",
                  "UserName": "nusstu\\" + USERNAME,
                  "Password": PASSWORD,
                  }
    response = req.post(url=url, data=login_info, params=params)

    if response.status_code != 200 or "JSESSIONID" not in response.cookies:
        print("Log in failed. Error Code:", response.status_code)
        sys.exit(1)
    else:
        print("Logged in successfully.")
        return response.cookies["JSESSIONID"]


def submit_declaration(cookie):

    url = "https://myaces.nus.edu.sg/htd/htd"
    cookie = {"JSESSIONID": cookie}

    data = {"actionName": "dlytemperature",
            "tempDeclOn": get_date(),
            "declFrequency": get_period(),
            "symptomsFlag": "N",
            "familySymptomsFlag": "N"}

    response = req.post(url=url, cookies=cookie, data=data)

    if response.status_code != 200:
        print("Failed to declare temperature. HTTP Error Code:",
              response.status_code)
        sys.exit(1)

    print("Submitted successfully.")


if __name__ == "__main__":
    submit_declaration(login_to_page())
    sys.exit(0)
