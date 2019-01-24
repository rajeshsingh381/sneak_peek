from PyQt5.QtWidgets import (QApplication, QLabel, QWidget, QTableWidget, QHBoxLayout, QGridLayout, 
QTabWidget, QSizePolicy, QStyleFactory, QDialog, QTableWidgetItem)
from tms_assigned import Tms_task

class SneakPeek(QDialog):
    def __init__(self, parent=None):
        super(SneakPeek, self).__init__(parent)
        self.createTmsWidget()
        mainLayout = QHBoxLayout()
        mainLayout.addWidget(self.createTmsWidget)
        self.setLayout(mainLayout)
        self.setWindowTitle("Sneakpeek")
        self.changeStyle('Fusion ')

    def changeStyle(self, styleName):
        QApplication.setStyle(QStyleFactory.create(styleName))
        

    def createTmsWidget(self):

        tmo = Tms_task("rajesingh", "Myfri3nd5f@mi1y")
        output_df = tmo.assigned_func()
        print(output_df)
        self.createTmsWidget = QTabWidget()
        
        #self.sneakpeekWidget.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Ignored)
        tms_assigned = self.createAssignedWidget(output_df[0])
        self.createTmsWidget.addTab(tms_assigned, 'TMS Assigned by me')
        tms_assigned1 = self.createAssignedWidget(output_df[1])
        self.createTmsWidget.addTab(tms_assigned1, 'TMS Assigned to me')
    def createAssignedWidget(self, df):
        tms = QWidget()
        tabHeaderList = list(df.columns)
        tabIndexList = list(df.index)
        tableWidget = QTableWidget(len(tabIndexList), len(tabHeaderList))
        #tableWidget = QTableWidget(10, 10)
        
        tableWidget.setHorizontalHeaderLabels(tabHeaderList)
        for i in tabHeaderList:
            for j in tabIndexList:
                #print( output_df[0].loc[j,i])
                tableWidget.setItem(j,tabHeaderList.index(i), QTableWidgetItem(df.loc[j,i]))
        #print(output_df[0].loc[0, tabHeaderList[0]])
        tmshbox = QHBoxLayout()
        tmshbox.setContentsMargins(5, 5, 5, 5)
        tmshbox.addWidget(tableWidget)
        tms.setLayout(tmshbox)
        return tms



if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    dialog = SneakPeek()
    dialog.show()
    sys.exit(app.exec_())