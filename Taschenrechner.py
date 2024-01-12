import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QGridLayout, QPushButton, QLineEdit, QTextEdit
from PyQt5.QtGui import QFont, QKeySequence
from PyQt5.QtCore import Qt
import qdarkstyle

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        
        
        
        
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet())
    calc = Calculator()
    sys.exit(app.exec_())