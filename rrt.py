from tms_assigned import Tms_task
import requests
from requests.auth import HTTPBasicAuth
import json
import pandas as pd

class showRes():
    def __init__(self):
        URL = "http://res.sonusnet.com/Web/Services/Authentication/Authenticate"
        #r = requests.post(url = URL, json={"username":'ayadav',"password":'Welcome@456'})
        r = requests.post(url = URL, json={"username":Tms_task.username,"password":Tms_task.password})
        data = r.json()
        keys = ('Resource','StartDate','EndDate')
        resource = dict.fromkeys(keys)
        sessionToken = data['sessionToken']
        userId = data['userId']

        getResources = "http://res.sonusnet.com/Web/Services/index.php/Reservations/?userId="+str(userId)

        allResources = requests.get(url = getResources,headers={'X-Booked-SessionToken':str(sessionToken), 'X-Booked-UserId':str(userId)},data={'userId':userId})
        userResourcesJSON = json.loads(allResources.content)
        userReslist = userResourcesJSON['reservations']

        for re in userReslist:
            if resource['Resource'] == None:
                resource['Resource'] = [re['resourceName']]
                resource['StartDate'] =  [re['startDate']]
                resource['EndDate'] = [re['endDate']]
            else:
                resource['Resource'].append(re['resourceName'])
                resource['StartDate'].append(re['startDate'])
                resource['EndDate'].append(['endDate'])
        dfs = pd.DataFrame.from_dict(userReslist)
        self.userResources = dfs


    def getResourcesData(self):
        return self.userResources


