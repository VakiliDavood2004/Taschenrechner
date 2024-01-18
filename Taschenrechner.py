import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QGridLayout, QPushButton, QLineEdit, QTextEdit
from PyQt5.QtGui import QFont, QKeySequence
from PyQt5.QtCore import Qt
import qdarkstyle

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('Professioneller Taschenrechner')
        self.setGeometry(100, 100, 400, 550)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        central_widget.setFocusPolicy(Qt.StrongFocus)  # Zum Empfangen von Tastaturereignissen

        vbox = QVBoxLayout()
        vbox.setSpacing(10)
        central_widget.setLayout(vbox)

        self.display = QLineEdit()
        self.display.setFont(QFont('Segoe UI', 24, QFont.Bold))
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)
        self.display.setStyleSheet("""
            QLineEdit {
                border: none;
                background-color: #282a36;
                color: #f8f8f2;
                padding: 15px;
                font-weight: bold;
            }
        """)
        vbox.addWidget(self.display)

        self.history = QTextEdit()
        self.history.setFont(QFont('Segoe UI', 12))
        self.history.setReadOnly(True)
        self.history.setStyleSheet("""
            QTextEdit {
                border: 1px solid #44475a;
                background-color: #282a36;
                color: #f8f8f2;
                padding: 10px;
            }
            QScrollBar:vertical {
                border: none;
                background: #44475a;
                width: 10px;
                margin: 0px 0 0px 0;
            }
            QScrollBar::handle:vertical {
                background: #6272a4;
                min-height: 20px;
                border-radius: 5px;
            }
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                border: none;
                background: none;
            }
        """)
        vbox.addWidget(self.history)

        grid = QGridLayout()
        grid.setSpacing(5)
        vbox.addLayout(grid)

        buttons = [
            'C', '+/-', '%', '/',
            '7', '8', '9', '*',
            '4', '5', '6', '-',
            '1', '2', '3', '+',
            '0', '.', '='
        ]

        positions = [
            (0, 0), (0, 1), (0, 2), (0, 3),
            (1, 0), (1, 1), (1, 2), (1, 3),
            (2, 0), (2, 1), (2, 2), (2, 3),
            (3, 0), (3, 1), (3, 2), (3, 3),
            (4, 0), (4, 1), (4, 2)
        ]

        self.button_map = {} # Zur Zuordnung des Buttontexts zum QPushButton-Objekt

        for position, button_text in zip(positions, buttons):
            btn = QPushButton(button_text)
            btn.setObjectName(button_text)  # Zur Erkennung im keyPressEvent
            btn.setFont(QFont('Segoe UI', 16, QFont.Bold))
            btn.clicked.connect(self.on_click)
            btn.setFocusPolicy(Qt.NoFocus)
            btn.setStyleSheet(self.get_button_style(button_text))
            grid.addWidget(btn, *position)
            self.button_map[button_text] = btn

        grid.addWidget(self.button_map['0'], 4, 0, 1, 2)

        self.show()
        text = event.text()
        key = event.key()

        if text.isdigit() or text in ['.', '+', '-', '*', '/']:
            self.display.setText(self.display.text() + text)
        elif key == Qt.Key_Enter or key == Qt.Key_Return:
            self.evaluate_expression()
        elif key == Qt.Key_Escape:
            self.display.setText('')
        elif key == Qt.Key_Backspace:
            self.display.setText(self.display.text()[:-1])
        elif key == Qt.Key_PlusMinus:
            self.on_click_keyboard('+/-')
        elif key == Qt.Key_Percent:
            self.on_click_keyboard('%')
        elif text.lower() == 'c':
            self.on_click_keyboard('C')
        else:
            super().keyPressEvent(event)

    def on_click(self):
        sender = self.sender()
        text = sender.text()
        self.handle_button_click(text)
    def on_click_keyboard(self, text):
        self.handle_button_click(text)

    def handle_button_click(self, text):
        current_display = self.display.text()

        if text == '=':
            self.evaluate_expression()
        elif text == 'C':
            self.display.setText('')
        elif text == '+/-':
            try:
                if current_display and current_display != 'Fehler':
                    if current_display[0] == '-':
                        self.display.setText(current_display[1:])
                    else:
                        self.display.setText('-' + current_display)
            except:
                self.display.setText('Fehler')
        elif text == '%':
            try:
                if current_display and current_display != 'Fehler':
                    self.display.setText(str(eval(f'{current_display} / 100')))
            except:
                self.display.setText('Fehler')
        else:
            self.display.setText(current_display + text)
        
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet())
    calc = Calculator()
    sys.exit(app.exec_())