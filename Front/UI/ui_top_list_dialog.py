# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_top_list_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QListWidget,
    QListWidgetItem, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(298, 343)
        Dialog.setStyleSheet(u"/* Style the dialog window */\n"
"QDialog{\n"
"background-color: #FFFBF5; /* \u0431\u0435\u043b\u044b\u0439 \u0431\u044d\u043a\u0433\u0440\u0430\u0443\u043d\u0434 */\n"
"}\n"
"\n"
"/* Style the label */\n"
"QLabel {\n"
"    font-size: 18px; /* larger font size */\n"
"    font-weight: bold; /* bold font */\n"
"    color: #333; /* dark gray text color */\n"
"}\n"
"\n"
"/* Style the list widget */\n"
"QListWidget {\n"
"    background-color: #fff; /* white background */\n"
"    border: 1px solid #ddd; /* thin gray border */\n"
"    border-radius: 5px; /* rounded corners */\n"
"}\n"
"\n"
"/* Style the list items */\n"
"QListWidgetItem {\n"
"    padding: 10px; /* add some padding to the list items */\n"
"    border-bottom: 1px solid #ccc; /* thin gray border between list items */\n"
"}\n"
"\n"
"QListWidgetItem:hover {\n"
"    background-color: #f0f0f0; /* light gray background on hover */\n"
"}\n"
"\n"
"QListWidgetItem:selected {\n"
"    background-color: #ccc; /* gray background on selection */\n"
"    color: #333;"
                        " /* dark gray text color on selection */\n"
"}")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(60, 20, 161, 31))
        self.label.setStyleSheet(u"QDialog{\n"
"background-color: #FFFBF5; /* \u0431\u0435\u043b\u044b\u0439 \u0431\u044d\u043a\u0433\u0440\u0430\u0443\u043d\u0434 */\n"
"}")
        self.top_list = QListWidget(Dialog)
        self.top_list.setObjectName(u"top_list")
        self.top_list.setGeometry(QRect(30, 60, 221, 261))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.top_list.setFont(font)
        self.top_list.setStyleSheet(u"QListWidget {\n"
"    /* \u043e\u0431\u0449\u0438\u0439 \u0441\u0442\u0438\u043b\u044c \u0441\u043f\u0438\u0441\u043a\u0430 */\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 5px;\n"
"    background-color: #F4EDE2;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QListWidget::item {\n"
"    /* \u0441\u0442\u0438\u043b\u044c \u043e\u0442\u0434\u0435\u043b\u044c\u043d\u043e\u0433\u043e \u044d\u043b\u0435\u043c\u0435\u043d\u0442\u0430 \u0441\u043f\u0438\u0441\u043a\u0430 */\n"
"    padding: 10px;\n"
"    border-bottom: 2px solid #ccc;\n"
"}\n"
"\n"
"QListWidget::item:hover {\n"
"    /* \u0441\u0442\u0438\u043b\u044c \u044d\u043b\u0435\u043c\u0435\u043d\u0442\u0430 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 \u043a\u0443\u0440\u0441\u043e\u0440\u0430 */\n"
"    background-color: #E6DAC3;\n"
"    border-bottom: 2px solid #aaa;\n"
"}\n"
"\n"
"QListWidget::item:selected {\n"
"    /* \u0441\u0442\u0438\u043b\u044c \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u043e\u0433\u043e \u044d\u043b\u0435\u043c"
                        "\u0435\u043d\u0442\u0430 */\n"
"    background-color: #C9C4B5;\n"
"    border-bottom: 2px solid #666;\n"
"    color: #333;\n"
"}\n"
"\n"
"QListWidget::item:selected:hover {\n"
"    /* \u0441\u0442\u0438\u043b\u044c \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u043e\u0433\u043e \u044d\u043b\u0435\u043c\u0435\u043d\u0442\u0430 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 \u043a\u0443\u0440\u0441\u043e\u0440\u0430 */\n"
"    background-color: #B3A892;\n"
"    border-bottom: 2px solid #444;\n"
"    color: #222;\n"
"}\n"
"")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u041b\u0443\u0447\u0448\u0438\u0435 \u0438\u0433\u0440\u043e\u043a\u0438", None))
    # retranslateUi

