import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import  QTableWidget, QTableWidgetItem,QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QFormLayout, QGroupBox, QStackedWidget,QMessageBox
from lib.database import DatabaseManager  # Import your DatabaseManager class

from app.gui.pages.CompanyCreate import CompanyCreate
class RowWiseTabTable(QTableWidget):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    def focusNextPrevChild(self, nextChild: bool):
        currentRow = self.currentRow()
        currentColumn = self.currentColumn()
        rowCount = self.rowCount()
        columnCount = self.columnCount()

        if nextChild:
            currentRow += 1
            if currentRow >= rowCount:
                currentRow = 0
                currentColumn += 1
                if currentColumn >= columnCount:
                    currentColumn = 0
        else:
            currentRow -= 1
            if currentRow < 0:
                currentRow = rowCount - 1
                currentColumn -= 1
                if currentColumn < 0:
                    currentColumn = columnCount - 1

        self.setCurrentCell(currentRow, currentColumn)
        self.selectRow(currentRow)  # Select the entire row
        return True
    
class CompanyList(QWidget):
    
    
    def __init__(self, stack_widget, db):
        super().__init__()

        self.stack_widget = stack_widget
        self.db = db
        self.table = RowWiseTabTable()
        self.init_ui()
        
    def keyPressEvent(self, event):
        if event.modifiers() == Qt.KeyboardModifier.AltModifier and event.key() == Qt.Key.Key_C:
            self.createCompanyButton()
        elif event.key() == Qt.Key.Key_Enter or event.key() == Qt.Key.Key_Return:
            self.selectCompanyName()
            
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

        data = self.db.getCompanies()
        for i, row_data in enumerate(data):
            self.table.insertRow(i)
            for j, item in enumerate(row_data):
                cell_item = QTableWidgetItem(item)
                cell_item.setFlags(cell_item.flags() & ~Qt.ItemFlag.ItemIsEditable)  # Disable editing
                self.table.setItem(i, j, cell_item)

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
    
    def selectCompanyName(self):
        current_row = self.table.currentRow()
        company_name_item = self.table.item(current_row, 1)  # Assuming company name is in the second column
        if company_name_item:
            company_name = company_name_item.text()
            QMessageBox.warning(self, company_name, company_name)
            print("Selected company name:", company_name)
            
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
