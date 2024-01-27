from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel

class LoginPage(QMainWindow):
    def __init__(self):
        super().__init__()

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout(self.central_widget)
        layout.addWidget(QLabel("This is the Login Page"))
        
        # Additional widgets and layout for the login page can be added here

class RegisterPage(QMainWindow):
    def __init__(self):
        super().__init__()

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout(self.central_widget)
        layout.addWidget(QLabel("This is the Register Page"))
        
        # Additional widgets and layout for the register page can be added here

class LandingPage(QMainWindow):
    def __init__(self):
        super().__init__()

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout(self.central_widget)
        layout.addWidget(QLabel("This is the Landing Page"))
        
        # Additional widgets and layout for the landing page can be added here

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.login_page_button = QPushButton("Login Page", self)
        self.login_page_button.clicked.connect(self.show_login_page)

        self.register_page_button = QPushButton("Register Page", self)
        self.register_page_button.clicked.connect(self.show_register_page)

        self.landing_page_button = QPushButton("Landing Page", self)
        self.landing_page_button.clicked.connect(self.show_landing_page)

        layout = QVBoxLayout()
        layout.addWidget(self.login_page_button)
        layout.addWidget(self.register_page_button)
        layout.addWidget(self.landing_page_button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def show_login_page(self):
        login_page = LoginPage()
        login_page.show()

    def show_register_page(self):
        register_page = RegisterPage()
        register_page.show()

    def show_landing_page(self):
        landing_page = LandingPage()
        landing_page.show()

if __name__ == "__main__":
    app = QApplication([])
    main_window = MainWindow()
    main_window.show()
    app.exec()
