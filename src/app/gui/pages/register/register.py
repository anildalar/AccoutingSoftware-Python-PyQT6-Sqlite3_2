import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QFormLayout, QGroupBox, QStackedWidget,QMessageBox
from lib.database import DatabaseManager  # Import your DatabaseManager class

class RegistrationForm(QWidget):
    def __init__(self, stack_widget, db):
        super().__init__()

        self.stack_widget = stack_widget
        self.db = db

        self.init_ui()

    def init_ui(self):
        layout = QFormLayout()

        # Registration Page Widgets
        username_label = QLabel("Username:")
        self.username_input = QLineEdit()
        layout.addRow(username_label, self.username_input)

        password_label = QLabel("Password:")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addRow(password_label, self.password_input)

        confirm_password_label = QLabel("Confirm Password:")
        self.confirm_password_input = QLineEdit()
        self.confirm_password_input.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addRow(confirm_password_label, self.confirm_password_input)

        # Increase the vertical spacing between rows
        layout.setVerticalSpacing(70)

        register_button = QPushButton("Register")
        register_button.clicked.connect(self.on_register_clicked)
        register_button.setStyleSheet("background-color: blue; color: white;")
        layout.addRow(register_button)

        group_box = QGroupBox("Registration")
        group_box.setLayout(layout)
        group_box.setFixedWidth(600)

        main_layout = QVBoxLayout(self)
        main_layout.addWidget(group_box, alignment=Qt.AlignmentFlag.AlignCenter)  # Center the widget
        self.setStyleSheet("background-color: #D9D9D9;")  # Set the background color

    def on_register_clicked(self):
        username = self.username_input.text()
        password = self.password_input.text()

        # Check if passwords match and username is not empty
        if password == self.confirm_password_input.text() and username:
            if self.db.checkIfUserExists(username):
                # Perform registration in the database
                if self.db.register_user(username, password):
                    print("Registration successful!")
                    # Show a success popup
                    QMessageBox.information(None, "Registration Success", "User registered successfully!")
                    self.stack_widget.setCurrentIndex(0)  # Switch to Login Page
                else:
                    print("Registration failed. Username might already exist.")
                pass
            else:
                # Show a success popup
                QMessageBox.information(None, "This username is already registered", "This username is already registered")
                self.stack_widget.setCurrentIndex(0)  # Switch to Login Page
                pass
            
        else:
            print("Invalid username or passwords do not match!")

