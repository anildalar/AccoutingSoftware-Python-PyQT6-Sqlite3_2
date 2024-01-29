#from topmoudle.submodule import elem1,elem2,.....
from lib.initialSetup import import_sql,checkIfAdminRegister

from PyQt6.QtWidgets import QGridLayout,QWidget,QLabel,QLineEdit,QApplication, QMainWindow, QPushButton, QVBoxLayout, QDialog
from PyQt6.QtGui import QIcon

from app.gui.forms.login.login import LoginForm
from app.gui.forms.register.register import RegisterForm

#class ChildClass(ParentClass)
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('OKLABS Account Software 1.0.0')
        # Set window icon
        icon = QIcon("./src/assets/icon.png")  # Replace with the path to your icon file
        self.setWindowIcon(icon)
        self.setStyleSheet("background-color: #A4BFD8;")
        

        #moduleName.method(aa1,aa2)
        import_sql()
        self.init_ui()#aa
        pass
        
    def init_ui(self):#fa
         # Create a central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Create a layout for the central widget
        grid_layout = QGridLayout(central_widget)
        
        if checkIfAdminRegister() :
            #ceo              = ClassName()
            login_form = LoginForm()
            self.setCentralWidget(login_form)
            print('Show The Login Form')
            pass
        else:
             # Create three empty widgets to fill the first and last columns
            for i in range(3):
                empty_widget = QWidget()
                grid_layout.addWidget(empty_widget, 0, i)
                
            registration_form = RegisterForm()
            grid_layout.addWidget(registration_form, 0, 2)# row 2, column 0, spanning 1 row, 2 columns
                
            print('Show The Registeration Form')
            pass
        
        pass
    

if __name__ == "__main__":
    app = QApplication([])
    main_window = MainWindow()
    main_window.show()
    main_window.showMaximized()
    app.exec()
