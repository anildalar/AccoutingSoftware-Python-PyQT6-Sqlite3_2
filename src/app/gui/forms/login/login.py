import os
from PyQt6.QtWidgets import QApplication, QDialog
from PyQt6.uic import loadUi

#1. Class defination
class LoginForm(QDialog):
    #1. Property
    
    #2. Constructor
    def __init__(self):
        super().__init__()
        # Print the current working directory
        print("Current working directory before change:", os.getcwd())
        print(__file__)
        print(os.path.abspath(__file__))
        #path=os.getcwd()
        print(os.path.dirname(__file__))
        print("Current working directory after change", os.path.dirname(__file__))
        #path += '/src/app/gui/forms/login/login.ui'
        #loadUi(path, self)

        #self.pushButtonLogin.clicked.connect(self.on_login_button_click)

    #3. Method
    def on_login_button_click(self):
        username = self.lineEditUsername.text()
        password = self.lineEditPassword.text()

        # Add your login logic here
        print(f"Username: {username}, Password: {password}")

if __name__ == "__main__":
    app = QApplication([])
    #2. create class external object/Class instantiation
    login_form = LoginForm()
    login_form.show()
    app.exec()
