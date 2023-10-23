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
        self.ui.tableWidget.setColumnCount(3)
        self.ui.tableWidget.setHorizontalHeaderLabels(["Token", "Lexema", "#"])


    def clickLexico(self):
        input_text = self.ui.plainTextEdit.toPlainText()
        tokens = get_tokens(input_text)

        # Limpia la tabla
        self.ui.tableWidget.setRowCount(0)

        for i, token in enumerate(tokens):
            row_pos = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(row_pos)

            # Muestra el lexema como el token
            self.ui.tableWidget.setItem(row_pos, 0, QTableWidgetItem(token.lexema))
            self.ui.tableWidget.setItem(row_pos, 1, QTableWidgetItem(token_types[token.type.value][1]))
            self.ui.tableWidget.setItem(row_pos, 2, QTableWidgetItem(str(i + 1)))


    
    def clickSintactico(self):
        sintactico_text = self.ui.plainTextEdit_2.toPlainText()
        # Realiza la evaluación sintáctica aquí, por ejemplo:
        if es_correcto(sintactico_text):
            message = "Texto sintácticamente correcto"
        else:
            message = "Texto sintácticamente incorrecto"
        # Muestra el mensaje en un cuadro de diálogo
        QMessageBox.information(self, "Evaluación Sintáctica", message)
        return print('Sintactico')
    

    
def es_correcto(sintactico_text):
    stack = []
    
    for char in sintactico_text:
        if char == '(':
            stack.append('(')
        elif char == ')':
            if not stack:
                return False  # Se encontró un paréntesis cerrado sin un paréntesis abierto correspondiente
            stack.pop()
    
    return len(stack) == 0