from PySide6.QtWidgets import *
from PySide6.QtGui import *
from ui_mainwindow import Ui_MainWindow
from lexico import token_types, get_tokens
from sintactico import programa, mensajes

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #Conexion xon los botones
        self.ui.pushButton.clicked.connect(self.clickLexico)
        self.ui.pushButton_2.clicked.connect(self.clickSintactico)
        self.ui.actionOpen.triggered.connect(self.action_abrir_archivo)
        self.ui.actionSave.triggered.connect(self.action_guardar_archivo)

        self.ui.tableWidget.setColumnCount(3)
        self.ui.tableWidget.setHorizontalHeaderLabels(["Token", "Lexema", "#"])


    def clickLexico(self):
        # Obtén el texto del plainTextEdit
        input_text = self.ui.plainTextEdit.toPlainText()

        # Verifica si el plainTextEdit está vacío
        if not input_text.strip():
            QMessageBox.warning(self, 'Texto vacío', 'No hay texto para analizar.')
            return

        # Obtiene los tokens
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
        mensajes.clear()  # Limpia los mensajes previos
        programa(self.tokens)
        self.ui.plainTextEdit_2.clear()

        # Concatena todos los mensajes en una cadena
        mensajes_completos = "\n".join(mensajes)
        self.ui.plainTextEdit_2.insertPlainText(mensajes_completos)
        print(mensajes_completos)
        print(mensajes)


    def action_abrir_archivo(self):
        ubicacion = QFileDialog.getOpenFileName(
            self,
            'Abrir Archivo',
            '.',
            'TXT (*.txt)'
        )[0]

        if ubicacion:
            try:
                with open(ubicacion, 'r', encoding='utf-8') as archivo:
                    texto = archivo.read()
                    self.ui.plainTextEdit.setPlainText(texto)  # Establece el texto en el QPlainTextEdit

                QMessageBox.information(
                    self,
                    "Éxito",
                    f"El archivo se abrió correctamente: {ubicacion}"
                )
            except Exception as e:
                QMessageBox.critical(
                    self,
                    "Error",
                    f"No se pudo abrir el archivo: {str(e)}"
                )
        else:
            QMessageBox.critical(
                self,
                "Error",
                "No se seleccionó un archivo válido para abrir."
            )


    def action_guardar_archivo(self):
        ubicacion = QFileDialog.getSaveFileName(
            self,
            'Guardar Archivo',
            '.',
            'TXT (*.txt)'
        )[0]

        if ubicacion:  # Verifica si se seleccionó una ubicación válida
            texto_a_guardar = self.ui.plainTextEdit.toPlainText()  # Obtiene el texto del plainTextEdit

            try:
                with open(ubicacion, 'w', encoding='utf-8') as archivo:
                    archivo.write(texto_a_guardar)

                QMessageBox.information(
                    self,
                    "Éxito",
                    f"El archivo de texto se guardó en: {ubicacion}"
                )
            except Exception as e:
                QMessageBox.critical(
                    self,
                    "Error",
                    f"No se pudo guardar el archivo de texto en {ubicacion}: {str(e)}"
                )
        else:
            QMessageBox.critical(
                self,
                "Error",
                "No se seleccionó una ubicación válida para guardar el archivo de texto."
            )
