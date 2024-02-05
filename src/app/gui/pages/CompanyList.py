import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QTableWidget, QTableWidgetItem,QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QFormLayout, QGroupBox, QStackedWidget,QMessageBox
from lib.database import DatabaseManager  # Import your DatabaseManager class

class CompanyList(QWidget):
    def __init__(self, stack_widget, db):
        super().__init__()

        self.stack_widget = stack_widget
        self.db = db

        self.init_ui()

    def init_ui(self):
        layout = QFormLayout()
        # Increase the vertical spacing between rows

        create_company_button = QPushButton("Create")
        create_company_button.clicked.connect(self.createCompanyButton)
        create_company_button.setStyleSheet("background-color: #333; color: white;")
        layout.addRow(create_company_button)

        table = QTableWidget()
        table.setColumnCount(3)  # Set the number of columns
        table.setHorizontalHeaderLabels(["#", "Company Name", "Financial Year"])  # Set column headers

        print(self.db.getCompanies())
        # Example data
        data = self.db.getCompanies()

        for i, row_data in enumerate(data):
            table.insertRow(i)
            for j, item in enumerate(row_data):
                table.setItem(i, j, QTableWidgetItem(item))

        layout.addWidget(table)
        
        group_box = QGroupBox("Company List Page")
        group_box.setLayout(layout)

        main_layout = QVBoxLayout(self)
        main_layout.addWidget(group_box)  # Center the widget
        self.setStyleSheet("background-color: #D9D9D9;")  # Set the background color

    def createCompanyButton(self):
        print("Hi")
        pass
