import os
import sys

import re  # Import re for regular expressions
import winreg  # Import winreg for working with Windows Registry
import requests  # Import requests for making HTTP requests
import pywintypes
import json

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet

from pathlib import Path

from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QDesktopWidget,QComboBox, QMessageBox, QPlainTextEdit, QProgressBar
from PyQt5.QtGui import QIcon,QFont  # Import QIcon for setting the window icon
from custom_widgets import CustomPlainTextEdit  # Import the custom class

from resources import *

from login_form import LoginForm
from updater import Updater

from dotenv import load_dotenv
load_dotenv()  # Load variables from .env file

cms_url = os.getenv("CMS_URL")
win_reg_url = os.getenv("WIN_REG_URL")



class RegistrationForm(QWidget):
    def __init__(self,login_form):
        super().__init__()
        self.login_form = login_form

        self.init_ui()
    

    def init_ui(self):
        self.setWindowTitle('AUTOKIO Registration Form')
        # Set the window icon
        self.setWindowIcon(QIcon('icon.png')) 

        self.email_label = QLabel('Email:')
        self.email_input = QLineEdit()

        self.password_label = QLabel('Password (Min 6 Char):')
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)

        self.confirm_password_label = QLabel('Confirm Password:')
        self.confirm_password_input = QLineEdit()
        self.confirm_password_input.setEchoMode(QLineEdit.Password)
        
        self.fullname_label = QLabel('Full Name:')
        self.fullname_input = QLineEdit()

        self.mobileno_label = QLabel('Mobile No:')
        self.mobileno_input = QLineEdit("+91")

        self.address_label = QLabel('Enter Address:')
        #self.address_text = QPlainTextEdit(self)
        self.address_text = CustomPlainTextEdit()  # Use the custom class
        # Set a maximum height for the QPlainTextEdit
        self.address_text.setMaximumHeight(60)

        self.state_label = QLabel('State:')
        self.state_input = QLineEdit()

        self.city_label = QLabel('City:')
        self.city_input = QLineEdit()

        self.pincode_label = QLabel('Pincode:')
        self.pincode_input = QLineEdit()

        self.register_button = QPushButton('Register')
        self.register_button.clicked.connect(self.register)

        
        self.progress_bar = QProgressBar(self)
        self.progress_bar.setRange(0, 0)  # Set the range to 0 to show an indeterminate progress bar
        self.progress_bar.hide()  # Initially hide the progress bar

        layout = QVBoxLayout()
        layout.addWidget(self.progress_bar)

        layout.addWidget(self.email_label)
        layout.addWidget(self.email_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.confirm_password_label)
        layout.addWidget(self.confirm_password_input)
        
        layout.addWidget(self.fullname_label)
        layout.addWidget(self.fullname_input)
        layout.addWidget(self.mobileno_label)
        layout.addWidget(self.mobileno_input)
        layout.addWidget(self.address_label)
        layout.addWidget(self.address_text)
        
        layout.addWidget(self.state_label)
        self.state_input = QComboBox(self)
        self.state_input.addItems([
            "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh",
            "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand", "Karnataka",
            "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram",
            "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu",
            "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal",
            "Andaman and Nicobar Islands", "Chandigarh",
            "Dadra and Nagar Haveli and Daman and Diu", "Lakshadweep", "Delhi", "Puducherry",
            "Jammu and Kashmir", "Ladakh"
        ])
        layout.addWidget(self.state_input)
        
        layout.addWidget(self.city_label)
        layout.addWidget(self.city_input)
        layout.addWidget(self.pincode_label)
        layout.addWidget(self.pincode_input)
        layout.addWidget(self.register_button)

        self.setLayout(layout)

        self.email_input.setFocus()
        
         # Set the window size to be 70% of the desktop width
        desktop_width = QDesktopWidget().screenGeometry().width()
        self.resize(int(desktop_width * 0.5), self.height())
        
        self.mobileno_input.setTabOrder(self.mobileno_input, self.address_text)
        self.address_text.setTabOrder(self.address_text, self.state_input)
        self.state_input.setTabOrder(self.state_input, self.city_input)
        self.city_input.setTabOrder(self.city_input, self.pincode_input)
        self.pincode_input.setTabOrder(self.pincode_input, self.register_button)

        # Set tab order for moving from state_input to city_input
        self.state_input.setTabOrder(self.state_input, self.city_input)

        # Set tab order for moving from city_input to pincode_input
        self.city_input.setTabOrder(self.city_input, self.pincode_input)

        # Set tab order for moving from pincode_input to register_button
        self.pincode_input.setTabOrder(self.pincode_input, self.register_button)
        
        # Center the window on the desktop
        self.center_on_screen()

    
    def login_cms(self):
        if self.load_data_from_registry() != False:
            registry_data = self.load_data_from_registry()
            print(registry_data)
            # Access values from the returned dictionary
            email = registry_data["email"]
            password = registry_data["password"]
        
            strapi_login_url = f"{cms_url}/api/auth/local"
            login_data = {
                "identifier": email,
                "password": password
            }

            try:
                response = requests.post(strapi_login_url, json=login_data)
                response.raise_for_status()

                if response.status_code == 200:
                    # Login successful, continue with the application
                    print("Strapi login successful.")
                    self.open_login_page()
                    # Here you might want to perform additional actions if the login is successful
                else:
                    # Strapi login failed, show the registration form
                    print("Strapi login failed.")
                    

                    # Connect the login_failed method to handle the case where Strapi login fails
                    self.login_failed()
            except requests.exceptions.RequestException as e:
                print(f"Error during Strapi login: {e}")
                # Handle the error as needed, possibly show an error message to the user
                pass
        else:
            self.show()
        pass
    def open_login_page(self):
        # Create an instance of your login form (assuming you have a LoginForm class)
        self.login_form.show()
        self.hide()

        # Optionally, hide the registration form if needed
        #self.hide()
        pass
    def center_on_screen(self):
        screen_geometry = QDesktopWidget().screenGeometry()
        x = (screen_geometry.width() - self.width()) // 2
        y = (screen_geometry.height() - self.height()) // 2
        self.move(x, y)
        
    # Function to encrypt data
    def encrypt(self, data, key):
        # Ensure that the key size is valid for AES (16, 24, or 32 bytes)
        # Ensure that the key size is valid for Fernet (32 bytes)
        key_size_bytes = len(key)
        print(key_size_bytes)
        #if key_size_bytes != 32:
        #    raise ValueError(f"Invalid key size: {key_size_bytes} bytes. Fernet key size should be 32 bytes.")

        # Initialize the Fernet cipher with the provided key
        cipher_suite = Fernet(key)
        
        # Encrypt the data
        encrypted_data = cipher_suite.encrypt(data.encode())
        return encrypted_data

    # Function to decrypt data
    def decrypt(self, encrypted_data, key):
        # Ensure that the key size is valid for Fernet (32 bytes)
        key_size_bytes = len(key)
        #if key_size_bytes != 32:
        #    raise ValueError(f"Invalid key size: {key_size_bytes} bytes. Fernet key size should be 32 bytes.")

        # Initialize the Fernet cipher with the provided key
        cipher_suite = Fernet(key)

        # Decrypt the data
        decrypted_data = cipher_suite.decrypt(encrypted_data).decode()
        return decrypted_data
    
    def load_data_from_registry(self):
        try:
            encryption_key = os.getenv("ENCRYPTION_KEY")
            if not encryption_key:
                raise ValueError("Encryption key is not set in the environment variables")

            # Convert the key to bytes if it's a string
            encryption_key = encryption_key.encode() if isinstance(encryption_key, str) else encryption_key
            
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, win_reg_url, 0, winreg.KEY_READ)
            rd_value = winreg.QueryValueEx(key, "rd")[0]
            
            print(rd_value)
            winreg.CloseKey(key)
            decrypted_data = self.decrypt(rd_value,encryption_key)
            print(decrypted_data)
            # Assuming decrypted_data is a JSON string
            decrypted_data_dict = json.loads(decrypted_data)
            print(decrypted_data_dict)
            # Now you can access the email attribute
            email = decrypted_data_dict.get("email")
            print(email)
            print("Success")
            return {
                "email": decrypted_data_dict.get("email"),
                "password": decrypted_data_dict.get("password"),
                "fullname": decrypted_data_dict.get("password"),
                "mobileno": decrypted_data_dict.get("mobileno"),
                "address": decrypted_data_dict.get("address"),
                "state": decrypted_data_dict.get("state"),
                "city": decrypted_data_dict.get("city"),
                "pincode": decrypted_data_dict.get("pincode"),
            }
            
        except FileNotFoundError:
            print("Failed")
            return False

    def is_valid_email(self, email):
        # Simple email validation using a regular expression
        email_pattern = re.compile(r"[^@]+@[^@]+\.[^@]+")
        return bool(re.match(email_pattern, email))
    
    def is_valid_mobile_number(self, number):
        # Regular expression for a valid Indian mobile number
        # Assumes the country code is +91 and followed by 10 digits
        pattern = re.compile(r'^\+91[1-9]\d{9}$')
    
        # Check if the provided number matches the pattern
        return bool(re.match(pattern, number))
    def is_valid_pincode(self, pincode):
        # Regular expression for a valid Indian PIN code
        pincode_pattern = re.compile(r'^[1-9][0-9]{5}$')
        
        # Check if the provided PIN code matches the pattern
        return bool(re.match(pincode_pattern, pincode))
    def is_valid_fullname(self, fullname):
        # Regular expression for a valid Indian PIN code
        fullname_pattern = re.compile(r'^[a-zA-Z ]*$')
        
        # Check if the provided fullname matches the pattern
        return bool(re.match(fullname_pattern, fullname))

    def is_valid_city(self, city):
        city_pattern = re.compile(r'^[a-zA-Z ]*$')
        
        # Check if the provided fullname matches the pattern
        return bool(re.match(city_pattern, city))

    def register(self):
         # Show the progress bar to indicate ongoing processing
        self.progress_bar.show()

        # Disable the button after click
        self.register_button.setEnabled(False)
    
        email = self.email_input.text()
        password = self.password_input.text()
        confirm_password = self.confirm_password_input.text()
        fullname = self.fullname_input.text()
        mobileno = self.mobileno_input.text()
        address = self.address_text.toPlainText()
        state = self.state_input.currentText()
        city = self.city_input.text()
        pincode = self.pincode_input.text()
        
        print("emil :- "+email)
        print("password :- "+password)
        print("confirm_password :- "+confirm_password)
        print("fullname :- "+fullname)
        print("mobileno :- "+mobileno)
        print("address :- "+address)
        print("state :- "+state)
        print("city :- "+city)
        print("pincode :- "+pincode)
        

        if email and password and confirm_password and fullname and mobileno and address and state and city and pincode:
            if self.is_valid_email(email):
                if len(password) >= 6 and password == confirm_password:
                    if self.is_valid_mobile_number(mobileno):
                        if self.is_valid_pincode(pincode):
                            if self.is_valid_city(city):
                                if self.is_valid_fullname(fullname):
                                    print(f"{mobileno} is a valid Indian mobile number.")
                                    print(f"{pincode} is a valid Indian PIN code.")
                                    print(f"{city} is a valid Indian PIN code.")
                                    print(f"{fullname} is a valid Indian PIN code.")
                                    
                                    # Register user in Strapi
                                    strapi_api_url = f"{cms_url}/api/auth/local/register"
                                    strapi_data = {
                                        "username": email,  # Assuming mobile number is unique and can be used as a username
                                        "email": email,     # Use mobile number as email for simplicity
                                        "password": password   # Use mobile number as password for simplicity
                                    }
                                    
                                    try:
                                        response = requests.post(strapi_api_url, json=strapi_data)
                                        response.raise_for_status()
                                        # Print the status code
                                        print("Status Code:", response.status_code)

                                        # Parse the JSON response
                                        strapi_response = response.json()

                                        # Print the entire response for debugging purposes
                                        print("Strapi Response:", strapi_response)
                                        
                                        # Check if the status code is 200 (OK)
                                        if response.status_code == 200:
                                            # Display a success message
                                            QMessageBox.information(self, 'Success', 'Registration successfull!')
                                            
                                            print("User registered successfully in Strapi.")
                                            
                                            jwt_token = strapi_response.get("jwt", "")
                                            user_info = strapi_response.get("user", {})
                                            
                                            print(f'Registering user:')
                                            print(f'Full Name: {fullname}')
                                            print(f'Mobile No: {mobileno}')
                                            print(f'Address: {address}')
                                            print(f'State: {state}')
                                            print(f'City: {city}')
                                            print(f'Pincode: {pincode}')
                                            
                                            print(f'jwt_token: {jwt_token}')
                                            print(f'user_info: {user_info}')
                                            
                                            # Add your registration logic here
                                            
                                            
                                            registration_data = {
                                                "jwt_token": jwt_token,
                                                "user_info": user_info,
                                                "email": email,
                                                "password": password,
                                                "fullname": fullname,
                                                "mobileno": mobileno,
                                                "address": address,
                                                "state": state,
                                                "city": city,
                                                "pincode": pincode,
                                                "is_registered": "1"
                                            }
                                            registration_data_json = json.dumps(registration_data)
                                            encryption_key = os.getenv("ENCRYPTION_KEY")
                                            
                                            if not encryption_key:
                                                raise ValueError("Encryption key is not set in the environment variables")

                                            # Convert the key to bytes if it's a string
                                            encryption_key = encryption_key.encode() if isinstance(encryption_key, str) else encryption_key
                                            
                                            # Create or open the registry key
                                            key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, win_reg_url)
                                            
                                            # Encrypt the JSON string
                                            encrypted_data = self.encrypt(registration_data_json, encryption_key)

                                            # Store the encrypted data in the registry
                                            winreg.SetValueEx(key, "rd", 0, winreg.REG_BINARY, encrypted_data)

                                            # Open the login page after successful registration
                                            # Hide the registration form
                                            
                                            self.login_cms()
                                        
                                        else:
                                            QMessageBox.information(self, 'Error', f"{city} is not a valid Indian PIN code.")
                                        
                                    except requests.exceptions.RequestException as e:
                                        print(f"Error registering user in Strapi: {e}")
                                    finally:
                                        pass
                                else:
                                    QMessageBox.information(self, 'Error', f"{fullname} is not a valid Fullname.")
                            else:
                                QMessageBox.warning(self, 'Error', f"{city} is not a valid City.")
                        else:
                            QMessageBox.warning(self, 'Error', f"{pincode} is not a valid Indian PIN code.")
                    else:
                        QMessageBox.warning(self, 'Error', f"{mobileno} is not a valid Indian mobile number.")
                            
                else:
                    QMessageBox.warning(self, 'Error', 'Password should be at least 6 characters and match the confirmation.')
            else:
                QMessageBox.warning(self, 'Error', 'Invalid email format.')
        else:
            print('Please fill in all fields.')
        
        # Hide the progress bar when processing is complete
        self.progress_bar.hide()
        # Re-enable the button after processing
        self.register_button.setEnabled(True)
        
        
if __name__ == '__main__':
    # Specify the service name
    app = QApplication(sys.argv)
    updater = Updater(current_version=1.0)
    login_form = LoginForm(updater)
    registration_form = RegistrationForm(login_form)
    # Set the reference to the registration form in the login form
    registration_form.login_cms()
    
    registration_form.login_form = login_form

    sys.exit(app.exec_())
