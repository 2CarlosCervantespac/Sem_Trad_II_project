#from PySide6.QtWidgets import QMainWindow, QTableWidgetItem, QWidget, QVBoxLayout, QFont, QPlainTextEdit, QFontMetrics, QPushButton, QTableWidget
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from ui_mainwindow import Ui_MainWindow
from lexico import token_types, get_tokens

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #Conexion xon los botones
        self.ui.pushButton.clicked.connect(self.clickLexico)
        self.ui.pushButton_2.clicked.connect(self.clickSintactico)


    def clickLexico(self):
        #tokens = [get_tokens(self.ui.plainTextEdit.toPlainText())]
        tokens = get_tokens(self.ui.plainTextEdit.toPlainText())
        print(tokens)
		# Limpiar la tabla
        self.ui.tableWidget.clearContents()
        self.ui.tableWidget.setRowCount(0)

        for i in range(len(tokens)):
            

            row_pos = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(0)
            self.ui.tableWidget.setItem(0, 0, QTableWidgetItem(tokens[i].lexema))
            self.ui.tableWidget.setItem(0, 1, QTableWidgetItem(token_types[tokens[i].type.value][1]))
            self.ui.tableWidget.setItem(0, 2, QTableWidgetItem(str(tokens[i].type.value)))
    
    def clickSintactico(self):
        return print('Sintactico')
    
