import os
import sys
import random
import requests
import datetime

from faker import Faker
from math import ceil


if __name__ == "__main__":

    # number of fake account
    num_account = 15

    try:
        num_account = int(sys.argv[1])
    except IndexError:
        print('Using Default', num_account)
    
    os.chdir('../')
    file_path = os.getcwd() + os.sep + 'data' + os.sep

    # target host url
    target_url = ''
    target_form_email = 'email'
    target_form_password = 'pass'

    # initiate password
    fake = Faker('id_ID')

    # read common password to make it genuine input
    common_password = open(file_path + 'password.txt', 'r')
    list_password = common_password.readline()
    max_line = len(list_password)

    # generate random rubbish information
    for item in range(1, num_account + 1):
        # initialize fake account
        fullName = (fake.first_name()+"."+fake.last_name()).lower()
        email = fullName + "@example.com"
        password = list_password[random.randint(0, max_line - 1)].replace("\n", "") + fake.password(length=4, special_chars=False, digits=True, upper_case=False, lower_case=False)
        user_agent = fake.chrome()

        # payload & header for requests
        headers = {'User-Agent': user_agent}
        payload = {
            target_form_email:email,
            target_form_password:password
        }

        # proceed request
        resp = requests.post(target_url,headers=headers,data=payload)
        if resp.status_code == 200:
            if item % ceil(num_account / 2) == 0 or item == num_account:
                print("{} | {} Payload Submitted.".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), str(item)))

