#from topmoudle.submodule import elem1,elem2,.....
from lib.initialSetup import import_sql,checkIfAdminRegister

from PyQt6.QtWidgets import QWidget,QLabel,QLineEdit,QApplication, QMainWindow, QPushButton, QVBoxLayout, QDialog
from PyQt6.QtGui import QIcon

from app.gui.forms.login.login import LoginForm
from app.gui.forms.register.register import RegisterForm

class LoginForm(QWidget):
    #1. Property/Variables/State
    
    #2. Constructor
    def __init__(self):
        super().__init__()# We are calling the parent constructor
        self.init_ui()
        pass
    
    def init_ui(self):
        layout = QVBoxLayout()

        label_username = QLabel('Username:')
        self.edit_username = QLineEdit()

        label_password = QLabel('Password:')
        self.edit_password = QLineEdit()
        self.edit_password.setEchoMode(QLineEdit.EchoMode.Password)

        btn_register = QPushButton('Login')
        #btn_register.clicked.connect(self.register_clicked)

        layout.addWidget(label_username)
        layout.addWidget(self.edit_username)
        layout.addWidget(label_password)
        layout.addWidget(self.edit_password)
        layout.addWidget(btn_register)

        self.setLayout(layout)
        pass
    pass
class RegisterForm(QWidget):
    #1. Property/Variables/State
    
    #2. Constructor
    def __init__(self):
        super().__init__()# We are calling the parent constructor
        self.init_ui()
        pass
    
    def init_ui(self):
        layout = QVBoxLayout()

        label_username = QLabel('Username:')
        self.edit_username = QLineEdit()

        label_password = QLabel('Password:')
        self.edit_password = QLineEdit()
        self.edit_password.setEchoMode(QLineEdit.EchoMode.Password)

        btn_register = QPushButton('Register')
        #btn_register.clicked.connect(self.register_clicked)

        layout.addWidget(label_username)
        layout.addWidget(self.edit_username)
        layout.addWidget(label_password)
        layout.addWidget(self.edit_password)
        layout.addWidget(btn_register)

        self.setLayout(layout)
        pass
    #3. Method/Function/Behaviours
    pass
#class ChildClass(ParentClass)
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        #moduleName.method(aa1,aa2)
        import_sql()
        self.init_ui()
        pass
        
    def init_ui(self):
        if checkIfAdminRegister() :
            #ceo              = ClassName()
            login_form = LoginForm()
            self.setCentralWidget(login_form)
            print('Show The Login Form')
            pass
        else:
            registration_form = RegisterForm()
            self.setCentralWidget(registration_form)
            print('Show The Registeration Form')
            pass
        
        
        pass
    

if __name__ == "__main__":
    app = QApplication([])
    main_window = MainWindow()
    main_window.show()
    main_window.showMaximized()
    main_window.setWindowTitle('OKLABS Account Software 1.0.0')
    # Set window icon
    icon = QIcon("./src/assets/icon.png")  # Replace with the path to your icon file
    main_window.setWindowIcon(icon)
    app.exec()
