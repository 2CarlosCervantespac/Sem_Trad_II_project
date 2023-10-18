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
        tokens = get_tokens(self.ui.plainTextEdit.toPlainText())
        self.ui.tableWidget.setColumnCount(3)
        headers = ["Token", "Lexema", "#"]
        self.ui.tableWidget.setHorizontalHeaderLabels(headers)
        self.ui.tableWidget.setRowCount(len(self.tokens))

        row = 0
        for i, token in enumerate(tokens):

            self.ui.tableWidget.setItem(row, 0, QTableWidgetItem(token_types[token.type.value][1]))
            self.ui.tableWidget.setItem(row, 1, QTableWidgetItem(token.lexema))
            self.ui.tableWidget.setItem(row, 2, QTableWidgetItem(str(i + 1)))
            
            row += 1
    
    def clickSintactico(self):
        return print('Sintactico')
    
