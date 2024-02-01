class Dashboard(QWidget):
    def _init_(self):
        super()._init_()

        # Set the background color to white
        self.setStyleSheet("background-color: white;")

        # Create a horizontal layout for the LandingPage
        main_layout = QHBoxLayout(self)

        # Set layout margins and spacing to 0
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # Add a white section (80% width, 100% height)
        white_section = QWidget()
        white_section.setStyleSheet("background-color: white;")

        # Set layout margins and spacing to 0
        white_layout = QVBoxLayout(white_section)
        white_layout.setContentsMargins(0, 0, 0, 0)
        white_layout.setSpacing(5)

        # Add logo centered in the white area
        logo_label = QLabel()
        logo_pixmap = QPixmap("./unnamed.png")  # Replace with the actual path to your logo
        logo_label.setPixmap(logo_pixmap.scaled(200, 200, aspectRatioMode=Qt.AspectRatioMode.KeepAspectRatio))

        white_layout.addWidget(logo_label)

        white_label = QLabel("Welcome to the Landing Page (White Section)")
        white_layout.addWidget(white_label)
        white_layout.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        main_layout.addWidget(white_section, 8)  # Set the white section to take 80% of the available width

        # Add a blue section (20%)
        blue_section = QWidget()
        blue_section.setStyleSheet("background-color: #B7F7EF;")

        # Set layout margins and reduced spacing to 0
        blue_layout = QVBoxLayout(blue_section)
        blue_layout.setContentsMargins(0, 0, 0, 0)
        blue_layout.setSpacing(0)  # Adjusted spacing

        # Move language dropdown to the place of "Additional Information" label
        language_dropdown = QComboBox()
        language_dropdown.addItem("English")
        language_dropdown.addItem("Spanish")
        language_dropdown.addItem("French")
        blue_layout.addWidget(language_dropdown)

        # Create buttons for each menu item
        button_customers = QPushButton("Customers")
        button_suppliers = QPushButton("Suppliers")
        button_items = QPushButton("Items")
        button_sale_register = QPushButton("Sale Register")

        # Set button styles
        button_styles = """
            QPushButton {
                background-color: none;
                color: black;
                border: black;
                font-weight: bold;
                padding: 50px;

            }
        """

        button_hover_style = """
            QPushButton:hover {
                cursor: pointinghand;
            }
        """

        button_customers.setStyleSheet(button_styles + button_hover_style)
        button_suppliers.setStyleSheet(button_styles + button_hover_style)
        button_items.setStyleSheet(button_styles + button_hover_style)
        button_sale_register.setStyleSheet(button_styles + button_hover_style)

        button_customers.setStyleSheet(button_styles)
        button_suppliers.setStyleSheet(button_styles)
        button_items.setStyleSheet(button_styles)
        button_sale_register.setStyleSheet(button_styles)

        button_customers.clicked.connect(self.show_custom_popup)
        button_suppliers.clicked.connect(self.show_custom_popup)
        button_items.clicked.connect(self.show_custom_popup)
        button_sale_register.clicked.connect(self.show_custom_popup)

        # Set cursor for buttons
        button_customers.setCursor(Qt.CursorShape.PointingHandCursor)
        button_suppliers.setCursor(Qt.CursorShape.PointingHandCursor)
        button_items.setCursor(Qt.CursorShape.PointingHandCursor)
        button_sale_register.setCursor(Qt.CursorShape.PointingHandCursor)

        blue_layout.addWidget(button_customers)
        blue_layout.addWidget(button_suppliers)
        blue_layout.addWidget(button_items)
        blue_layout.addWidget(button_sale_register)

        main_layout.addWidget(blue_section, 2)  # Set the blue section to take 20% of the available width

        # Set the layout for the main widget
        self.setLayout(main_layout)