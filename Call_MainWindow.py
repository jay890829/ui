from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import MainWindow as ui
import xml.etree.ElementTree as ET
import glob
#import entry

class Main(QMainWindow, ui.Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.result_path = ""
        self.xml_save_path = ""
        self.xml_file_path = ""
        self.file_path_or_directory = ""

        self.width_of_column = 0.65
        self.area_of_column = 11.7
        self.number_of_section = 7
        self.type_of_parts = 'A'
        self.mode = 0
        

        self.setupUi(self)
        self.Save_result_path_Button.clicked.connect(self.Save_result_path_Button_Clicked)
        self.Save_xml_Button.clicked.connect(self.Save_xml_Button_Clicked)
        self.Open_xml_Button.clicked.connect(self.Open_xml_Button_Clicked)
        self.type_of_parts_input.textChanged.connect(self.type_of_parts_input_textChanged)
        self.number_of_section_input.textChanged.connect(self.number_of_section_input_textChanged)
        self.width_of_column_input.textChanged.connect(self.width_of_column_input_textChanged)
        self.area_of_column_input.textChanged.connect(self.area_of_column_input_textChanged)
        self.Cancel_Button.clicked.connect(self.close)
        self.Filemode.toggled.connect(self.mode_radio_button_toggled)
        self.Pathmode.toggled.connect(self.mode_radio_button_toggled)
        self.Choose_file_or_path_Button.clicked.connect(self.Choose_file_or_path_Button_clicked)
        self.Start_Button.clicked.connect(self.Start_Button_clicked)
        self.section7_radiobutton.toggled.connect(self.section_number_radiobutton_toggled)
        self.section8_radiobutton.toggled.connect(self.section_number_radiobutton_toggled)

        for file in glob.glob(r'*.xml'):
            item = QListWidgetItem()
            item.setText(file)
            self.File_list.addItem(item)
            self.File_list.itemDoubleClicked.connect(self.List_item_double_clicked)
    
    def List_item_double_clicked(self, item):
        filename = item.text()

        try:
            tree = ET.parse(filename)
            root = tree.getroot()
            for node in root:
                if (node.tag == "type_of_parts"):
                    self.type_of_parts = node.text
                    self.type_display.setText("種類: " + node.text)
                elif (node.tag == "width_of_column"):
                    self.width_of_column = float(node.text)
                    self.width_of_column_display.setText("寬度: " + node.text)
                elif(node.tag == "area_of_column"):
                    self.area_of_column = float(node.text)
                    self.area_of_column_display.setText("面積:" + node.text)
                elif(node.tag == "number_of_section"):
                    self.number_of_section = int(node.text)
                    self.number_of_section_display.setText(node.text + "段")
        except:
            pass

    def Open_xml_Button_Clicked(self):
        self.xml_file_path = QtWidgets.QFileDialog.getOpenFileName(self, 'Select File', filter = "*.xml")[0]
        if (self.xml_file_path == ""):
            return

        try:
            tree = ET.parse(self.xml_file_path)
            root = tree.getroot()
            for node in root:
                if (node.tag == "type_of_parts"):
                    self.type_of_parts = node.text
                    self.type_display.setText("種類: " + node.text)
                elif (node.tag == "width_of_column"):
                    self.width_of_column = float(node.text)
                    self.width_of_column_display.setText("寬度: " + node.text)
                elif(node.tag == "area_of_column"):
                    self.area_of_column = float(node.text)
                    self.area_of_column_display.setText("面積:" + node.text)
                elif(node.tag == "number_of_section"):
                    self.number_of_section = int(node.text)
                    self.number_of_section_display.setText(node.text + "段")
        except:
            pass

    def Save_result_path_Button_Clicked(self):
        self.result_path = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Folder')
        self.Save_result_path_label.setText("儲存: " + self.result_path)
        

    def Save_xml_Button_Clicked(self):
        self.xml_save_path = QtWidgets.QFileDialog.getSaveFileName(self, 'Select File', filter = "*.xml")[0]
        if (self.xml_save_path == ""):
            return

        root = ET.Element("parameters")
        type_of_parts_node = ET.SubElement(root, "type_of_parts")
        type_of_parts_node.text = str(self.type_of_parts)

        width_of_column_node = ET.SubElement(root, "width_of_column")
        width_of_column_node.text = str(self.width_of_column)

        area_of_column_node = ET.SubElement(root, "area_of_column")
        area_of_column_node.text = str(self.area_of_column)

        number_of_section_node = ET.SubElement(root, "number_of_section")
        number_of_section_node.text = str(self.number_of_section)

        tree = ET.ElementTree(root)
        tree.write(self.xml_save_path, encoding = "utf-8")
    
    def type_of_parts_input_textChanged(self):
        text = self.type_of_parts_input.text()
        if (text != ''):
            self.type_display.setText("種類: " + text)
            self.type_of_parts = text

    def width_of_column_input_textChanged(self):
        try:
            self.width_of_column = float(self.width_of_column_input.text())
            self.width_of_column_display.setText("寬度: " + self.width_of_column_input.text())
        except:
            pass

    def area_of_column_input_textChanged(self):
        try:
            self.area_of_column = float(self.area_of_column_input.text())
            self.area_of_column_display.setText("面積: " + self.area_of_column_input.text())
        except:
            pass

    def number_of_section_input_textChanged(self):
        try:
            self.number_of_section = int(self.number_of_section_input.text())
            self.number_of_section_display.setText(self.number_of_section_input.text() + "段")
        except:
            pass
        
        

    def Choose_file_or_path_Button_clicked(self):
        if (self.mode == 0):
            self.file_path_or_directory = QtWidgets.QFileDialog.getOpenFileName(self, '選擇檔案', filter = "*.dcm")[0]
            self.Open_file_path_label.setText("開啟: " + self.file_path_or_directory)
        elif (self.mode == 1):
            self.file_path_or_directory = QtWidgets.QFileDialog.getExistingDirectory(self, '選擇資料夾')
            self.Open_file_path_label.setText("開啟: " + self.file_path_or_directory)

    def mode_radio_button_toggled(self):
        if (self.Filemode.isChecked()):
            self.mode = 0
            self.Choose_file_or_path_Button.setText("選擇檔案")
        elif (self.Pathmode.isChecked()):
            self.mode = 1
            self.Choose_file_or_path_Button.setText("選擇資料夾")

    def Start_Button_clicked(self):
        if (self.mode == 0):
            entry.enter("file", self.file_path_or_directory, self.type_of_parts, self.width_of_column, self.area_of_column, self.number_of_section, self.result_path)
        else:
            entry.enter("path", self.file_path_or_directory, self.type_of_parts, self.width_of_column, self.area_of_column, self.number_of_section, self.result_path)

    def section_number_radiobutton_toggled(self):
        if (self.section7_radiobutton.isChecked()):
            self.number_of_section = 7
            self.number_of_section_display.setText("7")
        elif (self.section8_radiobutton.isChecked()):
            self.number_of_section = 8
            self.number_of_section_display.setText("8")
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())