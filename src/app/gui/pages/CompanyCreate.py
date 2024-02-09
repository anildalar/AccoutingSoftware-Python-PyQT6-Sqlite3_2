import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QComboBox,QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from lib.database import DatabaseManager  # Import your DatabaseManager class
from lib.helper import countries,countries_with_states
class CompanyCreate(QWidget):
    def __init__(self, db,previous_page):
        super().__init__()
        self.db = db
        self.previous_page = previous_page
        self.init_ui()
    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Escape:
            #QMessageBox.information(self, 'Message', 'ESC key pressed!')
            self.close()
            self.previous_page.show()
            #self.createCompanyButton()
    def init_ui(self):
        layout = QVBoxLayout()

        self.name_label = QLabel("Company Name:")
        self.name_input = QLineEdit()
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_input)
        
        self.country_label = QLabel("Country:")
        self.country_combo = QComboBox()
        self.country_combo.addItems(countries_with_states)  # Add more countries if needed
        self.country_combo.setCurrentText("Angola")  # Set default value to India
        self.country_combo.currentIndexChanged.connect(self.update_states)  # Connect signal to update states
        layout.addWidget(self.country_label)
        layout.addWidget(self.country_combo)

        self.state_label = QLabel("State:")
        self.state_combo = QComboBox()
        self.update_states()  # Populate states for the default country
        layout.addWidget(self.state_label)
        layout.addWidget(self.state_combo)
        
        self.location_label = QLabel("Location:")
        self.location_input = QLineEdit()
        layout.addWidget(self.location_label)
        layout.addWidget(self.location_input)

        create_button = QPushButton("Create")
        create_button.clicked.connect(self.create_company)
        layout.addWidget(create_button)

        self.setLayout(layout)
        self.setWindowTitle("Create Company")
    def update_states(self):
        selected_country = self.country_combo.currentText()
        states = countries_with_states.get(selected_country, [])
        self.state_combo.clear()
        self.state_combo.addItems(states)
        
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
        

