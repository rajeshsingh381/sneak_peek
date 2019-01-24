from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QTableWidget, QHBoxLayout, QGridLayout, QTabWidget, QSizePolicy, QStyleFactory, QDialog

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
        self.createTmsWidget = QTabWidget()
        #self.sneakpeekWidget.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Ignored)
        tms = QWidget()
        tableWidget = QTableWidget(10, 10)

        tmshbox = QHBoxLayout()
        tmshbox.setContentsMargins(5, 5, 5, 5)
        tmshbox.addWidget(tableWidget)
        tms.setLayout(tmshbox)
        self.createTmsWidget.addTab(tms, 'TMS Assigned to me')


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    dialog = SneakPeek()
    dialog.show()
    sys.exit(app.exec_())
