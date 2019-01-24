#from win32com.client import Dispatch
#import datetime
#from tabulate import tabulate
 
#def getCalendarEntries(days=1):
    
    #Outlook = win32com.client.Dispatch("Outlook.Application")
 #   outlook = Dispatch("Outlook.Application")
  #  ns = outlook.GetNamespace("MAPI")
   # appointments = ns.GetDefaultFolder(9).Items
from win32com.client import Dispatch
from tabulate import tabulate
import datetime ,timedelta
import pdb
import pandas as pd
class Outlook_task:
    def getCalendarEntry(self):
        #OUTLOOK_FORMAT = '%m/%d/%Y %H:%M'
        OUTLOOK_FORMAT = '%d/%m/%Y %H:%M'
        outlook = Dispatch("Outlook.Application")
        ns = outlook.GetNamespace("MAPI")

        appointments = ns.GetDefaultFolder(9).Items
        appointments.Sort("[Start]")
        appointments.IncludeRecurrences = "True"
        today = datetime.datetime.today()
        begin = today.date().strftime("%m/%d/%Y")
        tomorrow= datetime.timedelta( days= 100)+today
        #print (tomorrow)
        end = tomorrow.date().strftime("%m/%d/%Y")
        appointments = appointments.Restrict("[Start] >= '" +begin+ "' AND [END] <= '" +end+ "'")
        events={'Start':[],'Subject':[],'Duration':[]}
        keys = ('Title', 'Organizer', 'Start', 'Duration(Minutes)')
        #print (type(keys))
        calcTable = dict.fromkeys(keys)
        #print(calcTable)
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
            
            
            #calcTableBody.append(events)
            #  print (calcTableBody)
        #print(calcTableHeader)
        #print (calcTableBody)
        #print (dict(zip(calcTableHeader,calcTableBody) ) )
        #print (calcTable)
        dfs = pd.DataFrame.from_dict(calcTable)
        print(dfs)
        return dfs
        #return  (tabulate(calcTableBody, headers=calcTableHeader));   
        
        #return calcTableBody


# def GetData():
#     getCalendarEntry()
#     #print (type(data))
    
# GetData()