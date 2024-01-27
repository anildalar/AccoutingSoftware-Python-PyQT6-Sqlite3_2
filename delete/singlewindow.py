from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QHBoxLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.login_page_button = QPushButton("Login Page", self)
        self.login_page_button.clicked.connect(self.load_login_page)
        self.layout.addWidget(self.login_page_button)

        self.register_page_button = QPushButton("Register Page", self)
        self.register_page_button.clicked.connect(self.load_register_page)
        self.layout.addWidget(self.register_page_button)

        self.landing_page_button = QPushButton("Landing Page", self)
        self.landing_page_button.clicked.connect(self.load_landing_page)
        self.layout.addWidget(self.landing_page_button)

        # Initially load the register page
        self.load_register_page()

    def load_login_page(self):
        self.set_current_page("Login Page")

    def load_register_page(self):
        self.set_current_page("Register Page")

        # Add registration form components
        form_layout = QVBoxLayout()

        username_label = QLabel("Username:")
        self.username_input = QLineEdit()
        form_layout.addWidget(username_label)
        form_layout.addWidget(self.username_input)

        password_label = QLabel("Password:")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)  # Hide password characters
        form_layout.addWidget(password_label)
        form_layout.addWidget(self.password_input)

        register_button = QPushButton("Register", self)
        register_button.clicked.connect(self.register)
        form_layout.addWidget(register_button)

        self.layout.addLayout(form_layout)

    def load_landing_page(self):
        self.set_current_page("Landing Page")

    def set_current_page(self, page_name):
        # Clear existing layout
        for i in reversed(range(self.layout.count())):
            self.layout.itemAt(i).widget().setParent(None)

        # Load the selected page
        if page_name == "Login Page":
            self.layout.addWidget(QLabel("This is the Login Page"))
        elif page_name == "Register Page":
            self.load_register_page()
        elif page_name == "Landing Page":
            self.layout.addWidget(QLabel("This is the Landing Page"))

    def register(self):
        # Implement registration logic here, using self.username_input.text() and self.password_input.text()
        username = self.username_input.text()
        password = self.password_input.text()
        print(f"Registering user: {username}, password: {password}")

if __name__ == "__main__":
    app = QApplication([])
    main_window = MainWindow()
    main_window.show()
    app.exec()
