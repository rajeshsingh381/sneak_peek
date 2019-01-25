from PyQt5.QtWidgets import (QApplication, QLabel, QWidget, QTableWidget, QHBoxLayout, QGridLayout,
QTabWidget, QSizePolicy, QStyleFactory, QDialog, QTableWidgetItem, QVBoxLayout, QGroupBox, QFormLayout, QLineEdit, QPushButton)
from PyQt5 import QtCore
from tms_assigned import Tms_task
from outlook import Outlook_task

class SneakPeek(QDialog):
    my_ready_flag = 0
    username = None
    password = None
    def __init__(self, parent=None):
        super(SneakPeek, self).__init__(parent)
        mainLayout = QHBoxLayout()
        main_wid = QTabWidget()

        tms_wid = QWidget()
        outlook_wid = QWidget()

        self.createTmsWidget()
        self.createOutlookWidget()
        tmsLayout = QHBoxLayout()
        tmsLayout.addWidget(self.TmsWidget)
        tms_wid.setLayout(tmsLayout)
        outlookLayout = QHBoxLayout()
        outlookLayout.addWidget(self.OutlookWidget)
        outlook_wid.setLayout(outlookLayout)

        main_wid.addTab(tms_wid, "TMS")
        main_wid.addTab(outlook_wid, "OUTLOOK")
        mainLayout.addWidget(main_wid)
        self.setLayout(mainLayout)
        self.setWindowTitle("Sneakpeek")
        self.changeStyle('Fusion')
        self.resize(850, 400)

    def changeStyle(self, styleName):
        QApplication.setStyle(QStyleFactory.create(styleName))
        
    def createOutlookWidget(self):
        olo = Outlook_task()
        output_df = olo.getCalendarEntry()
        self.OutlookWidget = QTabWidget()
        
        outlook = QWidget()
        tabHeaderList = list(output_df.columns)
        tabIndexList = list(output_df.index)
        tableWidget = QTableWidget(len(tabIndexList), len(tabHeaderList))

        tableWidget.setHorizontalHeaderLabels(tabHeaderList)
        
        for i in tabHeaderList:
            for j in tabIndexList:
                tableWidget.setItem(j,tabHeaderList.index(i), QTableWidgetItem(str(output_df.loc[j,i])))
        
        tableWidget.resizeColumnsToContents()
        oulookhbox = QHBoxLayout()
        oulookhbox.setContentsMargins(5, 5, 5, 5)
        oulookhbox.addWidget(tableWidget)
        outlook.setLayout(oulookhbox)
        
        self.OutlookWidget.addTab(outlook, 'Outlook events')
        self.OutlookWidget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        
    def createTmsWidget(self):
        tmo = Tms_task(self.username, self.password)
        
        output_df = tmo.assigned_func()
        self.TmsWidget = QTabWidget()
        if output_df != None:
            tms_assigned = self.createAssignedWidget(output_df[0])
            self.TmsWidget.addTab(tms_assigned, 'TMS Assigned by me')
            tms_assigned1 = self.createAssignedWidget(output_df[1])
            self.TmsWidget.addTab(tms_assigned1, 'TMS Assigned to me')

    def createAssignedWidget(self, df):
        tms = QWidget()
        tabHeaderList = list(df.columns)
        tabIndexList = list(df.index)
        tableWidget = QTableWidget(len(tabIndexList), len(tabHeaderList))
        tableWidget.setHorizontalScrollBar = 0
        tableWidget.setHorizontalHeaderLabels(tabHeaderList)
        
        for i in tabHeaderList:
            for j in tabIndexList:
                tableWidget.setItem(j,tabHeaderList.index(i), QTableWidgetItem(df.loc[j,i]))

        tableWidget.resizeColumnsToContents()
        tmshbox = QHBoxLayout()
        tmshbox.setContentsMargins(5, 5, 5, 5)
        tmshbox.addWidget(tableWidget)
        tms.setLayout(tmshbox)
        return tms

class LoginD(QDialog):
    def __init__(self):
        super(LoginD, self).__init__()
        self.createFormGroupBox( )
        
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.formGroupBox)
        self.setLayout(mainLayout)
        
        self.setWindowTitle("TMS Login")
    
    def createFormGroupBox(self):
        self.formGroupBox = QGroupBox("Enter one time credentials")
        layout = QFormLayout()
        self.username = QLineEdit()
        self.password = QLineEdit()
        submit = QPushButton("Submit")
        submit.clicked.connect(self.closeEvent)
        self.password.setEchoMode(QLineEdit.Password)
        layout.addRow(QLabel("Name:"), self.username)
        layout.addRow(QLabel("Password:"), self.password)
        layout.addRow(submit)
        self.formGroupBox.setLayout(layout)
    def closeEvent(self, evnt):
        
        SneakPeek.my_ready_flag =1
        SneakPeek.username = self.username.text()
        SneakPeek.password = self.password.text()
        super(LoginD, self).setVisible(0)

    



if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    app.processEvents()

    dialog = LoginD()
    dialog.exec_()
    if SneakPeek.my_ready_flag == 1:
        dialog1 = SneakPeek()
        dialog1.show()
    
    sys.exit(app.exec_())