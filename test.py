import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
    def initUI(self):
        self.setGeometry(100, 100, 400, 300)
        self.setWindowTitle('Key Press Example')
        
    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_C:
            QMessageBox.information(self, 'Message', 'C key pressed!')
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())
