# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Pokemon_Info_UI_V02FebgVo.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Pokemon_Info(object):
    def setupUi(self, Pokemon_Info):
        if not Pokemon_Info.objectName():
            Pokemon_Info.setObjectName(u"Pokemon_Info")
        Pokemon_Info.resize(960, 725)
        self.label_1 = QLabel(Pokemon_Info)
        self.label_1.setObjectName(u"label_1")
        self.label_1.setGeometry(QRect(20, 140, 341, 31))
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_1.setFont(font)
        self.label_1.setTextFormat(Qt.PlainText)
        self.label_1.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.Pokemon_ComboBox = QComboBox(Pokemon_Info)
        self.Pokemon_ComboBox.addItem("")
        self.Pokemon_ComboBox.setObjectName(u"Pokemon_ComboBox")
        self.Pokemon_ComboBox.setGeometry(QRect(20, 190, 351, 41))
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(16)
        self.Pokemon_ComboBox.setFont(font1)
        self.Search_Button = QPushButton(Pokemon_Info)
        self.Search_Button.setObjectName(u"Search_Button")
        self.Search_Button.setEnabled(True)
        self.Search_Button.setGeometry(QRect(90, 270, 201, 41))
        font2 = QFont()
        font2.setFamily(u"Arial")
        font2.setPointSize(14)
        font2.setBold(True)
        font2.setWeight(75)
        self.Search_Button.setFont(font2)
        self.Refresh_Button = QPushButton(Pokemon_Info)
        self.Refresh_Button.setObjectName(u"Refresh_Button")
        self.Refresh_Button.setEnabled(True)
        self.Refresh_Button.setGeometry(QRect(400, 640, 191, 41))
        self.Refresh_Button.setFont(font2)
        self.label_6 = QLabel(Pokemon_Info)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 690, 411, 31))
        font3 = QFont()
        font3.setFamily(u"Arial")
        font3.setPointSize(10)
        font3.setBold(True)
        font3.setItalic(True)
        font3.setWeight(75)
        self.label_6.setFont(font3)
        self.label_6.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.Desc_TextEdit = QTextEdit(Pokemon_Info)
        self.Desc_TextEdit.setObjectName(u"Desc_TextEdit")
        self.Desc_TextEdit.setGeometry(QRect(620, 310, 321, 371))
        font4 = QFont()
        font4.setFamily(u"Arial")
        font4.setPointSize(14)
        self.Desc_TextEdit.setFont(font4)
        self.Desc_TextEdit.setReadOnly(True)
        self.label_2 = QLabel(Pokemon_Info)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(620, 140, 341, 31))
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.Genus_Text = QLineEdit(Pokemon_Info)
        self.Genus_Text.setObjectName(u"Genus_Text")
        self.Genus_Text.setGeometry(QRect(620, 190, 321, 41))
        self.Genus_Text.setFont(font1)
        self.Genus_Text.setEchoMode(QLineEdit.Normal)
        self.Genus_Text.setAlignment(Qt.AlignCenter)
        self.Genus_Text.setReadOnly(True)
        self.label_5 = QLabel(Pokemon_Info)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(430, 190, 191, 41))
        font5 = QFont()
        font5.setFamily(u"Arial")
        font5.setPointSize(12)
        font5.setBold(True)
        font5.setWeight(75)
        self.label_5.setFont(font5)
        self.label_5.setTextFormat(Qt.PlainText)
        self.label_5.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.Type1_Text = QLineEdit(Pokemon_Info)
        self.Type1_Text.setObjectName(u"Type1_Text")
        self.Type1_Text.setGeometry(QRect(620, 250, 141, 41))
        self.Type1_Text.setFont(font1)
        self.Type1_Text.setEchoMode(QLineEdit.Normal)
        self.Type1_Text.setAlignment(Qt.AlignCenter)
        self.Type1_Text.setReadOnly(True)
        self.label_7 = QLabel(Pokemon_Info)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(430, 250, 191, 41))
        self.label_7.setFont(font5)
        self.label_7.setTextFormat(Qt.PlainText)
        self.label_7.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.label_8 = QLabel(Pokemon_Info)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(430, 310, 191, 41))
        self.label_8.setFont(font5)
        self.label_8.setTextFormat(Qt.PlainText)
        self.label_8.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.Type2_Text = QLineEdit(Pokemon_Info)
        self.Type2_Text.setObjectName(u"Type2_Text")
        self.Type2_Text.setGeometry(QRect(800, 250, 141, 41))
        self.Type2_Text.setFont(font1)
        self.Type2_Text.setEchoMode(QLineEdit.Normal)
        self.Type2_Text.setAlignment(Qt.AlignCenter)
        self.Type2_Text.setReadOnly(True)
        self.Pokemon_Image = QGraphicsView(Pokemon_Info)
        self.Pokemon_Image.setObjectName(u"Pokemon_Image")
        self.Pokemon_Image.setGeometry(QRect(20, 330, 351, 351))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Pokemon_Image.sizePolicy().hasHeightForWidth())
        self.Pokemon_Image.setSizePolicy(sizePolicy)
        self.Pokemon_Image.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Pokemon_Image.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Type_ComboBox = QComboBox(Pokemon_Info)
        self.Type_ComboBox.addItem("")
        self.Type_ComboBox.setObjectName(u"Type_ComboBox")
        self.Type_ComboBox.setGeometry(QRect(560, 60, 241, 41))
        self.Type_ComboBox.setFont(font1)
        self.label_3 = QLabel(Pokemon_Info)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(560, 20, 341, 31))
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.KeyWord_Text = QLineEdit(Pokemon_Info)
        self.KeyWord_Text.setObjectName(u"KeyWord_Text")
        self.KeyWord_Text.setGeometry(QRect(230, 60, 251, 41))
        self.KeyWord_Text.setFont(font1)
        self.KeyWord_Text.setEchoMode(QLineEdit.Normal)
        self.KeyWord_Text.setAlignment(Qt.AlignCenter)
        self.KeyWord_Text.setReadOnly(False)
        self.label_4 = QLabel(Pokemon_Info)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(230, 20, 341, 31))
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.label_9 = QLabel(Pokemon_Info)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(10, 110, 941, 31))
        self.label_9.setFont(font)
        self.label_9.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.label_10 = QLabel(Pokemon_Info)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(20, 30, 181, 71))
        self.label_10.setFont(font)
        self.label_10.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.Keyword_Button = QPushButton(Pokemon_Info)
        self.Keyword_Button.setObjectName(u"Keyword_Button")
        self.Keyword_Button.setEnabled(True)
        self.Keyword_Button.setGeometry(QRect(440, 60, 41, 41))
        self.Keyword_Button.setFont(font2)
        self.Keyword_Button.raise_()
        self.label_1.raise_()
        self.Pokemon_ComboBox.raise_()
        self.Search_Button.raise_()
        self.Refresh_Button.raise_()
        self.label_6.raise_()
        self.Desc_TextEdit.raise_()
        self.label_2.raise_()
        self.Genus_Text.raise_()
        self.label_5.raise_()
        self.Type1_Text.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.Type2_Text.raise_()
        self.Pokemon_Image.raise_()
        self.Type_ComboBox.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.KeyWord_Text.raise_()

        self.retranslateUi(Pokemon_Info)

        QMetaObject.connectSlotsByName(Pokemon_Info)
    # setupUi

    def retranslateUi(self, Pokemon_Info):
        Pokemon_Info.setWindowTitle(QCoreApplication.translate("Pokemon_Info", u"Pok\u00e9dex", None))
        self.label_1.setText(QCoreApplication.translate("Pokemon_Info", u"Pok\u00e9mon ID_Name: ", None))
        self.Pokemon_ComboBox.setItemText(0, QCoreApplication.translate("Pokemon_Info", u"Choose Pokemon", None))

        self.Pokemon_ComboBox.setCurrentText(QCoreApplication.translate("Pokemon_Info", u"Choose Pokemon", None))
        self.Search_Button.setText(QCoreApplication.translate("Pokemon_Info", u"Search", None))
        self.Refresh_Button.setText(QCoreApplication.translate("Pokemon_Info", u"Refresh Data", None))
        self.label_6.setText(QCoreApplication.translate("Pokemon_Info", u"Developed by WillyF", None))
        self.label_2.setText(QCoreApplication.translate("Pokemon_Info", u"Pok\u00e9mon Info: ", None))
        self.label_5.setText(QCoreApplication.translate("Pokemon_Info", u"Pok\u00e9mon Genus:", None))
        self.label_7.setText(QCoreApplication.translate("Pokemon_Info", u"Pok\u00e9mon Type:", None))
        self.label_8.setText(QCoreApplication.translate("Pokemon_Info", u"Pok\u00e9mon Desc:", None))
        self.Type_ComboBox.setItemText(0, QCoreApplication.translate("Pokemon_Info", u"All Types", None))

        self.Type_ComboBox.setCurrentText(QCoreApplication.translate("Pokemon_Info", u"All Types", None))
        self.label_3.setText(QCoreApplication.translate("Pokemon_Info", u"Type: ", None))
        self.label_4.setText(QCoreApplication.translate("Pokemon_Info", u"Name Keyword: ", None))
        self.label_9.setText(QCoreApplication.translate("Pokemon_Info", u"================================================================================================", None))
        self.label_10.setText(QCoreApplication.translate("Pokemon_Info", u"Filters: ", None))
        self.Keyword_Button.setText(QCoreApplication.translate("Pokemon_Info", u"\u279c", None))
    # retranslateUi

