#from PySide6.QtWidgets import QMainWindow, QTableWidgetItem, QWidget, QVBoxLayout, QFont, QPlainTextEdit, QFontMetrics, QPushButton, QTableWidget
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from ui_mainwindow import Ui_MainWindow
from lexico import token_types, get_tokens
from sintactico import programa

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #Conexion xon los botones
        self.ui.pushButton.clicked.connect(self.clickLexico)
        self.ui.pushButton_2.clicked.connect(self.clickSintactico)
        self.ui.tableWidget.setColumnCount(3)
        self.ui.tableWidget.setHorizontalHeaderLabels(["Token", "Lexema", "#"])


    def clickLexico(self):
        input_text = self.ui.plainTextEdit.toPlainText()
        self.tokens = get_tokens(input_text)

        # Limpia la tabla
        self.ui.tableWidget.setRowCount(0)

        for i, token in enumerate(self.tokens):
            row_pos = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(row_pos)

            # Muestra el lexema como el token
            self.ui.tableWidget.setItem(row_pos, 0, QTableWidgetItem(token.lexema))
            self.ui.tableWidget.setItem(row_pos, 1, QTableWidgetItem(token_types[token.type.value][1]))
            self.ui.tableWidget.setItem(row_pos, 2, QTableWidgetItem(str(i + 1)))

        row = 0
        for i, token in enumerate(self.tokens):

            self.ui.tableWidget.setItem(row, 0, QTableWidgetItem(token_types[token.type.value][1]))
            self.ui.tableWidget.setItem(row, 1, QTableWidgetItem(token.lexema))
            self.ui.tableWidget.setItem(row, 2, QTableWidgetItem(str(i + 1)))
            
            row += 1
    
    def clickSintactico(self):
        programa(self.tokens)
    
