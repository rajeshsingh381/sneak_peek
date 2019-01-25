from win32com.client import Dispatch
from tabulate import tabulate
from datetime import datetime, timedelta
import pdb
import pandas as pd
class Outlook_task:
    def getCalendarEntry(self):

        OUTLOOK_FORMAT = '%d/%m/%Y %H:%M'
        outlook = Dispatch("Outlook.Application")
        ns = outlook.GetNamespace("MAPI")

        appointments = ns.GetDefaultFolder(9).Items
        appointments.Sort("[Start]")
        appointments.IncludeRecurrences = "True"
        today = datetime.now()
        begin = today.date().strftime("%d/%m/%Y")
        tomorrow=timedelta(days=10)+today

        end = tomorrow.date().strftime("%d/%m/%Y")
        appointments = appointments.Restrict("[Start] >= '" +begin+ "' AND [END] <= '" +end+ "'")
        events={'Start':[],'Subject':[],'Duration':[]}
        keys = ('Title', 'Organizer', 'Start', 'Duration(Minutes)')

        calcTable = dict.fromkeys(keys)
        for appointmentItem in appointments:
            if calcTable['Title']==None:
                calcTable['Title'] = appointmentItem.Subject
                calcTable['Organizer'] = appointmentItem.Organizer
                calcTable['Start'] = appointmentItem.Start.Format(OUTLOOK_FORMAT)
                calcTable['Duration(Minutes)'] = appointmentItem.Duration
            elif type(calcTable['Title']) == list:
                calcTable['Title'].append(appointmentItem.Subject)
                calcTable['Organizer'].append(appointmentItem.Organizer)
                calcTable['Start'].append(appointmentItem.Start.Format(OUTLOOK_FORMAT))
                calcTable['Duration(Minutes)'].append(appointmentItem.Duration)
            else:
                calcTable['Title'] = [calcTable['Title'],appointmentItem.Subject]
                calcTable['Organizer'] = [calcTable['Organizer'],appointmentItem.Organizer]
                calcTable['Start'] = [calcTable['Start'], appointmentItem.Start.Format(OUTLOOK_FORMAT)]
                calcTable['Duration(Minutes)'] = [calcTable['Duration(Minutes)'], appointmentItem.Duration]
            
        dfs = pd.DataFrame.from_dict([calcTable])

        return dfs
       