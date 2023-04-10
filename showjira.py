from tms_assigned import Tms_task
from jira import JIRA
import pandas as pd
from dumper import dump

class ShowJIRA():
    def __init__(self):
        jira = JIRA(basic_auth=(Tms_task.username, Tms_task.password),options = {'server': 'https://jira.sonusnet.com'}) 

        keys = ('Summary','ID')
        myJira = dict.fromkeys(keys)
        all_issues = jira.search_issues('assignee=currentuser() AND status=OPEN') 

        for issue in all_issues:
            if myJira['Summary'] == None and myJira['ID']==None:
                myJira['Summary'] = [issue.fields.summary]
                myJira['ID'] = [issue]
            else:
                myJira['Summary'].append( issue.fields.summary)
                myJira['ID'].append(issue)

        self.issue = pd.DataFrame.from_dict(myJira)

    def getIssuDat(self):
        return self.issue

