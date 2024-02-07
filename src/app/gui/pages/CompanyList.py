import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import  QTableWidget, QTableWidgetItem,QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QFormLayout, QGroupBox, QStackedWidget,QMessageBox
from lib.database import DatabaseManager  # Import your DatabaseManager class

from app.gui.pages.CompanyCreate import CompanyCreate

class CompanyList(QWidget):
    
    
    def __init__(self, stack_widget, db):
        super().__init__()

        self.stack_widget = stack_widget
        self.db = db
        self.table = QTableWidget()
        self.init_ui()
        
    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_C:
            #QMessageBox.information(self, 'Message', 'C key pressed!')
            self.createCompanyButton()
            
    def init_ui(self):
        layout = QFormLayout()
        # Increase the vertical spacing between rows
        create_company_button = QLabel('<span style="background-color: #333; color: white;"><span style="text-decoration: underline;">C</span>reate</span>')
        create_company_button.setStyleSheet("color: blue;")
        create_company_button.setOpenExternalLinks(True)
        create_company_button.linkActivated.connect(self.createCompanyButton)
        layout.addWidget(create_company_button)

       
        self.table.setColumnCount(3)  # Set the number of columns
        self.table.setHorizontalHeaderLabels(["#", "Company Name", "Financial Year"])  # Set column headers

        print(self.db.getCompanies())
        # Example data
        data = self.db.getCompanies()

        for i, row_data in enumerate(data):
            self.table.insertRow(i)
            for j, item in enumerate(row_data):
                self.table.setItem(i, j, QTableWidgetItem(item))

        layout.addWidget(self.table)
        
        group_box = QGroupBox("Company List Page")
        group_box.setLayout(layout)

        main_layout = QVBoxLayout(self)
        main_layout.addWidget(group_box)  # Center the widget
        self.setStyleSheet("background-color: #D9D9D9;")  # Set the background color

    def createCompanyButton(self):
        print("Hi")
        companycreate_page = CompanyCreate(self.db,self)
        self.stack_widget.addWidget(companycreate_page)
        self.stack_widget.setCurrentWidget(companycreate_page)
        pass
    def reload_page(self):
        self.reload_table_data()

    def reload_table_data(self):
        self.table.clearContents()
        data = self.db.getCompanies()

        self.table.setRowCount(len(data))
       # for   singular   in  plural        :
        for i, row_data in enumerate(data):
            for j, item in enumerate(row_data):
                self.table.setItem(i, j, QTableWidgetItem(item))
