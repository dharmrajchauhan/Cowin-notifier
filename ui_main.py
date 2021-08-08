from __future__ import annotations
import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtCore import QSize, Qt, QRect, QObject, QCoreApplication, QMetaObject, QPropertyAnimation
from PyQt5.QtWidgets import QApplication, QWidget, QProgressBar, QLabel, QTabWidget, QGridLayout, QVBoxLayout, \
QHBoxLayout, QSizePolicy, QSpacerItem, QStyle, QStyleFactory, QPushButton, QFrame, QFontDialog, QStackedWidget,\
QLineEdit, QTextBrowser, QTextEdit, QPlainTextEdit, QTableWidget, QTableWidgetItem, QToolBox, QComboBox, QAbstractItemView
from PyQt5.QtGui import QImage, QIcon, QPixmap, QPalette, QBrush, QColor, QFontDatabase, QFont, QCursor


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"Cowin Notifier")
        MainWindow.resize(1000, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(15, 21, 25);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(180, 16777215))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, -1, 0, 0)
        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"background-color: rgb(56, 75, 89);")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(15, 0, 0, 0)
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_4.addWidget(self.label)


        self.verticalLayout_2.addWidget(self.frame_4, 0, Qt.AlignTop)

        self.frame_6 = QFrame(self.frame_2)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setStyleSheet(u"background-color: rgb(24, 34, 43);")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_6)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, -1, 0, -1)
        self.frame_5 = QFrame(self.frame_6)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.slot_checker = QPushButton(self.frame_5)
        self.slot_checker.setObjectName(u"slot_checker")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.slot_checker.sizePolicy().hasHeightForWidth())
        self.slot_checker.setSizePolicy(sizePolicy1)
        self.slot_checker.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(15, 24, 31);")

        self.verticalLayout_4.addWidget(self.slot_checker)


        self.verticalLayout_3.addWidget(self.frame_5, 0, Qt.AlignTop)

        self.frame_8 = QFrame(self.frame_6)
        self.frame_8.setObjectName(u"frame_8")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy2)
        self.frame_8.setStyleSheet(u"")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_8)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(9, 9, 9, 9)
        self.frame_7 = QFrame(self.frame_8)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setStyleSheet(u"background-color: rgb(56, 75, 89);")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(10, 0, 0, 3)
        self.label_4 = QLabel(self.frame_7)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_6.addWidget(self.label_4)


        self.verticalLayout.addWidget(self.frame_7)

        self.linkdin_link = QPushButton(self.frame_8)
        self.linkdin_link.setObjectName(u"linkdin_link")
        self.linkdin_link.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(15, 24, 31);")
        icon = QIcon()
        icon.addFile(u"image/linkedin.png", QSize(), QIcon.Normal, QIcon.Off)
        self.linkdin_link.setIcon(icon)

        self.verticalLayout.addWidget(self.linkdin_link)

        self.git_link = QPushButton(self.frame_8)
        self.git_link.setObjectName(u"git_link")
        self.git_link.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(15, 24, 31);")
        icon1 = QIcon()
        icon1.addFile(u"image/github.png", QSize(), QIcon.Normal, QIcon.Off)
        self.git_link.setIcon(icon1)

        self.verticalLayout.addWidget(self.git_link)


        self.verticalLayout_3.addWidget(self.frame_8, 0, Qt.AlignBottom)


        self.verticalLayout_2.addWidget(self.frame_6)


        self.horizontalLayout_2.addWidget(self.frame_2)

        self.stackedWidget = QStackedWidget(self.frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        sizePolicy1.setHeightForWidth(self.page.sizePolicy().hasHeightForWidth())
        self.page.setSizePolicy(sizePolicy1)
        self.horizontalLayout_8 = QHBoxLayout(self.page)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, -1, -1, -1)
        self.frame_21 = QFrame(self.page)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setStyleSheet(u"background-color: rgb(15, 24, 31);")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_21)
        self.verticalLayout_19.setSpacing(4)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(-1, 0, -1, -1)
        self.label_2 = QLabel(self.frame_21)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: rgb(255,255,255);\n"
"background-color: rgb(56, 75, 89);")

        self.verticalLayout_19.addWidget(self.label_2)

        self.frame_25 = QFrame(self.frame_21)
        self.frame_25.setObjectName(u"frame_25")
        sizePolicy1.setHeightForWidth(self.frame_25.sizePolicy().hasHeightForWidth())
        self.frame_25.setSizePolicy(sizePolicy1)
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_25)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.frame_26 = QFrame(self.frame_25)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_26)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame_27 = QFrame(self.frame_26)
        self.frame_27.setObjectName(u"frame_27")
        sizePolicy1.setHeightForWidth(self.frame_27.sizePolicy().hasHeightForWidth())
        self.frame_27.setSizePolicy(sizePolicy1)
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_27)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_28 = QFrame(self.frame_27)
        self.frame_28.setObjectName(u"frame_28")
        sizePolicy.setHeightForWidth(self.frame_28.sizePolicy().hasHeightForWidth())
        self.frame_28.setSizePolicy(sizePolicy)
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_28)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.frame_29 = QFrame(self.frame_28)
        self.frame_29.setObjectName(u"frame_29")
        sizePolicy1.setHeightForWidth(self.frame_29.sizePolicy().hasHeightForWidth())
        self.frame_29.setSizePolicy(sizePolicy1)
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_29)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, -1)
        self.frame_30 = QFrame(self.frame_29)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, -1)
        self.tableWidget = QTableWidget(self.frame_30)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setBackground(QColor(255, 255, 255));
        __qtablewidgetitem.setForeground(brush);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setForeground(brush);
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setForeground(brush);
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if (self.tableWidget.rowCount() < 25):
            self.tableWidget.setRowCount(25)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(13, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(14, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(15, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(16, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(17, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(18, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(19, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(20, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(21, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(22, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(23, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(24, __qtablewidgetitem27)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy2.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy2)
        self.tableWidget.setStyleSheet(u"color:rgb(255,255,255);")
        self.tableWidget.setFrameShape(QFrame.WinPanel)
        self.tableWidget.setFrameShadow(QFrame.Raised)
        self.tableWidget.setDragEnabled(True)
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setSelectionMode(QAbstractItemView.MultiSelection)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(32)

        self.horizontalLayout_18.addWidget(self.tableWidget)


        self.horizontalLayout_17.addWidget(self.frame_30)


        self.verticalLayout_13.addWidget(self.frame_29)

        self.frame_31 = QFrame(self.frame_28)
        self.frame_31.setObjectName(u"frame_31")
        sizePolicy1.setHeightForWidth(self.frame_31.sizePolicy().hasHeightForWidth())
        self.frame_31.setSizePolicy(sizePolicy1)
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_31)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.frame_32 = QFrame(self.frame_31)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_32)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 10)
        self.frame_33 = QFrame(self.frame_32)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_33)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.frame_34 = QFrame(self.frame_33)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_34)
        self.horizontalLayout_20.setSpacing(30)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.frame_34)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(56, 75, 89);\n"
"border: 3px solid rgb(56, 75, 89);")

        self.horizontalLayout_20.addWidget(self.label_9)

        self.pincode_no = QLineEdit(self.frame_34)
        self.pincode_no.setObjectName(u"pincode_no")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.pincode_no.sizePolicy().hasHeightForWidth())
        self.pincode_no.setSizePolicy(sizePolicy3)
        self.pincode_no.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"")

        self.horizontalLayout_20.addWidget(self.pincode_no)

        self.label_10 = QLabel(self.frame_34)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(56, 75, 89);\n"
"border: 3px solid rgb(56, 75, 89);")

        self.horizontalLayout_20.addWidget(self.label_10)

        self.deos_no = QLineEdit(self.frame_34)
        self.deos_no.setObjectName(u"deos_no")
        self.deos_no.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.deos_no.setInputMethodHints(Qt.ImhDigitsOnly|Qt.ImhPreferNumbers)

        self.horizontalLayout_20.addWidget(self.deos_no)


        self.verticalLayout_15.addWidget(self.frame_34)


        self.horizontalLayout_19.addWidget(self.frame_33)


        self.verticalLayout_14.addWidget(self.frame_32)

        self.frame_35 = QFrame(self.frame_31)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_35)
        self.verticalLayout_16.setSpacing(10)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_36 = QFrame(self.frame_35)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_36)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_37 = QFrame(self.frame_36)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_37)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 10)
        self.frame_38 = QFrame(self.frame_37)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_38)
        self.horizontalLayout_21.setSpacing(20)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 10)
        self.label_11 = QLabel(self.frame_38)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(56, 75, 89);\n"
"border: 3px solid rgb(56, 75, 89);")

        self.horizontalLayout_21.addWidget(self.label_11)

        self.statename_line = QLineEdit(self.frame_38)
        self.statename_line.setObjectName(u"statename_line")
        sizePolicy3.setHeightForWidth(self.statename_line.sizePolicy().hasHeightForWidth())
        self.statename_line.setSizePolicy(sizePolicy3)
        self.statename_line.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.statename_line.setInputMethodHints(Qt.ImhNone)

        self.horizontalLayout_21.addWidget(self.statename_line)

        self.label_12 = QLabel(self.frame_38)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(56, 75, 89);\n"
"border: 3px solid rgb(56, 75, 89);\n"
"")

        self.horizontalLayout_21.addWidget(self.label_12)

        self.cityname_line = QLineEdit(self.frame_38)
        self.cityname_line.setObjectName(u"cityname_line")
        self.cityname_line.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"")

        self.horizontalLayout_21.addWidget(self.cityname_line)


        self.verticalLayout_18.addWidget(self.frame_38)

        self.frame_39 = QFrame(self.frame_37)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_39)
        self.horizontalLayout_22.setSpacing(10)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.agetype_box = QComboBox(self.frame_39)
        self.agetype_box.addItem("")
        self.agetype_box.addItem("")
        self.agetype_box.addItem("")
        self.agetype_box.setObjectName(u"agetype_box")
        sizePolicy1.setHeightForWidth(self.agetype_box.sizePolicy().hasHeightForWidth())
        self.agetype_box.setSizePolicy(sizePolicy1)
        self.agetype_box.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(56, 75, 89);\n"
"border: 3px solid rgb(56, 75, 89);")

        self.horizontalLayout_22.addWidget(self.agetype_box)

        self.vaccinetype_box = QComboBox(self.frame_39)
        self.vaccinetype_box.addItem("")
        self.vaccinetype_box.addItem("")
        self.vaccinetype_box.setObjectName(u"vaccinetype_box")
        sizePolicy1.setHeightForWidth(self.vaccinetype_box.sizePolicy().hasHeightForWidth())
        self.vaccinetype_box.setSizePolicy(sizePolicy1)
        self.vaccinetype_box.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(56, 75, 89);\n"
"border: 3px solid rgb(56, 75, 89);")

        self.horizontalLayout_22.addWidget(self.vaccinetype_box)

        self.paidtype_box = QComboBox(self.frame_39)
        self.paidtype_box.addItem("")
        self.paidtype_box.addItem("")
        self.paidtype_box.setObjectName(u"paidtype_box")
        sizePolicy1.setHeightForWidth(self.paidtype_box.sizePolicy().hasHeightForWidth())
        self.paidtype_box.setSizePolicy(sizePolicy1)
        self.paidtype_box.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(56, 75, 89);\n"
"border: 3px solid rgb(56, 75, 89);")

        self.horizontalLayout_22.addWidget(self.paidtype_box)

        self.pinsub_btn = QPushButton(self.frame_39)
        self.pinsub_btn.setObjectName(u"pinsub_btn")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.pinsub_btn.sizePolicy().hasHeightForWidth())
        self.pinsub_btn.setSizePolicy(sizePolicy4)
        self.pinsub_btn.setStyleSheet(u"color: rgb(255, 255, 255);;\n"
"border: 3px solid rgb(56, 75, 89);")

        self.horizontalLayout_22.addWidget(self.pinsub_btn)


        self.verticalLayout_18.addWidget(self.frame_39)


        self.verticalLayout_17.addWidget(self.frame_37)


        self.verticalLayout_16.addWidget(self.frame_36)


        self.verticalLayout_14.addWidget(self.frame_35)


        self.verticalLayout_13.addWidget(self.frame_31, 0, Qt.AlignBottom)


        self.horizontalLayout_16.addWidget(self.frame_28)


        self.verticalLayout_12.addWidget(self.frame_27)

        self.frame_40 = QFrame(self.frame_26)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_40)
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.pin_error = QLineEdit(self.frame_40)
        self.pin_error.setObjectName(u"pin_error")
        sizePolicy3.setHeightForWidth(self.pin_error.sizePolicy().hasHeightForWidth())
        self.pin_error.setSizePolicy(sizePolicy3)
        self.pin_error.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.pin_error.setReadOnly(True)

        self.horizontalLayout_23.addWidget(self.pin_error)


        self.verticalLayout_12.addWidget(self.frame_40, 0, Qt.AlignBottom)


        self.horizontalLayout_13.addWidget(self.frame_26)


        self.verticalLayout_19.addWidget(self.frame_25)


        self.horizontalLayout_8.addWidget(self.frame_21)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.horizontalLayout_3 = QHBoxLayout(self.page_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.gitview = QFrame(self.page_2)
        self.gitview.setObjectName(u"gitview")
        self.gitview.setFrameShape(QFrame.StyledPanel)
        self.gitview.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.gitview)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")

        self.horizontalLayout_3.addWidget(self.gitview)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.horizontalLayout_7 = QHBoxLayout(self.page_3)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.frame_9 = QFrame(self.page_3)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(50, -1, 50, -1)
        self.frame_10 = QFrame(self.frame_9)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setStyleSheet(u"")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_10)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.dj_pic = QLabel(self.frame_10)
        self.dj_pic.setObjectName(u"dj_pic")
        self.dj_pic.setStyleSheet(u"border: 5px inset rgb(56, 75, 89);\n"
"")
        self.dj_pic.setScaledContents(False)

        self.verticalLayout_5.addWidget(self.dj_pic)

        self.dj = QPushButton(self.frame_10)
        self.dj.setObjectName(u"dj")
        self.dj.setStyleSheet(u"color: rgb(255,255,255);")

        self.verticalLayout_5.addWidget(self.dj)


        self.horizontalLayout_9.addWidget(self.frame_10, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.frame_11 = QFrame(self.frame_9)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_6 = QLabel(self.frame_11)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(16777215, 378))
        self.label_6.setPixmap(QPixmap(u"image/support (5).png"))
        self.label_6.setScaledContents(False)
        self.label_6.setWordWrap(True)

        self.horizontalLayout_10.addWidget(self.label_6)


        self.horizontalLayout_9.addWidget(self.frame_11, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.frame_3 = QFrame(self.frame_9)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.rohit_pic = QLabel(self.frame_3)
        self.rohit_pic.setObjectName(u"rohit_pic")
        self.rohit_pic.setStyleSheet(u"border: 5px inset rgb(56, 75, 89);\n"
"")

        self.verticalLayout_6.addWidget(self.rohit_pic)

        self.rohit = QPushButton(self.frame_3)
        self.rohit.setObjectName(u"rohit")
        self.rohit.setStyleSheet(u"color: rgb(255,255,255);")

        self.verticalLayout_6.addWidget(self.rohit)


        self.horizontalLayout_9.addWidget(self.frame_3, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout_7.addWidget(self.frame_9)

        self.stackedWidget.addWidget(self.page_3)

        self.horizontalLayout_2.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Cowin Notifier", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.slot_checker.setText(QCoreApplication.translate("MainWindow", u"   Slots Checker   ", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Support Me", None))
        self.linkdin_link.setText(QCoreApplication.translate("MainWindow", u"   Linkdin", None))
        self.git_link.setText(QCoreApplication.translate("MainWindow", u"   Github", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Cowin Notifier", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"NAME", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"ADDRESS", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"TOTAL_DOES", None));
        ___qtablewidgetitem3 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem6 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem7 = self.tableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem8 = self.tableWidget.verticalHeaderItem(5)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"6", None));
        ___qtablewidgetitem9 = self.tableWidget.verticalHeaderItem(6)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"7", None));
        ___qtablewidgetitem10 = self.tableWidget.verticalHeaderItem(7)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"8", None));
        ___qtablewidgetitem11 = self.tableWidget.verticalHeaderItem(8)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"9", None));
        ___qtablewidgetitem12 = self.tableWidget.verticalHeaderItem(9)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"10", None));
        ___qtablewidgetitem13 = self.tableWidget.verticalHeaderItem(10)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"11", None));
        ___qtablewidgetitem14 = self.tableWidget.verticalHeaderItem(11)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"12", None));
        ___qtablewidgetitem15 = self.tableWidget.verticalHeaderItem(12)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"13", None));
        ___qtablewidgetitem16 = self.tableWidget.verticalHeaderItem(13)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"14", None));
        ___qtablewidgetitem17 = self.tableWidget.verticalHeaderItem(14)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"15", None));
        ___qtablewidgetitem18 = self.tableWidget.verticalHeaderItem(15)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"16", None));
        ___qtablewidgetitem19 = self.tableWidget.verticalHeaderItem(16)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"17", None));
        ___qtablewidgetitem20 = self.tableWidget.verticalHeaderItem(17)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"18", None));
        ___qtablewidgetitem21 = self.tableWidget.verticalHeaderItem(18)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"19", None));
        ___qtablewidgetitem22 = self.tableWidget.verticalHeaderItem(19)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"20", None));
        ___qtablewidgetitem23 = self.tableWidget.verticalHeaderItem(20)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"21", None));
        ___qtablewidgetitem24 = self.tableWidget.verticalHeaderItem(21)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"22", None));
        ___qtablewidgetitem25 = self.tableWidget.verticalHeaderItem(22)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"23", None));
        ___qtablewidgetitem26 = self.tableWidget.verticalHeaderItem(23)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"24", None));
        ___qtablewidgetitem27 = self.tableWidget.verticalHeaderItem(24)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"25", None));
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"  Pincode  ", None))
        self.pincode_no.setPlaceholderText(QCoreApplication.translate("MainWindow", u"395010", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"  Dose 1/2  ", None))
#if QT_CONFIG(whatsthis)
        self.deos_no.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Does no 1 or 2</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.deos_no.setPlaceholderText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"  State name  ", None))
        self.statename_line.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Gujarat", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"  City name  ", None))
        self.cityname_line.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Surat", None))
        self.agetype_box.setItemText(0, QCoreApplication.translate("MainWindow", u"18&Above", None))
        self.agetype_box.setItemText(1, QCoreApplication.translate("MainWindow", u"18 to 45", None))
        self.agetype_box.setItemText(2, QCoreApplication.translate("MainWindow", u"45 Above", None))

        self.vaccinetype_box.setItemText(0, QCoreApplication.translate("MainWindow", u"Covishield", None))
        self.vaccinetype_box.setItemText(1, QCoreApplication.translate("MainWindow", u"Covaxin", None))

        self.paidtype_box.setItemText(0, QCoreApplication.translate("MainWindow", u"Free", None))
        self.paidtype_box.setItemText(1, QCoreApplication.translate("MainWindow", u"Paid", None))

        self.pinsub_btn.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.pin_error.setPlaceholderText(QCoreApplication.translate("MainWindow", u"When you choose pincode do not enter statename or cityname. Use wisely", None))
        self.dj_pic.setText(QCoreApplication.translate("MainWindow", u"hii", None))
        self.dj.setText(QCoreApplication.translate("MainWindow", u"@dharmrajchauhan", None))
        self.label_6.setText("")
        self.rohit_pic.setText(QCoreApplication.translate("MainWindow", u"hii", None))
        self.rohit.setText(QCoreApplication.translate("MainWindow", u"@rohitmishra888", None))
    # retranslateUi
















