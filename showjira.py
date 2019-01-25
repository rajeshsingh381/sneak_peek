from tms_assigned import Tms_task
from jira import JIRA
import pandas as pd
import re

class ShowJIRA():
    def __init__(self):
        jira = JIRA(basic_auth=(Tms_task.username, Tms_task.password),options = {'server': 'https://jira.sonusnet.com'}) 
        all_issues = jira.search_issues('assignee=currentuser() AND status=OPEN') 
        #print(type(all_issues))
        self.issue = pd.DataFrame.from_dict(all_issues)
        #print(self.issue)

    def getIssuDat(self):
        return self.issue

#ob = ShowJIRA()
#print(ob.returndat)