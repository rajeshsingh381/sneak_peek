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

#OUTLOOK_FORMAT = '%m/%d/%Y %H:%M'
OUTLOOK_FORMAT = '%d/%m/%Y %H:%M'
outlook = Dispatch("Outlook.Application")
ns = outlook.GetNamespace("MAPI")

appointments = ns.GetDefaultFolder(9).Items
appointments.Sort("[Start]")
appointments.IncludeRecurrences = "True"
today = datetime.datetime.today()
begin = today.date().strftime("%m/%d/%Y")
tomorrow= datetime.timedelta( days= 7)+today
end = tomorrow.date().strftime("%m/%d/%Y")
appointments = appointments.Restrict("[Start] >= '" +begin+ "' AND [END] <= '" +end+ "'")
events={'Start':[],'Subject':[],'Duration':[]}
calcTableHeader = ['Title', 'Organizer', 'Start', 'Duration(Minutes)'];
calcTableBody = [];
for appointmentItem in appointments:
   # adate=datetime.datetime.fromtimestamp(int(a.Start))
    #print a.Start, a.Subject,a.Duration
#    events['Start'].append(a.date)
 #   events['Subject'].append(a.Subject)
  #  events['Duration'].append(a.Duration)
    row = []
    row.append(appointmentItem.Subject)
    row.append(appointmentItem.Organizer)
    row.append(appointmentItem.Start.Format(OUTLOOK_FORMAT))
    row.append(appointmentItem.Duration)
    calcTableBody.append(row)
    #calcTableBody.append(events)
print (tabulate(calcTableBody, headers=calcTableHeader));    
