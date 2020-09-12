from SimplePasswordManagerCore.SimpleEncryption import SimpleEncryptor
from SimplePasswordManagerCore.SimpleDB import SimpleDB
from PyQt5 import QtCore, QtGui, QtWidgets
from time import sleep
import webbrowser

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(569, 241)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(0, 0, 231, 31))
        self.comboBox.setObjectName("comboBox")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(250, 50, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.LoginCopyButton = QtWidgets.QPushButton(self.centralwidget)
        self.LoginCopyButton.setGeometry(QtCore.QRect(520, 50, 31, 31))
        self.LoginCopyButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("SimplePasswordManagerCore\\Icons\\ClipBoardIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.LoginCopyButton.setIcon(icon)
        self.LoginCopyButton.setIconSize(QtCore.QSize(32, 32))
        self.LoginCopyButton.setObjectName("LoginCopyButton")
        self.PasswordCopyButton = QtWidgets.QPushButton(self.centralwidget)
        self.PasswordCopyButton.setGeometry(QtCore.QRect(520, 90, 31, 31))
        self.PasswordCopyButton.setText("")
        self.PasswordCopyButton.setIcon(icon)
        self.PasswordCopyButton.setIconSize(QtCore.QSize(32, 32))
        self.PasswordCopyButton.setObjectName("PasswordCopyButton")
        self.OpenUrlButton = QtWidgets.QPushButton(self.centralwidget)
        self.OpenUrlButton.setGeometry(QtCore.QRect(520, 130, 31, 31))
        self.OpenUrlButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("SimplePasswordManagerCore\\Icons\\ArrowIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.OpenUrlButton.setIcon(icon1)
        self.OpenUrlButton.setIconSize(QtCore.QSize(32, 32))
        self.OpenUrlButton.setObjectName("OpenUrlButton")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(250, 90, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(250, 130, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.PasswordBox = QtWidgets.QLineEdit(self.centralwidget)
        self.PasswordBox.setGeometry(QtCore.QRect(310, 90, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.PasswordBox.setFont(font)
        self.PasswordBox.setText("")
        self.PasswordBox.setEchoMode(QtWidgets.QLineEdit.Password)
        self.PasswordBox.setObjectName("PasswordBox")
        self.LoginBox = QtWidgets.QLineEdit(self.centralwidget)
        self.LoginBox.setGeometry(QtCore.QRect(310, 50, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.LoginBox.setFont(font)
        self.LoginBox.setText("")
        self.LoginBox.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.LoginBox.setObjectName("LoginBox")
        self.UrlBox = QtWidgets.QLineEdit(self.centralwidget)
        self.UrlBox.setGeometry(QtCore.QRect(310, 130, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.UrlBox.setFont(font)
        self.UrlBox.setText("")
        self.UrlBox.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.UrlBox.setObjectName("UrlBox")
        self.NameBox = QtWidgets.QLineEdit(self.centralwidget)
        self.NameBox.setGeometry(QtCore.QRect(310, 10, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.NameBox.setFont(font)
        self.NameBox.setText("")
        self.NameBox.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.NameBox.setAlignment(QtCore.Qt.AlignCenter)
        self.NameBox.setObjectName("NameBox")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(250, 10, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.SaveEntryButton = QtWidgets.QPushButton(self.centralwidget)
        self.SaveEntryButton.setGeometry(QtCore.QRect(520, 10, 31, 31))
        self.SaveEntryButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("SimplePasswordManagerCore\\Icons\\SaveIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.SaveEntryButton.setIcon(icon2)
        self.SaveEntryButton.setIconSize(QtCore.QSize(32, 32))
        self.SaveEntryButton.setObjectName("SaveEntryButton")
        self.ClearClipboardBar = QtWidgets.QProgressBar(self.centralwidget)
        self.ClearClipboardBar.setGeometry(QtCore.QRect(250, 170, 301, 23))
        self.ClearClipboardBar.setMaximum(15)
        self.ClearClipboardBar.setProperty("value", 0)
        self.ClearClipboardBar.setTextVisible(False)
        self.ClearClipboardBar.setObjectName("ClearClipboardBar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 569, 21))
        self.menubar.setObjectName("menubar")
        self.menuPlik = QtWidgets.QMenu(self.menubar)
        self.menuPlik.setObjectName("menuPlik")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOtw_rz = QtWidgets.QAction(MainWindow)
        self.actionOtw_rz.setObjectName("actionOtw_rz")
        self.actionZapisz = QtWidgets.QAction(MainWindow)
        self.actionZapisz.setObjectName("actionZapisz")
        self.actionNowy = QtWidgets.QAction(MainWindow)
        self.actionNowy.setObjectName("actionNowy")
        self.actionOtw_rz_2 = QtWidgets.QAction(MainWindow)
        self.actionOtw_rz_2.setObjectName("actionOtw_rz_2")
        self.actionZapisz_2 = QtWidgets.QAction(MainWindow)
        self.actionZapisz_2.setObjectName("actionZapisz_2")
        self.actionZamknij = QtWidgets.QAction(MainWindow)
        self.actionZamknij.setObjectName("actionZamknij")
        self.actionZmie_has_o_g_wne = QtWidgets.QAction(MainWindow)
        self.actionZmie_has_o_g_wne.setObjectName("actionZmie_has_o_g_wne")
        self.menuPlik.addAction(self.actionNowy)
        self.menuPlik.addAction(self.actionOtw_rz_2)
        self.menuPlik.addAction(self.actionZapisz_2)
        self.menuPlik.addAction(self.actionZmie_has_o_g_wne)
        self.menuPlik.addAction(self.actionZamknij)
        self.menubar.addAction(self.menuPlik.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SimplePasswordManager"))
        self.label.setText(_translate("MainWindow", "Login"))
        self.label_3.setText(_translate("MainWindow", "Hasło"))
        self.label_4.setText(_translate("MainWindow", "URL"))
        self.NameBox.setPlaceholderText(_translate("MainWindow", "Wpis zostanie usunięty po zapisaniu"))
        self.label_2.setText(_translate("MainWindow", "Nazwa"))
        self.menuPlik.setTitle(_translate("MainWindow", "Plik"))
        self.actionOtw_rz.setText(_translate("MainWindow", "Otwórz"))
        self.actionZapisz.setText(_translate("MainWindow", "Zapisz"))
        self.actionNowy.setText(_translate("MainWindow", "Nowy"))
        self.actionOtw_rz_2.setText(_translate("MainWindow", "Otwórz"))
        self.actionZapisz_2.setText(_translate("MainWindow", "Zapisz"))
        self.actionZamknij.setText(_translate("MainWindow", "Zamknij"))
        self.actionZmie_has_o_g_wne.setText(_translate("MainWindow", "Zmień hasło"))

############################### Begining of non generated code ###############################
     
##############################################################################################
        self.clearClipboardThread = QtCore.QTimer()
        self.clearClipboardThread.setInterval(1000)
        self.clearClipboardThread.timeout.connect(self.reccuring_clearClipboardJob)
        self.clearClipboardThread.start()
############# this create background job ( i spent 2 hours figuring out how to make this ;-; )

        self.clipboardTimeLeft = 0
        self.clipboardNeedToClear = False

        self.LoginCopyButton.clicked.connect(self.copyLogin)
        self.PasswordCopyButton.clicked.connect(self.copyPassword)
        self.OpenUrlButton.clicked.connect(self.openUrl)

    def reccuring_clearClipboardJob(self):

        self.ClearClipboardBar.setValue(self.clipboardTimeLeft)

        if self.clipboardTimeLeft > 0: self.clipboardTimeLeft -= 1

        if self.clipboardTimeLeft == 0 and self.clipboardNeedToClear: 
            self.clipboardNeedToClear = False
            QtGui.QGuiApplication.clipboard().setText('')  
            

    def copyLogin(self):
        
        self.clipboardNeedToClear = True
        self.clipboardTimeLeft = 15
        QtGui.QGuiApplication.clipboard().setText(self.LoginBox.text())  

    def copyPassword(self):
        self.clipboardNeedToClear = True
        self.clipboardTimeLeft = 15
        QtGui.QGuiApplication.clipboard().setText(self.PasswordBox.text()) 

    def openUrl(self):
        webbrowser.open(self.UrlBox.text())
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    