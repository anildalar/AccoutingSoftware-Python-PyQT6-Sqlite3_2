import sys
import json
import os
import winreg
import base64
import cryptography
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
from cryptography.fernet import Fernet

#1. Class defination
#class ChildClass(ParentClass): PascalCase
class AccountingApp(QWidget):
    #1.Properties = Varaible = Store
    settings={
        "windowTitle":"OK"
    }
    encryption_key=''
    cipher=''
    #2. Class constructor
    def __init__(self): # self=cio
        super().__init__() # I can call the parent construtor this way
        """ # Generate a new Fernet key (32 bytes)
        new_key = Fernet.generate_key()

        # Print the new key (optional)
        print(f"Generated Key: {new_key}")

        self.encryption_key = new_key
        self.cipher = Fernet(self.encryption_key)
        print("Hello from constructor")
        #2. function calling
        self.readJsonFile() """
        print(self.checkIfAdminIsCreated())
        x=self.checkIfAdminIsCreated()
        # Calling(argument)
        self.buildUI(isAdminCreated=x)
        pass
    
    #3.Method=Function
    def readJsonFile(self):
         # Lets try to read the json file
        try:
            with open('accounting.json', 'r') as file:
                self.settings = json.load(file)
        except FileNotFoundError:
            self.settings = {}
        print(self.settings)    
        print(type(self.settings)) #cio
        pass 
    # Define
    def encrypt_value(self, value):
        encrypted_value = self.cipher.encrypt(value.encode())
        return encrypted_value

    def decrypt_value(self, encrypted_value):
        try:
            decrypted_value = self.cipher.decrypt(encrypted_value).decode()
            return decrypted_value
        except cryptography.fernet.InvalidToken:
            print("InvalidToken: Unable to decrypt the value.")
            return None  # or handle the exception accordingly
    
    def checkIfAdminIsCreated(self):
        # Every function may return somethign 
        return False
        """ print('Hello from checkIfAdminIsCreated')
        
        registry_key_path = r"SOFTWARE\as"
        value_name = "dt"
        default_json = '{"isAdminCreated":false,"isLicenseActivated":false}'
        # Open the registry key for reading
        # Initialize key outside the try block
        key = None
        try:
            # Open the registry key for reading
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, registry_key_path)
            
            # Read the encrypted value of the specified entry
            # We are trying to get the value
            encrypted_value, _ = winreg.QueryValueEx(key, value_name)

            if encrypted_value:
                 # We are trying to read the value
                # Decrypt the value if it exists
               
                rd_value = winreg.QueryValueEx(key, "rd")[0]
            
                print(rd_value)
                winreg.CloseKey(key)
                decrypted_data = self.decrypt(rd_value,encryption_key)
                print(decrypted_data)
            
                print(key)
                dt_value = winreg.QueryValueEx(key, "dt")[0]
            
                print(dt_value)
                decrypted_value = self.decrypt_value(dt_value)
                print(f"Existing decrypted value: {decrypted_value}")
            else:
                 # We are try to set the value
                # Encrypt and create an entry with the registry key and set the default JSON string
                encrypted_default_json = self.encrypt_value(default_json)
                print("Create an entry dt with default JSON value")
                winreg.SetValueEx(key, value_name, 0, winreg.REG_BINARY, encrypted_default_json)
                
            # Close the registry key
        except FileNotFoundError:
            #We are try to set the value
            print("KeyNotFoundError")
            
            #ceo = ceo2.ClassName(ca1,ca2)
            encrypted_default_json = self.encrypt_value(default_json)
            key = winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, registry_key_path)
            # Decode the base64 string
            winreg.SetValueEx(key, value_name, 0, winreg.REG_BINARY, encrypted_default_json)
        
        finally:
            # Close the registry key if it's open
            if key:
                winreg.CloseKey(key) """
        pass
    
    def buildUI(self,isAdminCreated):
        #self=window
        self.setStyleSheet("background-color: #A4BFD8;") #aa
        self.setWindowTitle(self.settings["windowTitle"])
        self.showMaximized()
        
        # Check if the admin is created
        if isAdminCreated == False:
            # Then we wanat to create the registration from
            print('Create Registration Form')
             # Registration form
            registration_layout = QVBoxLayout(self)

            # Labels and Line Edits
            username_label = QLabel("Username:")
            username_edit = QLineEdit()

            password_label = QLabel("Password:")
            password_edit = QLineEdit()
            password_edit.setEchoMode(QLineEdit.EchoMode.Password)

            confirm_password_label = QLabel("Confirm Password:")
            confirm_password_edit = QLineEdit()
            confirm_password_edit.setEchoMode(QLineEdit.EchoMode.Password)

            registration_layout.addWidget(username_label)
            registration_layout.addWidget(username_edit)
            registration_layout.addWidget(password_label)
            registration_layout.addWidget(password_edit)
            registration_layout.addWidget(confirm_password_label)
            registration_layout.addWidget(confirm_password_edit)
            pass
        else:
            # Login form
            login_layout = QVBoxLayout(self)

            # Labels and Line Edits for Login
            username_label_login = QLabel("Username:")
            username_edit_login = QLineEdit()

            password_label_login = QLabel("Password:")
            password_edit_login = QLineEdit()
            password_edit_login.setEchoMode(QLineEdit.EchoMode.Password)

            login_layout.addWidget(username_label_login)
            login_layout.addWidget(username_edit_login)
            login_layout.addWidget(password_label_login)
            login_layout.addWidget(password_edit_login)
            print('Create Login Form')
            pass
        self.show()
        pass
    pass
#2. Create class Object
app = QApplication([])
ceo = AccountingApp()
ceo.showMaximized()
sys.exit(app.exec())

