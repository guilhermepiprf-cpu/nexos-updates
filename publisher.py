import sys
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QPushButton,
    QLabel,
    QFileDialog,
    QLineEdit,
    QTextEdit,
    QFrame
)
from PyQt6.QtCore import Qt


class NexosPublisher(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Nexos Publisher")
        self.resize(900, 600)

        self.setStyleSheet("""
        QWidget {
            background-color: #121212;
            color: white;
            font-family: Arial;
            font-size: 14px;
        }

        QLabel {
            color: #e5e5e5;
        }

        QLineEdit, QTextEdit {
            background-color: #1e1e1e;
            border: 1px solid #2a2a2a;
            border-radius: 8px;
            padding: 10px;
            color: white;
        }

        QPushButton {
            background-color: #0066ff;
            color: white;
            border: none;
            border-radius: 10px;
            padding: 12px;
            font-weight: bold;
        }

        QPushButton:hover {
            background-color: #1a75ff;
        }

        QPushButton:pressed {
            background-color: #0052cc;
        }

        QFrame {
            background-color: #181818;
            border-radius: 12px;
            border: 1px solid #222222;
        }
        """)

        self.file_path = ""

        layout = QVBoxLayout()

        titulo = QLabel("Nexos Publisher")
        titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        titulo.setStyleSheet("""
            font-size: 30px;
            font-weight: bold;
            padding: 15px;
            color: #4da3ff;
        """)
        layout.addWidget(titulo)

        subtitulo = QLabel("Sistema de Publicação de Atualizações")
        subtitulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(subtitulo)

        painel = QFrame()
        painel_layout = QVBoxLayout()

        self.label = QLabel("Nenhum arquivo selecionado")
        painel_layout.addWidget(self.label)

        self.select_btn = QPushButton("Selecionar Arquivo")
        self.select_btn.clicked.connect(self.select_file)
        painel_layout.addWidget(self.select_btn)

        versao_label = QLabel("Versão")
        painel_layout.addWidget(versao_label)

        self.version = QLineEdit()
        self.version.setPlaceholderText("Ex: 1.0.1")
        painel_layout.addWidget(self.version)

        descricao_label = QLabel("Descrição da Atualização")
        painel_layout.addWidget(descricao_label)

        self.changelog = QTextEdit()
        self.changelog.setPlaceholderText(
            "Digite as novidades desta atualização..."
        )
        painel_layout.addWidget(self.changelog)

        self.publish_btn = QPushButton("Publicar Atualização")
        self.publish_btn.clicked.connect(self.publish)
        painel_layout.addWidget(self.publish_btn)

        painel.setLayout(painel_layout)

        layout.addWidget(painel)

        self.status = QLabel("Pronto para publicar")
        self.status.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.status)

        self.setLayout(layout)

    def select_file(self):
        file, _ = QFileDialog.getOpenFileName(self)

        if file:
            self.file_path = file
            self.label.setText(f"Arquivo: {file}")

    def publish(self):
        if not self.file_path:
            self.status.setText("Selecione um arquivo primeiro.")
            return

        self.status.setText(
            f"Atualização {self.version.text()} preparada para publicação."
        )

        print("Arquivo:", self.file_path)
        print("Versão:", self.version.text())
        print("Descrição:", self.changelog.toPlainText())


app = QApplication(sys.argv)

window = NexosPublisher()
window.show()

sys.exit(app.exec())
