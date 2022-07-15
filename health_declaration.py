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
    # returns current date in specified format
    return datetime.today().strftime("%d/%m/%Y")


def get_period():
    # returns whether it is AM or PM  based on current time
    if int(datetime.today().strftime("%H")) >= 12:
        return "P"

    return "A"


def login_to_page():

    # temp declaration login page URL
    url = "https://vafs.nus.edu.sg/adfs/oauth2/authorize"

    # params for login page
    params = {
        "response_type": "code",
        "client_id": VAFS_CLIENT_ID,
        "resource": "sg_edu_nus_oauth",
        "redirect_uri": "https://myaces.nus.edu.sg:443/htd/htd"
    }

    # authentication info
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

    # temp declaraion URL
    url = "https://myaces.nus.edu.sg/htd/htd"

    # session cookie
    cookie = {"JSESSIONID": cookie}

    # temp declaration info
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
