# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'secondW.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SeconWindow(object):
    def setupUi(self, SeconWindow):
        SeconWindow.setObjectName("SeconWindow")
        SeconWindow.resize(800, 191)
        self.centralwidget = QtWidgets.QWidget(SeconWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 30, 781, 81))
        self.tableWidget.setBaseSize(QtCore.QSize(100, 100))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(710, 120, 75, 23))
        self.pushButton_7.setObjectName("pushButton_7")
        SeconWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SeconWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        SeconWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SeconWindow)
        self.statusbar.setObjectName("statusbar")
        SeconWindow.setStatusBar(self.statusbar)

        self.retranslateUi(SeconWindow)
        QtCore.QMetaObject.connectSlotsByName(SeconWindow)
        self.pushButton_7.clicked.connect(self.get_table_content)

    def retranslateUi(self, SeconWindow):
        _translate = QtCore.QCoreApplication.translate
        SeconWindow.setWindowTitle(_translate("SeconWindow", "MainWindow"))
        self.pushButton_7.setText(_translate("SeconWindow", "PushButton"))

    def get_table_content(self):
        list_columns = []
        for item in self.tableWidget.selectedItems():
            list_columns.append(item.text())
    
    def set_data_table(self, list_column):
        cant_columns = len(list_column)
        lista_fix = []
        for i in range(0, cant_columns):
            if(not str(list_column[i]).__contains__('Unnamed:')):
                lista_fix.append(list_column[i])
        
        cant_columns = len(lista_fix)
        self.tableWidget.setColumnCount(cant_columns)
        self.tableWidget.setRowCount(1)
        #self.tableWidget.setHorizontalHeaderLabels(('test', 'test2'))
        #self.tableWidget.setColumnWidth(0, 120)
        j = 0
        for i in lista_fix:
            self.tableWidget.setItem(0, j, QtWidgets.QTableWidgetItem(str(i)))
            j += 1
            
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SeconWindow = QtWidgets.QMainWindow()
    ui = Ui_SeconWindow()
    ui.setupUi(SeconWindow)
    SeconWindow.show()
    sys.exit(app.exec_())
