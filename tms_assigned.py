import sys
import requests
import re
import pandas as pd

class Tms_task:
    username = 'vramesh'
    password = 'YF23@blackwidow'
    def __init__(self,username, password):
        LOGIN_URL = 'http://127.0.0.1:8080/login/?next=/'
        self.client = requests.session()

        # Retrieve the CSRF token first
        self.client.get(LOGIN_URL)  # sets cookie
        if 'csrftoken' in self.client.cookies:
            # Django 1.6 and up
            csrftoken = self.client.cookies['csrftoken']
        else:
            # older versions
            csrftoken = self.client.cookies['csrf']
        login_data = dict(username=username, password=password, csrfmiddlewaretoken=csrftoken, next='/')
        self.client.post(LOGIN_URL, data=login_data, headers=dict(Referer=LOGIN_URL))

    def assigned_func(self):
        #######-------assigned by me--------######
        assigned_by_me_URL = 'http://127.0.0.1:8080/review/assigned-by-me/'
        r =  self.client.get(assigned_by_me_URL)
        s = r.text
        reg_match = re.search('<table.*(\n.*)+\/table>', s)
        dfs = []
        if reg_match:
            found = reg_match.group(0)
            dfs = pd.read_html(found)
        else:
            print ("couldn't fetch tms assigned by me table results")

        ########----------assigned to me-------------#########
        assigned_to_me_URL = 'http://127.0.0.1:8080/review/assigned-to-me/'
        r1 =  self.client.get(assigned_to_me_URL)
        s1 = r1.text
        reg_match1 = re.search('<table.*(\n.*)+\/table>', s1)
        if reg_match1:
            found1 = reg_match1.group(0)
            dfs1 = pd.read_html(found1)
            dfs.append(dfs1[0])
        else:
            print ("couldn't fetch tms assigned to me table results")

        my_bistq_jobqueue_url = 'http://127.0.0.1:8080/bistq/jobqueue/'
        r1 =  self.client.get(my_bistq_jobqueue_url)
        s1 = r1.text
        reg_match1 = re.search('<table.*(\n.*)+\/table>', s1)
        if reg_match1:
            found1 = reg_match1.group(0)
            dfs1 = pd.read_html(found1)
            for i in dfs1:
                i = i.loc[i['Username'] == Tms_task.username]
                dfs.append(i[['Job ID', 'Username','Start Time','Status','Build','Version']])
        else:
            print ("couldn't fetch tms assigned to me table results")

        return dfs
