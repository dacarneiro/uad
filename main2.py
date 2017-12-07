from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot
import zipfile, os
import shutil
from random import randrange
from sys import argv, exit
from PyQt5.QtWidgets import QListWidgetItem, QListWidget, QApplication, QGroupBox, QVBoxLayout, QPushButton




def backupToZip(folder):
    # Backup the entire contents of "folder" into a ZIP file.

    folder = os.path.abspath(folder)  # make sure folder is absolute
    print(folder)
    # Figure out the filename this code should use based on
    # what files already exist.
    number = 1
    while True:
        zipFilename1 = os.path.basename(folder) + '_' + str(number)
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number = number + 1

    # TODO: Create the ZIP file.
    # Walk the entire folder tree and compress the files in each folder.
    print('Creating %s...' % (zipFilename))
    print('Done.')
    shutil.make_archive(zipFilename1, 'zip', folder)
    if os.path.exists(zipFilename):
        return 1
    return 0


def Hide(self):
    # Move the Hided to Unsused folder.


    #item1 = QtWidgets.QTableWidgetItem('Plueeegin')
    #print(self.tableWidget.horizontalHeaderItem(1).text())
    #combo1=self.tableWidget.cellWidget(0,1)
    #print(self.tableWidget.item(2,0).text())
    #print(combo1.currentText())
    #self.tableWidget = QtWidgets.QTableWidget(self.tab)
    #combo = QtWidgets.QTableWidget(self.tab)
    #self.tableWidget = QtWidgets.QTableWidget()
    print("Status")
    self.tableWidget.setCurrentCell(0, 0)
    curItem = self.tableWidget.currentItem()
    print(curItem.text())




    print("End")
    return 1

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(740, 440)
        Dialog.setMinimumSize(QtCore.QSize(740, 440))
        Dialog.setMaximumSize(QtCore.QSize(740, 440))
        Dialog.setAutoFillBackground(False)
        Dialog.setStyleSheet("border-image:url(uad.jpg);\n""")
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(0, 60, 741, 311))
        self.tabWidget.setSizeIncrement(QtCore.QSize(0, 0))
        self.tabWidget.setBaseSize(QtCore.QSize(0, 0))
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setIconSize(QtCore.QSize(16, 16))
        self.tabWidget.setMovable(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")

        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 741, 291))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)

#        self.tableWidget = QtWidgets.QTableWidget(5, 2, self)
#        self.tableWidget.move(30, 30)
#        self.tableWidget.resize(400, 300)
        for root, dirs, files in os.walk("D:\\Python\\Projetos\\UAD\\plugin"):
            plugins = files
           # print(plugins)




        item1 = QtWidgets.QTableWidgetItem('Plugin')
        #item1.setBackground(QtGui.QColor(255, 0, 0))
        self.tableWidget.setHorizontalHeaderItem(0, item1)
        self.tableWidget.setColumnWidth(0,624)
        item2 = QtWidgets.QTableWidgetItem('Status')
        #item2.setBackground(QtGui.QColor(0, 255, 0))
        self.tableWidget.setHorizontalHeaderItem(1, item2)

        combo_box_options = ["Show", "Hide"]

        root = "D:\\Python\\Projetos\\UAD\\plugin"
        listplugin = ""
        temp1 = 0
        index = 0

        for i in os.listdir(root):

            temp1 = temp1 + 1
            if os.path.isfile(os.path.join(root, i)):
                    combo = QtWidgets.QCheckBox()
                    self.tableWidget.insertRow(self.tableWidget.rowCount())
                    item = QtWidgets.QTableWidgetItem('UAD')
                    item.setText(i)
                    self.tableWidget.setItem(temp1-1, 0, item)
                    #for t in combo_box_options:
                    combo.setChecked(temp1-6)
                    self.tableWidget.setCellWidget(temp1-1, 1, combo)
                    #print(combo.checkState())
        self.tableWidget.cellWidget(1,1)
        combo = self.tableWidget.cellWidget(5, 1)
        print(combo.checkState())





        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(180, 10, 381, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(10, 396, 211, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setToolTip('Backup Plugin Folder to your Desktop')
        self.pushButton.clicked.connect(self.on_click)

        self.pushButton1 = QtWidgets.QPushButton(Dialog)
        self.pushButton1.setGeometry(QtCore.QRect(650, 396, 70, 23))
        self.pushButton1.setObjectName("pushButton")
        self.pushButton1.setToolTip('Apply')
        self.pushButton1.clicked.connect(self.on_click_Apply)
        self.pushButton1.setText("Apply")

        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(10, 420, 381, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_4.setObjectName("label_4")


        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)








    def showdialog():
        d = QDialog()
        b1 = QPushButton("ok", d)
        b1.move(50, 50)
        d.setWindowTitle("Dialog")
        d.setWindowModality(Qt.ApplicationModal)
        d.exec_()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "UAD HIDE/UNHIDE Plugins"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Currently Showed"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Currently Hided"))
        self.label_3.setText(_translate("Dialog", "UAD HIDE/UNHIDE Plugins"))
        self.pushButton.setText(_translate("Dialog", "Backup Plugin Folder to your Desktop"))
        self.pushButton1.setText(_translate("Dialog", "Apply"))
        self.label_4.setText(_translate("Dialog", " "))

    @pyqtSlot()
    def on_click(self):
        temp = 0
        result = backupToZip('D:\\Python\\Projetos\\UAD\\plugin')
        if result:
            self.label_4.setText("Backup OK!")
        if not result:
            self.label_4.setText("Backup NOK!")

    def on_click_Apply(self):
            result = Hide(self)
            if result:
                self.label_4.setText("Succeed!")
            if not result:
                self.label_4.setText("Failed!")




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

