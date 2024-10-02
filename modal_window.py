from PySide6.QtWidgets import QApplication, QDialog, QLabel, QVBoxLayout, QPushButton

class ModalDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Information")
        self.setFixedSize(300, 100)

        # 设置布局和控件
        layout = QVBoxLayout()
        label = QLabel("Extracting Embedding...", self)
        layout.addWidget(label)

        # close_button = QPushButton("关闭")
        # close_button.clicked.connect(self.accept)
        # layout.addWidget(close_button)

        self.setLayout(layout)