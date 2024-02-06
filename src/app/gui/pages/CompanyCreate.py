import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from lib.database import DatabaseManager  # Import your DatabaseManager class

class CompanyCreate(QWidget):
    def __init__(self, db,previous_page):
        super().__init__()
        self.db = db
        self.previous_page = previous_page
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.name_label = QLabel("Company Name:")
        self.name_input = QLineEdit()
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_input)

        self.location_label = QLabel("Location:")
        self.location_input = QLineEdit()
        layout.addWidget(self.location_label)
        layout.addWidget(self.location_input)

        create_button = QPushButton("Create")
        create_button.clicked.connect(self.create_company)
        layout.addWidget(create_button)

        self.setLayout(layout)
        self.setWindowTitle("Create Company")

    def create_company(self):
        name = self.name_input.text()
        location = self.location_input.text()
        print(name)
        print(location)
        if not name or not location:
            QMessageBox.warning(self, "Warning", "Please enter both name and location.")
            return

        # Assuming db is an instance of DatabaseManager
        if self.db.saveCompany(name,location):
            QMessageBox.information(self, "Success", "Company created successfully.")
            self.hide()
            self.previous_page.reload_page()  # Reload the previous page
            self.previous_page.show()  # Show the previous page
        else:
            QMessageBox.warning(self, "Failed", "Error in inserting")
        

