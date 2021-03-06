# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1024, 768)
        MainWindow.setFocusPolicy(QtCore.Qt.ClickFocus)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Save_result_path_Button = QtWidgets.QPushButton(MainWindow)
        self.Save_result_path_Button.setGeometry(QtCore.QRect(500, 590, 181, 31))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(16)
        self.Save_result_path_Button.setFont(font)
        self.Save_result_path_Button.setObjectName("Save_result_path_Button")
        self.Save_xml_Button = QtWidgets.QPushButton(MainWindow)
        self.Save_xml_Button.setGeometry(QtCore.QRect(180, 590, 121, 31))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(16)
        self.Save_xml_Button.setFont(font)
        self.Save_xml_Button.setObjectName("Save_xml_Button")
        self.Open_xml_Button = QtWidgets.QPushButton(MainWindow)
        self.Open_xml_Button.setGeometry(QtCore.QRect(40, 590, 121, 31))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(16)
        self.Open_xml_Button.setFont(font)
        self.Open_xml_Button.setObjectName("Open_xml_Button")
        self.type_of_parts_groupbox = QtWidgets.QGroupBox(MainWindow)
        self.type_of_parts_groupbox.setGeometry(QtCore.QRect(30, 30, 231, 121))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(16)
        self.type_of_parts_groupbox.setFont(font)
        self.type_of_parts_groupbox.setStyleSheet("border: 0px")
        self.type_of_parts_groupbox.setTitle("")
        self.type_of_parts_groupbox.setObjectName("type_of_parts_groupbox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.type_of_parts_groupbox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.type_of_parts_label = QtWidgets.QLabel(self.type_of_parts_groupbox)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(16)
        self.type_of_parts_label.setFont(font)
        self.type_of_parts_label.setObjectName("type_of_parts_label")
        self.verticalLayout.addWidget(self.type_of_parts_label)
        self.type_of_parts_input = QtWidgets.QLineEdit(self.type_of_parts_groupbox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.type_of_parts_input.sizePolicy().hasHeightForWidth())
        self.type_of_parts_input.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(16)
        self.type_of_parts_input.setFont(font)
        self.type_of_parts_input.setText("")
        self.type_of_parts_input.setFrame(True)
        self.type_of_parts_input.setObjectName("type_of_parts_input")
        self.verticalLayout.addWidget(self.type_of_parts_input)
        self.type_display = QtWidgets.QLabel(self.type_of_parts_groupbox)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(16)
        self.type_display.setFont(font)
        self.type_display.setObjectName("type_display")
        self.verticalLayout.addWidget(self.type_display)
        self.width_of_column_groupbox = QtWidgets.QGroupBox(MainWindow)
        self.width_of_column_groupbox.setGeometry(QtCore.QRect(30, 150, 231, 111))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(16)
        self.width_of_column_groupbox.setFont(font)
        self.width_of_column_groupbox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.width_of_column_groupbox.setStyleSheet("border: 0px")
        self.width_of_column_groupbox.setTitle("")
        self.width_of_column_groupbox.setObjectName("width_of_column_groupbox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.width_of_column_groupbox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.width_of_column_label = QtWidgets.QLabel(self.width_of_column_groupbox)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(16)
        self.width_of_column_label.setFont(font)
        self.width_of_column_label.setObjectName("width_of_column_label")
        self.verticalLayout_2.addWidget(self.width_of_column_label)
        self.width_of_column_input = QtWidgets.QLineEdit(self.width_of_column_groupbox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.width_of_column_input.sizePolicy().hasHeightForWidth())
        self.width_of_column_input.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(16)
        self.width_of_column_input.setFont(font)
        self.width_of_column_input.setText("")
        self.width_of_column_input.setFrame(False)
        self.width_of_column_input.setObjectName("width_of_column_input")
        self.verticalLayout_2.addWidget(self.width_of_column_input)
        self.width_of_column_display = QtWidgets.QLabel(self.width_of_column_groupbox)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(16)
        self.width_of_column_display.setFont(font)
        self.width_of_column_display.setObjectName("width_of_column_display")
        self.verticalLayout_2.addWidget(self.width_of_column_display)
        self.area_of_column_groupbox = QtWidgets.QGroupBox(MainWindow)
        self.area_of_column_groupbox.setGeometry(QtCore.QRect(30, 260, 231, 111))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(16)
        self.area_of_column_groupbox.setFont(font)
        self.area_of_column_groupbox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.area_of_column_groupbox.setStyleSheet("border: 0px")
        self.area_of_column_groupbox.setTitle("")
        self.area_of_column_groupbox.setObjectName("area_of_column_groupbox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.area_of_column_groupbox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.area_of_column_label = QtWidgets.QLabel(self.area_of_column_groupbox)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(16)
        self.area_of_column_label.setFont(font)
        self.area_of_column_label.setObjectName("area_of_column_label")
        self.verticalLayout_3.addWidget(self.area_of_column_label)
        self.area_of_column_input = QtWidgets.QLineEdit(self.area_of_column_groupbox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.area_of_column_input.sizePolicy().hasHeightForWidth())
        self.area_of_column_input.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(16)
        self.area_of_column_input.setFont(font)
        self.area_of_column_input.setText("")
        self.area_of_column_input.setFrame(False)
        self.area_of_column_input.setObjectName("area_of_column_input")
        self.verticalLayout_3.addWidget(self.area_of_column_input)
        self.area_of_column_display = QtWidgets.QLabel(self.area_of_column_groupbox)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(16)
        self.area_of_column_display.setFont(font)
        self.area_of_column_display.setObjectName("area_of_column_display")
        self.verticalLayout_3.addWidget(self.area_of_column_display)
        self.number_of_section_group = QtWidgets.QGroupBox(MainWindow)
        self.number_of_section_group.setGeometry(QtCore.QRect(30, 360, 321, 211))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(16)
        self.number_of_section_group.setFont(font)
        self.number_of_section_group.setStyleSheet("border: 0px")
        self.number_of_section_group.setTitle("")
        self.number_of_section_group.setObjectName("number_of_section_group")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.number_of_section_group)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.number_of_section_label = QtWidgets.QLabel(self.number_of_section_group)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(16)
        self.number_of_section_label.setFont(font)
        self.number_of_section_label.setObjectName("number_of_section_label")
        self.verticalLayout_4.addWidget(self.number_of_section_label)
        self.section7_radiobutton = QtWidgets.QRadioButton(self.number_of_section_group)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(16)
        self.section7_radiobutton.setFont(font)
        self.section7_radiobutton.setChecked(True)
        self.section7_radiobutton.setObjectName("section7_radiobutton")
        self.verticalLayout_4.addWidget(self.section7_radiobutton)
        self.section8_radiobutton = QtWidgets.QRadioButton(self.number_of_section_group)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(16)
        self.section8_radiobutton.setFont(font)
        self.section8_radiobutton.setObjectName("section8_radiobutton")
        self.verticalLayout_4.addWidget(self.section8_radiobutton)
        self.groupBox_2 = QtWidgets.QGroupBox(self.number_of_section_group)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(16)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setCheckable(False)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.number_of_section_input = QtWidgets.QLineEdit(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.number_of_section_input.sizePolicy().hasHeightForWidth())
        self.number_of_section_input.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(16)
        self.number_of_section_input.setFont(font)
        self.number_of_section_input.setText("")
        self.number_of_section_input.setObjectName("number_of_section_input")
        self.horizontalLayout.addWidget(self.number_of_section_input)
        self.number_of_section_display = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(16)
        self.number_of_section_display.setFont(font)
        self.number_of_section_display.setObjectName("number_of_section_display")
        self.horizontalLayout.addWidget(self.number_of_section_display)
        self.verticalLayout_4.addWidget(self.groupBox_2)
        self.Open_file_path_label = QtWidgets.QLabel(MainWindow)
        self.Open_file_path_label.setGeometry(QtCore.QRect(40, 640, 971, 41))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(16)
        self.Open_file_path_label.setFont(font)
        self.Open_file_path_label.setObjectName("Open_file_path_label")
        self.Start_Button = QtWidgets.QPushButton(MainWindow)
        self.Start_Button.setGeometry(QtCore.QRect(720, 590, 101, 31))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(16)
        self.Start_Button.setFont(font)
        self.Start_Button.setObjectName("Start_Button")
        self.Cancel_Button = QtWidgets.QPushButton(MainWindow)
        self.Cancel_Button.setGeometry(QtCore.QRect(850, 590, 101, 31))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(16)
        self.Cancel_Button.setFont(font)
        self.Cancel_Button.setObjectName("Cancel_Button")
        self.File_list = QtWidgets.QListWidget(MainWindow)
        self.File_list.setGeometry(QtCore.QRect(490, 200, 421, 321))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(16)
        self.File_list.setFont(font)
        self.File_list.setObjectName("File_list")
        self.Save_result_path_label = QtWidgets.QLabel(MainWindow)
        self.Save_result_path_label.setGeometry(QtCore.QRect(40, 700, 971, 41))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(16)
        self.Save_result_path_label.setFont(font)
        self.Save_result_path_label.setObjectName("Save_result_path_label")
        self.Choose_file_or_path_Button = QtWidgets.QPushButton(MainWindow)
        self.Choose_file_or_path_Button.setGeometry(QtCore.QRect(320, 590, 151, 31))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(16)
        self.Choose_file_or_path_Button.setFont(font)
        self.Choose_file_or_path_Button.setObjectName("Choose_file_or_path_Button")
        self.file_or_path_mode_groupbox = QtWidgets.QGroupBox(MainWindow)
        self.file_or_path_mode_groupbox.setGeometry(QtCore.QRect(490, 70, 161, 111))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(16)
        self.file_or_path_mode_groupbox.setFont(font)
        self.file_or_path_mode_groupbox.setStyleSheet("border: 0px")
        self.file_or_path_mode_groupbox.setTitle("")
        self.file_or_path_mode_groupbox.setObjectName("file_or_path_mode_groupbox")
        self.Filemode = QtWidgets.QRadioButton(self.file_or_path_mode_groupbox)
        self.Filemode.setGeometry(QtCore.QRect(10, 10, 151, 31))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(16)
        self.Filemode.setFont(font)
        self.Filemode.setChecked(True)
        self.Filemode.setObjectName("Filemode")
        self.Pathmode = QtWidgets.QRadioButton(self.file_or_path_mode_groupbox)
        self.Pathmode.setGeometry(QtCore.QRect(10, 50, 151, 31))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(16)
        self.Pathmode.setFont(font)
        self.Pathmode.setObjectName("Pathmode")
        self.aboutbutton = QtWidgets.QPushButton(MainWindow)
        self.aboutbutton.setGeometry(QtCore.QRect(850, 30, 131, 31))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(16)
        self.aboutbutton.setFont(font)
        self.aboutbutton.setObjectName("aboutbutton")
        self.jpg_or_not_group = QtWidgets.QGroupBox(MainWindow)
        self.jpg_or_not_group.setGeometry(QtCore.QRect(690, 60, 161, 111))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(16)
        self.jpg_or_not_group.setFont(font)
        self.jpg_or_not_group.setStyleSheet("border: 0px")
        self.jpg_or_not_group.setTitle("")
        self.jpg_or_not_group.setObjectName("jpg_or_not_group")
        self.jpgmode = QtWidgets.QRadioButton(self.jpg_or_not_group)
        self.jpgmode.setGeometry(QtCore.QRect(10, 10, 151, 41))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(16)
        self.jpgmode.setFont(font)
        self.jpgmode.setChecked(True)
        self.jpgmode.setObjectName("jpgmode")
        self.nojpgmode = QtWidgets.QRadioButton(self.jpg_or_not_group)
        self.nojpgmode.setGeometry(QtCore.QRect(10, 50, 151, 41))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(16)
        self.nojpgmode.setFont(font)
        self.nojpgmode.setObjectName("nojpgmode")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "空氣導管X光硬焊瑕疵辨識系統"))
        self.Save_result_path_Button.setText(_translate("MainWindow", "儲存檔案路徑"))
        self.Save_xml_Button.setText(_translate("MainWindow", "儲存參數"))
        self.Open_xml_Button.setText(_translate("MainWindow", "開啟參數"))
        self.type_of_parts_label.setText(_translate("MainWindow", "種類 type"))
        self.type_display.setText(_translate("MainWindow", "種類: A"))
        self.width_of_column_label.setText(_translate("MainWindow", "寬度 width"))
        self.width_of_column_display.setText(_translate("MainWindow", "寬度: 10"))
        self.area_of_column_label.setText(_translate("MainWindow", "面積 area"))
        self.area_of_column_display.setText(_translate("MainWindow", "面積: 10"))
        self.number_of_section_label.setText(_translate("MainWindow", "段數 section"))
        self.section7_radiobutton.setText(_translate("MainWindow", "7"))
        self.section8_radiobutton.setText(_translate("MainWindow", "8"))
        self.number_of_section_display.setText(_translate("MainWindow", "7段"))
        self.Open_file_path_label.setText(_translate("MainWindow", "開啟:"))
        self.Start_Button.setText(_translate("MainWindow", "開始"))
        self.Cancel_Button.setText(_translate("MainWindow", "關閉"))
        self.Save_result_path_label.setText(_translate("MainWindow", "儲存:"))
        self.Choose_file_or_path_Button.setText(_translate("MainWindow", "選擇檔案"))
        self.Filemode.setText(_translate("MainWindow", "單個檔案"))
        self.Pathmode.setText(_translate("MainWindow", "資料夾"))
        self.aboutbutton.setText(_translate("MainWindow", "開發名單"))
        self.jpgmode.setText(_translate("MainWindow", "輸出jpg"))
        self.nojpgmode.setText(_translate("MainWindow", "不輸出jpg"))
