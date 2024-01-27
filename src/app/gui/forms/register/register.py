from PyQt6.QtWidgets import QApplication, QDialog
from PyQt6.uic import loadUi

class RegisterForm(QDialog):
    def __init__(self):
        super().__init__()
        loadUi("register.ui", self)

        self.pushButtonRegister.clicked.connect(self.on_register_button_click)

    def on_register_button_click(self):
        username = self.lineEditUsername.text()
        password = self.lineEditPassword.text()
        confirm_password = self.lineEditConfirmPassword.text()

        # Add your registration logic here
        print(f"Username: {username}, Password: {password}, Confirm Password: {confirm_password}")

if __name__ == "__main__":
    app = QApplication([])
    register_form = RegisterForm()
    register_form.show()
    app.exec()
