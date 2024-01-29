from PyQt6.QtWidgets import QGridLayout,QWidget,QLabel,QLineEdit,QApplication, QMainWindow, QPushButton, QVBoxLayout, QDialog


class RegisterForm(QWidget):
    #1. Property/Variables/State
    
    #2. Constructor
    def __init__(self):
        super().__init__()# We are calling the parent constructor
        self.setStyleSheet("background-color:#eee")
        self.init_ui()
        pass
    
    def init_ui(self):
        layout = QVBoxLayout()

        label_username = QLabel('Username:')
        self.edit_username = QLineEdit()

        label_password = QLabel('Password:')
        self.edit_password = QLineEdit()
        self.edit_password.setEchoMode(QLineEdit.EchoMode.Password)
        
        label_cpassword = QLabel('Confirm Password:')
        self.edit_cpassword = QLineEdit()
        self.edit_cpassword.setEchoMode(QLineEdit.EchoMode.Password)

        btn_register = QPushButton('Register')
        #btn_register.clicked.connect(self.register_clicked)

        layout.addWidget(label_username)
        layout.addWidget(self.edit_username)
        layout.addWidget(label_password)
        layout.addWidget(self.edit_password)
        layout.addWidget(label_cpassword)
        layout.addWidget(self.edit_cpassword)
        layout.addWidget(btn_register)

        self.setLayout(layout)
        pass
    #3. Method/Function/Behaviours
    pass