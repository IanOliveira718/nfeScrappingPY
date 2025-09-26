import sys
from services.pdfReader import extractAllPdfs
from services.archivesReader import readAllPdfArchives

from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit,
    QPushButton, QFileDialog, QHBoxLayout, QMessageBox
)

class MinhaInterface(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Interface de Geração")
        self.setMinimumWidth(500)

        layout = QVBoxLayout()

        # Pasta 1
        layout.addWidget(QLabel("Caminho da Pasta 1:"))
        self.pasta1_input = QLineEdit()
        botao_pasta1 = QPushButton("Selecionar")
        botao_pasta1.clicked.connect(lambda: self.selecionar_pasta(self.pasta1_input))
        linha1 = QHBoxLayout()
        linha1.addWidget(self.pasta1_input)
        linha1.addWidget(botao_pasta1)
        layout.addLayout(linha1)

        # Pasta 2
        layout.addWidget(QLabel("Caminho da Pasta 2:"))
        self.pasta2_input = QLineEdit()
        botao_pasta2 = QPushButton("Selecionar")
        botao_pasta2.clicked.connect(lambda: self.selecionar_pasta(self.pasta2_input))
        linha2 = QHBoxLayout()
        linha2.addWidget(self.pasta2_input)
        linha2.addWidget(botao_pasta2)
        layout.addLayout(linha2)

        # Nome
        layout.addWidget(QLabel("Nome:"))
        self.nome_input = QLineEdit()
        layout.addWidget(self.nome_input)

        # Botão Gerar
        self.botao_gerar = QPushButton("Gerar")
        self.botao_gerar.clicked.connect(self.gerar)
        layout.addWidget(self.botao_gerar)

        self.setLayout(layout)

    def selecionar_pasta(self, input_field):
        caminho = QFileDialog.getExistingDirectory(self, "Selecionar Pasta")
        if caminho:
            input_field.setText(caminho)

    def gerar(self):
        pasta1 = self.pasta1_input.text()
        pasta2 = self.pasta2_input.text()
        nome = self.nome_input.text()

        if not pasta1 or not pasta2 or not nome:
            QMessageBox.warning(self, "Aviso", "Preencha todos os campos!")
            return

        # Aqui você coloca a lógica de geração
        print("Pasta 1:", pasta1)
        print("Pasta 2:", pasta2)
        print("Nome:", nome)
        archivesFullName = readAllPdfArchives(pasta1)
        pdfsTexts = extractAllPdfs(archivesFullName)
        #todo: regex to get all the fields
        #todo: save an excel
        print(pdfsTexts)
        QMessageBox.information(self, "Sucesso", "Dados recebidos com sucesso!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = MinhaInterface()
    janela.show()
    sys.exit(app.exec())
