# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Pokemon_Info_UI_V03sxeqgT.ui'
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
        Pokemon_Info.resize(1260, 864)
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
        self.Pokemon_ComboBox.setMaxVisibleItems(14)
        self.Search_Button = QPushButton(Pokemon_Info)
        self.Search_Button.setObjectName(u"Search_Button")
        self.Search_Button.setEnabled(True)
        self.Search_Button.setGeometry(QRect(90, 410, 201, 41))
        font2 = QFont()
        font2.setFamily(u"Arial")
        font2.setPointSize(14)
        font2.setBold(True)
        font2.setWeight(75)
        self.Search_Button.setFont(font2)
        self.Refresh_Button = QPushButton(Pokemon_Info)
        self.Refresh_Button.setObjectName(u"Refresh_Button")
        self.Refresh_Button.setEnabled(True)
        self.Refresh_Button.setGeometry(QRect(400, 780, 191, 41))
        self.Refresh_Button.setFont(font2)
        self.label_6 = QLabel(Pokemon_Info)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 830, 611, 31))
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
        self.Desc_TextEdit.setGeometry(QRect(620, 350, 321, 471))
        font4 = QFont()
        font4.setFamily(u"Arial")
        font4.setPointSize(14)
        self.Desc_TextEdit.setFont(font4)
        self.Desc_TextEdit.setReadOnly(True)
        self.label_2 = QLabel(Pokemon_Info)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(430, 140, 341, 31))
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
        self.label_5.setGeometry(QRect(510, 190, 111, 41))
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
        self.Type1_Text.setGeometry(QRect(620, 270, 141, 41))
        self.Type1_Text.setFont(font1)
        self.Type1_Text.setEchoMode(QLineEdit.Normal)
        self.Type1_Text.setAlignment(Qt.AlignCenter)
        self.Type1_Text.setReadOnly(True)
        self.label_7 = QLabel(Pokemon_Info)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(510, 270, 111, 41))
        self.label_7.setFont(font5)
        self.label_7.setTextFormat(Qt.PlainText)
        self.label_7.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.label_8 = QLabel(Pokemon_Info)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(510, 350, 111, 41))
        self.label_8.setFont(font5)
        self.label_8.setTextFormat(Qt.PlainText)
        self.label_8.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.Type2_Text = QLineEdit(Pokemon_Info)
        self.Type2_Text.setObjectName(u"Type2_Text")
        self.Type2_Text.setGeometry(QRect(800, 270, 141, 41))
        self.Type2_Text.setFont(font1)
        self.Type2_Text.setEchoMode(QLineEdit.Normal)
        self.Type2_Text.setAlignment(Qt.AlignCenter)
        self.Type2_Text.setReadOnly(True)
        self.Pokemon_Image = QGraphicsView(Pokemon_Info)
        self.Pokemon_Image.setObjectName(u"Pokemon_Image")
        self.Pokemon_Image.setGeometry(QRect(20, 470, 351, 351))
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
        self.Type_ComboBox.setGeometry(QRect(700, 60, 241, 41))
        self.Type_ComboBox.setFont(font1)
        self.label_3 = QLabel(Pokemon_Info)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(700, 20, 241, 31))
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.KeyWord_Text = QLineEdit(Pokemon_Info)
        self.KeyWord_Text.setObjectName(u"KeyWord_Text")
        self.KeyWord_Text.setGeometry(QRect(370, 60, 251, 41))
        self.KeyWord_Text.setFont(font1)
        self.KeyWord_Text.setEchoMode(QLineEdit.Normal)
        self.KeyWord_Text.setAlignment(Qt.AlignCenter)
        self.KeyWord_Text.setReadOnly(False)
        self.label_4 = QLabel(Pokemon_Info)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(370, 20, 341, 31))
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.label_9 = QLabel(Pokemon_Info)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(10, 110, 1241, 31))
        self.label_9.setFont(font)
        self.label_9.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.label_10 = QLabel(Pokemon_Info)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(220, 30, 151, 71))
        self.label_10.setFont(font)
        self.label_10.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.Keyword_Button = QPushButton(Pokemon_Info)
        self.Keyword_Button.setObjectName(u"Keyword_Button")
        self.Keyword_Button.setEnabled(True)
        self.Keyword_Button.setGeometry(QRect(580, 60, 41, 41))
        self.Keyword_Button.setFont(font2)
        self.label_11 = QLabel(Pokemon_Info)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(670, 830, 581, 31))
        self.label_11.setFont(font3)
        self.label_11.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.SS_Text = QLineEdit(Pokemon_Info)
        self.SS_Text.setObjectName(u"SS_Text")
        self.SS_Text.setGeometry(QRect(1160, 190, 81, 41))
        self.SS_Text.setFont(font1)
        self.SS_Text.setEchoMode(QLineEdit.Normal)
        self.SS_Text.setAlignment(Qt.AlignCenter)
        self.SS_Text.setReadOnly(True)
        self.label_12 = QLabel(Pokemon_Info)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(970, 190, 191, 41))
        self.label_12.setFont(font5)
        self.label_12.setTextFormat(Qt.PlainText)
        self.label_12.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.Atk_Text = QLineEdit(Pokemon_Info)
        self.Atk_Text.setObjectName(u"Atk_Text")
        self.Atk_Text.setGeometry(QRect(1010, 350, 81, 41))
        self.Atk_Text.setFont(font1)
        self.Atk_Text.setEchoMode(QLineEdit.Normal)
        self.Atk_Text.setAlignment(Qt.AlignCenter)
        self.Atk_Text.setReadOnly(True)
        self.Def_Text = QLineEdit(Pokemon_Info)
        self.Def_Text.setObjectName(u"Def_Text")
        self.Def_Text.setGeometry(QRect(1130, 350, 81, 41))
        self.Def_Text.setFont(font1)
        self.Def_Text.setEchoMode(QLineEdit.Normal)
        self.Def_Text.setAlignment(Qt.AlignCenter)
        self.Def_Text.setReadOnly(True)
        self.HP_Text = QLineEdit(Pokemon_Info)
        self.HP_Text.setObjectName(u"HP_Text")
        self.HP_Text.setGeometry(QRect(1010, 270, 81, 41))
        self.HP_Text.setFont(font1)
        self.HP_Text.setEchoMode(QLineEdit.Normal)
        self.HP_Text.setAlignment(Qt.AlignCenter)
        self.HP_Text.setReadOnly(True)
        self.SpDef_Text = QLineEdit(Pokemon_Info)
        self.SpDef_Text.setObjectName(u"SpDef_Text")
        self.SpDef_Text.setGeometry(QRect(1130, 430, 81, 41))
        self.SpDef_Text.setFont(font1)
        self.SpDef_Text.setEchoMode(QLineEdit.Normal)
        self.SpDef_Text.setAlignment(Qt.AlignCenter)
        self.SpDef_Text.setReadOnly(True)
        self.SpAtk_Text = QLineEdit(Pokemon_Info)
        self.SpAtk_Text.setObjectName(u"SpAtk_Text")
        self.SpAtk_Text.setGeometry(QRect(1010, 430, 81, 41))
        self.SpAtk_Text.setFont(font1)
        self.SpAtk_Text.setEchoMode(QLineEdit.Normal)
        self.SpAtk_Text.setAlignment(Qt.AlignCenter)
        self.SpAtk_Text.setReadOnly(True)
        self.label_13 = QLabel(Pokemon_Info)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(1010, 240, 81, 31))
        font6 = QFont()
        font6.setFamily(u"Arial")
        font6.setPointSize(10)
        font6.setBold(True)
        font6.setWeight(75)
        self.label_13.setFont(font6)
        self.label_13.setTextFormat(Qt.PlainText)
        self.label_13.setAlignment(Qt.AlignCenter)
        self.label_14 = QLabel(Pokemon_Info)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(1010, 320, 81, 31))
        self.label_14.setFont(font6)
        self.label_14.setTextFormat(Qt.PlainText)
        self.label_14.setAlignment(Qt.AlignCenter)
        self.label_15 = QLabel(Pokemon_Info)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(1130, 400, 81, 31))
        self.label_15.setFont(font6)
        self.label_15.setTextFormat(Qt.PlainText)
        self.label_15.setAlignment(Qt.AlignCenter)
        self.label_17 = QLabel(Pokemon_Info)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(1130, 320, 81, 31))
        self.label_17.setFont(font6)
        self.label_17.setTextFormat(Qt.PlainText)
        self.label_17.setAlignment(Qt.AlignCenter)
        self.label_18 = QLabel(Pokemon_Info)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(1010, 400, 81, 31))
        self.label_18.setFont(font6)
        self.label_18.setTextFormat(Qt.PlainText)
        self.label_18.setAlignment(Qt.AlignCenter)
        self.Speed_Text = QLineEdit(Pokemon_Info)
        self.Speed_Text.setObjectName(u"Speed_Text")
        self.Speed_Text.setGeometry(QRect(1130, 270, 81, 41))
        self.Speed_Text.setFont(font1)
        self.Speed_Text.setEchoMode(QLineEdit.Normal)
        self.Speed_Text.setAlignment(Qt.AlignCenter)
        self.Speed_Text.setReadOnly(True)
        self.label_16 = QLabel(Pokemon_Info)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(1130, 240, 81, 31))
        self.label_16.setFont(font6)
        self.label_16.setTextFormat(Qt.PlainText)
        self.label_16.setAlignment(Qt.AlignCenter)
        self.Type2_ComboBox = QComboBox(Pokemon_Info)
        self.Type2_ComboBox.addItem("")
        self.Type2_ComboBox.setObjectName(u"Type2_ComboBox")
        self.Type2_ComboBox.setGeometry(QRect(980, 60, 241, 41))
        self.Type2_ComboBox.setFont(font1)
        self.label_19 = QLabel(Pokemon_Info)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(980, 20, 241, 31))
        self.label_19.setFont(font)
        self.label_19.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.Pic_Label = QLabel(Pokemon_Info)
        self.Pic_Label.setObjectName(u"Pic_Label")
        self.Pic_Label.setGeometry(QRect(10, 20, 181, 80))
        self.Pic_Label.setFont(font)
        self.Pic_Label.setFrameShape(QFrame.NoFrame)
        self.Pic_Label.setAlignment(Qt.AlignCenter)
        self.Forme_ComboBox = QComboBox(Pokemon_Info)
        self.Forme_ComboBox.addItem("")
        self.Forme_ComboBox.setObjectName(u"Forme_ComboBox")
        self.Forme_ComboBox.setGeometry(QRect(20, 320, 351, 41))
        self.Forme_ComboBox.setFont(font1)
        self.Forme_ComboBox.setMaxVisibleItems(14)
        self.label_20 = QLabel(Pokemon_Info)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(20, 270, 341, 31))
        self.label_20.setFont(font)
        self.label_20.setTextFormat(Qt.PlainText)
        self.label_20.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.label_21 = QLabel(Pokemon_Info)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(970, 510, 281, 41))
        self.label_21.setFont(font5)
        self.label_21.setTextFormat(Qt.PlainText)
        self.label_21.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.Counter_Table = QTableWidget(Pokemon_Info)
        self.Counter_Table.setObjectName(u"Counter_Table")
        self.Counter_Table.setGeometry(QRect(970, 560, 131, 261))
        font7 = QFont()
        font7.setFamily(u"Arial")
        font7.setPointSize(10)
        self.Counter_Table.setFont(font7)
        self.Counter_Table.setAlternatingRowColors(False)
        self.Weakness_Table = QTableWidget(Pokemon_Info)
        self.Weakness_Table.setObjectName(u"Weakness_Table")
        self.Weakness_Table.setGeometry(QRect(1110, 560, 131, 261))
        self.Weakness_Table.setFont(font7)
        self.Weakness_Table.setAlternatingRowColors(False)
        self.Pokemon_Image_Label = QLabel(Pokemon_Info)
        self.Pokemon_Image_Label.setObjectName(u"Pokemon_Image_Label")
        self.Pokemon_Image_Label.setGeometry(QRect(20, 470, 351, 351))
        self.Pokemon_Image_Label.setFont(font)
        self.Pokemon_Image_Label.setFrameShape(QFrame.NoFrame)
        self.Pokemon_Image_Label.setScaledContents(True)
        self.Pokemon_Image_Label.setAlignment(Qt.AlignCenter)
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
        self.label_11.raise_()
        self.SS_Text.raise_()
        self.label_12.raise_()
        self.Atk_Text.raise_()
        self.Def_Text.raise_()
        self.HP_Text.raise_()
        self.SpDef_Text.raise_()
        self.SpAtk_Text.raise_()
        self.label_13.raise_()
        self.label_14.raise_()
        self.label_15.raise_()
        self.label_17.raise_()
        self.label_18.raise_()
        self.Speed_Text.raise_()
        self.label_16.raise_()
        self.Type2_ComboBox.raise_()
        self.label_19.raise_()
        self.Pic_Label.raise_()
        self.Forme_ComboBox.raise_()
        self.label_20.raise_()
        self.label_21.raise_()
        self.Counter_Table.raise_()
        self.Weakness_Table.raise_()
        self.Pokemon_Image_Label.raise_()

        self.retranslateUi(Pokemon_Info)

        QMetaObject.connectSlotsByName(Pokemon_Info)
    # setupUi

    def retranslateUi(self, Pokemon_Info):
        Pokemon_Info.setWindowTitle(QCoreApplication.translate("Pokemon_Info", u"Pok\u00e9dex", None))
        self.label_1.setText(QCoreApplication.translate("Pokemon_Info", u"Pok\u00e9mon ID_Name: ", None))
        self.Pokemon_ComboBox.setItemText(0, QCoreApplication.translate("Pokemon_Info", u"Choose Pok\u00e9mon", None))

        self.Pokemon_ComboBox.setCurrentText(QCoreApplication.translate("Pokemon_Info", u"Choose Pok\u00e9mon", None))
        self.Search_Button.setText(QCoreApplication.translate("Pokemon_Info", u"Search", None))
        self.Refresh_Button.setText(QCoreApplication.translate("Pokemon_Info", u"Refresh Data", None))
        self.label_6.setText(QCoreApplication.translate("Pokemon_Info", u"Developed by WillyF", None))
        self.label_2.setText(QCoreApplication.translate("Pokemon_Info", u"Pok\u00e9mon Info: ", None))
        self.label_5.setText(QCoreApplication.translate("Pokemon_Info", u"Genus:", None))
        self.label_7.setText(QCoreApplication.translate("Pokemon_Info", u"Type:", None))
        self.label_8.setText(QCoreApplication.translate("Pokemon_Info", u"Desc:", None))
        self.Type_ComboBox.setItemText(0, QCoreApplication.translate("Pokemon_Info", u"All Types", None))

        self.Type_ComboBox.setCurrentText(QCoreApplication.translate("Pokemon_Info", u"All Types", None))
        self.label_3.setText(QCoreApplication.translate("Pokemon_Info", u"Type1: ", None))
        self.label_4.setText(QCoreApplication.translate("Pokemon_Info", u"ID_Name Keyword: ", None))
        self.label_9.setText(QCoreApplication.translate("Pokemon_Info", u"================================================================================================", None))
        self.label_10.setText(QCoreApplication.translate("Pokemon_Info", u"Filters: ", None))
        self.Keyword_Button.setText(QCoreApplication.translate("Pokemon_Info", u"\u279c", None))
        self.label_11.setText(QCoreApplication.translate("Pokemon_Info", u"Remembering Ash and Pikachu for this 26-year-journey with us!", None))
        self.SS_Text.setText("")
        self.label_12.setText(QCoreApplication.translate("Pokemon_Info", u"Species Strength:", None))
        self.Atk_Text.setText("")
        self.Def_Text.setText("")
        self.HP_Text.setText("")
        self.SpDef_Text.setText("")
        self.SpAtk_Text.setText("")
        self.label_13.setText(QCoreApplication.translate("Pokemon_Info", u"HP", None))
        self.label_14.setText(QCoreApplication.translate("Pokemon_Info", u"Atk", None))
        self.label_15.setText(QCoreApplication.translate("Pokemon_Info", u"Sp. Def", None))
        self.label_17.setText(QCoreApplication.translate("Pokemon_Info", u"Def", None))
        self.label_18.setText(QCoreApplication.translate("Pokemon_Info", u"Sp. Atk", None))
        self.Speed_Text.setText("")
        self.label_16.setText(QCoreApplication.translate("Pokemon_Info", u"Speed", None))
        self.Type2_ComboBox.setItemText(0, QCoreApplication.translate("Pokemon_Info", u"All Types", None))

        self.Type2_ComboBox.setCurrentText(QCoreApplication.translate("Pokemon_Info", u"All Types", None))
        self.label_19.setText(QCoreApplication.translate("Pokemon_Info", u"Type2: ", None))
        self.Pic_Label.setText("")
        self.Forme_ComboBox.setItemText(0, QCoreApplication.translate("Pokemon_Info", u"Choose Forme", None))

        self.Forme_ComboBox.setCurrentText(QCoreApplication.translate("Pokemon_Info", u"Choose Forme", None))
        self.label_20.setText(QCoreApplication.translate("Pokemon_Info", u"Pok\u00e9mon Forme: ", None))
        self.label_21.setText(QCoreApplication.translate("Pokemon_Info", u"Counters & Weaknesses:", None))
        self.Pokemon_Image_Label.setText("")
    # retranslateUi

