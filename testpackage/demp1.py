# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled1.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
#from os import path

from PyQt5.QtCore import ( QFile, QFileInfo, QPoint, QRect, QSettings, QSize,
        Qt, QTextStream)

#from PyQt5.Qt import QDir
#from pathlib import WindowsPath
import os.path
import re # regex
from pathlib import Path, PureWindowsPath, PurePath
import os
from os.path import isfile
from fileinput import filename

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(901, 723)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(140, 50, 151, 23))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(90, 80, 651, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(140, 180, 291, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(140, 370, 291, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(140, 220, 291, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(140, 410, 291, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_3.setGeometry(QtCore.QRect(460, 370, 291, 101))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(460, 180, 291, 101))
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(70, 140, 791, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(70, 330, 791, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(70, 490, 791, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 20, 51, 61))
        font = QtGui.QFont()
        font.setPointSize(42)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 150, 51, 61))
        font = QtGui.QFont()
        font.setPointSize(42)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(80, 340, 51, 61))
        font = QtGui.QFont()
        font.setPointSize(42)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(80, 500, 51, 61))
        font = QtGui.QFont()
        font.setPointSize(42)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(140, 30, 161, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(140, 160, 161, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(140, 350, 161, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(140, 510, 161, 16))
        self.label_8.setObjectName("label_8")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(140, 610, 141, 21))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(140, 530, 221, 17))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_3.setGeometry(QtCore.QRect(140, 550, 82, 17))
        self.radioButton_3.setObjectName("radioButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(140, 260, 291, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(140, 450, 291, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(250, 550, 501, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(250, 580, 151, 23))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(670, 640, 75, 23))
        self.pushButton_7.setObjectName("pushButton_7")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 901, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # Slots verbinden
        self.pushButton_7.clicked.connect(self.myslot1)
       



        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Pfad auswählen"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Struktur Entwicklung"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Prüfung nur XML Dateien"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Prüfung nur JPG Dateien"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Prüfung 1"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Prüfung 2"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "neues Element in Briefen einfügen"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "finde Dateien ohne Jahreszahl"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "Versionen der Dateinamen erhöhen"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "Transformation2"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "Transformation 1"))
        self.pushButton_2.setText(_translate("MainWindow", "-->"))
        self.pushButton_3.setText(_translate("MainWindow", "-->"))
        self.textBrowser_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">neues Element in Briefen einfügen</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("MainWindow", "Struktur Entwicklung"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.label.setText(_translate("MainWindow", "1."))
        self.label_2.setText(_translate("MainWindow", "2."))
        self.label_3.setText(_translate("MainWindow", "3."))
        self.label_4.setText(_translate("MainWindow", "4."))
        self.label_5.setText(_translate("MainWindow", "Startverzeichnis wählen"))
        self.label_6.setText(_translate("MainWindow", "Auswahl der Objekte"))
        self.label_7.setText(_translate("MainWindow", "Aktion wählen"))
        self.label_8.setText(_translate("MainWindow", "Ziel wählen"))
        self.radioButton.setText(_translate("MainWindow", "Dateinamen beibehalten"))
        self.radioButton_2.setText(_translate("MainWindow", "Version erhöhen"))
        self.radioButton_3.setText(_translate("MainWindow", "Pfad wähen"))
        self.pushButton_4.setText(_translate("MainWindow", "<--"))
        self.pushButton_5.setText(_translate("MainWindow", "<--"))
        self.pushButton_6.setText(_translate("MainWindow", "Pfad auswählen"))
        self.pushButton_7.setText(_translate("MainWindow", "Ausführen"))

       
    
    
    
   

    def myslot1(self, MainWindow):
        #self.textEdit.setText("Button gekclickt")
        print("myslot1 getriggert")
        
        #1 Textfeld 1 Prüfen ob ein Pfad eingeben wurde
        
        if self.lineEdit.text():
            print("lineEdit ist ausgefüllt TEXT IST FALSCH")
        else: 
            amifolder = ["beispiele","bilder","editionsdaten","html","meta","mitarbeiter","publish","temp","transfer","verschiedenes","x_archiv"] 
            self.myAmiFolderCheck(PureWindowsPath('C:/Users/seiffert/eclipse-workspace/filesystemwalker/testpackage/testdata/013'), amifolder)                                                   
            print("lineEdit ist leer TEXT IST FALSCH")    
           
        
    def myAmiFolderCheck(self, path, containsfolders):
        
        # Funktion1
        
        ##############
        #
        # editionsdaten
        #    Brief
        #        backup
        #        img-jpg
        #        img-tif
        #        19xx
        #        19xx
        #        19xx
        #        19xx
        #    Notiz
        #        backup
        #        img-jpg
        #        img-tiff
        #    tagebuch
        #        backup
        #        img-jpg
        #        img-tiff
        #    werk
        #        backup
        #        img-jpg
        #        img-tiff
        #
        #
        
        
        p=Path(path)
        print(p.iterdir())
        numberOfDirShouldBe = containsfolders.__len__() 
        numberOfDirOnFileSystem = 0
        print( p, numberOfDirShouldBe ) 
        
        for child in p.iterdir():      
            if child.name in containsfolders:
                print("Verzeichnis        " + child.name + " gefunden")
                if child.name == 'editionsdaten':
                    p1=Path(child)
                    for x in p1.iterdir():
                        print("Untererzeichnis         " + x.name + " gefunden")
                        pp=Path(x)
                        d=pp.__str__()
                        yy = os.scandir(d)
                        for file in yy:
                            f2 = os.path.join(d,file.name)  #if isfile(file):
                            if isfile(f2):
                                print("Datei gefunden            " +f2)
                                #self.myAction(f2, 1)
                                dateiname=file.name
                        
                numberOfDirOnFileSystem = numberOfDirOnFileSystem + 1 
        
        print(" ")
        print(numberOfDirShouldBe.__str__() + " Verzeichnisse erwartet")
        print(numberOfDirOnFileSystem.__str__() + " Verzeichnisse gefunden")  
        
        self.function2(dateiname, 1)
        
        return True      
    
    def function2(self, path, pruefung):
        
        print(path )
        
        ##Dateiname aus Pfad rausfriemeln
        
        
        
        
        ##REGEXPRÜFUNG###################
        # 
        # Bsp cor_roau_hgk_19040307_or_d01
        #
        string = path
        for element in string:
            m = re.match(".*(_d01)", string)
            if m:
                print(m.groups())
        
        
        self.myAction(string, 1)
        
        return True     
        
        
    def myAction(self, path, a):
        action=0
        action=a
        print("Aktion " ,action ,"auf Objekt " ,path )
    
    
    

        os.chdir("C:\\Users\\seiffert\eclipse-workspace\\filesystemwalker\\testpackage\\testdata\\013\\editionsdaten\\brief\\")
             
        #cmd = "C:\\Users\\seiffert\eclipse-workspace\\20171127_PythonDevelopment\\testpackage\\testdata\\013\\editionsdaten\\brief\\ java -jar saxon9ee.jar -s:cor_roau_hgk_19040307_or_d01.xml -xsl:Transformation_EdView_test.xsl -o:xsloutput"
      
        cmd = " java -jar saxon9ee.jar -s:cor_roau_hgk_19040307_or_d01.xml -xsl:Transformation_EdView_test.xsl -o:xsloutput"
         
        os.system(cmd)
        return True   
    
    
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

