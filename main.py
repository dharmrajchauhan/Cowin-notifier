# let's start a new project with a new shayri, as i do always
'''
life is unpredictable and not everything is in our control. but as long as you with right people you handle anything.

'''

from __future__ import print_function
import os
import sys
# from PyQt5.uic import loadUi
# from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtCore import QSize, Qt, QRect, QObject, QCoreApplication, QMetaObject, QPropertyAnimation, QTimer, pyqtSlot, QThread, \
pyqtSignal, QUrl
from PyQt5.QtWidgets import QApplication, QWidget, QProgressBar, QLabel, QTabWidget, QGridLayout, QVBoxLayout, \
QHBoxLayout, QSizePolicy, QSpacerItem, QStyle, QStyleFactory, QPushButton, QFrame, QFontDialog, QStackedWidget, \
QMainWindow, QMessageBox, QTableWidget, QGraphicsDropShadowEffect, QSystemTrayIcon, QMenu, qApp, QToolBox, QComboBox
from PyQt5.QtGui import QImage, QIcon, QPixmap, QPalette, QBrush, QColor, QFontDatabase, QFont, QKeySequence
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
import signal

from ui_main import Ui_MainWindow

class MainWindow(QMainWindow):
    # =============================================================================
    #     initilize a mainwindow as self
    # =============================================================================
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon('./image/syringe (3).ico'))
        
        self.ui.tableWidget.setColumnWidth(0, 250)
        self.ui.tableWidget.setColumnWidth(1, 300)
        self.ui.tableWidget.setColumnWidth(2, 100)
        
        stylesheet = "::section{color:rgb(0,0,0);}"
        self.ui.tableWidget.verticalHeader().setStyleSheet(stylesheet)
        
        stylesheet = "::section{color:rgb(0,0,0);}"
        self.ui.tableWidget.horizontalHeader().setStyleSheet(stylesheet)
        
        
        # self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        self.ui.slot_checker.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page))
        self.ui.git_link.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_2))
        self.ui.linkdin_link.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_3))
        self.ui.git_link.clicked.connect(lambda: self.github())
        self.ui.linkdin_link.clicked.connect(lambda: self.linkdin())
        self.ui.pinsub_btn.clicked.connect(lambda: self.funcationcaller())
        self.ui.dj.clicked.connect(lambda: self.djview())
        self.ui.rohit.clicked.connect(lambda: self.rohitview())
        print(self.ui.cityname_line.text(), "text")
        print(len(self.ui.cityname_line.text()), "len")
        
#     # mask detection---------------------------------------------------------------
    @pyqtSlot()
    def funcationcaller(self):
        if len(self.ui.cityname_line.text()) == 0:
            print(self.ui.cityname_line.text(), 'text1')
            print(len(self.ui.cityname_line.text()), 'len1')
            self.pin()
            return True
        else:
            print(self.ui.cityname_line.text(), 'text2')
            print(len(self.ui.cityname_line.text()), 'len2')
            self.state()
            return True

    @pyqtSlot()
    def state(self):
        from funcation3 import statecode
        statecode.searching_start(self)
    
    @pyqtSlot()    
    def pin(self):
        from funcation1 import pin_code
        pin_code.searching_start(self)
        
    @pyqtSlot()    
    def github(self):
        web = QWebEngineView(self.ui.page_2)
        web.setUrl(QUrl("https://github.com/Ubtohts/Cowin-notifier"))
        web.resize(750, 700)
        web.show()
        
    def linkdin(self):
        pixmap = QPixmap("./image/001 -copy.jpg")
        pixmap1 = QPixmap("./image/002-copy.jpg")
        pixmapd = pixmap.scaled(240,240, Qt.KeepAspectRatio)
        pixmapr = pixmap1.scaled(240,240, Qt.KeepAspectRatio)
        self.ui.dj_pic.setPixmap(pixmapd)
        self.ui.rohit_pic.setPixmap(pixmapr)
        
    @pyqtSlot()    
    def djview(self):
        web = QWebEngineView(self.ui.frame_9)
        web.setUrl(QUrl("https://www.linkedin.com/in/dharmrajchauhan"))
        web.resize(750, 700)
        web.show()
    
    def rohitview(self):
        web = QWebEngineView(self.ui.frame_9)
        web.setUrl(QUrl("https://www.linkedin.com/in/rohitmishra888"))
        web.resize(750, 700)
        web.show()
        
def sigint_handler(*args):
    """Handler for the SIGINT signal."""
    sys.stderr.write('\r')
    if QMessageBox.question(None, '', "Are you sure you want to quit?",
                            QMessageBox.Yes | QMessageBox.No,
                            QMessageBox.No) == QMessageBox.Yes:
        QApplication.quit()
            # qApp.quit()
    

if __name__ == "__main__":
    signal.signal(signal.SIGINT, sigint_handler)
    app = QApplication(sys.argv)
    window = MainWindow()
    timer = QTimer()
    timer.start(500)  # You may change this if you wish.
    timer.timeout.connect(lambda: None)  # Let the interpreter run each 500 ms.
    window.show()
    
    sys.exit(app.exec_())