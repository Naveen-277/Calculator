# Basic Calculator
This is a simple Basic Calculator built using Flask for the backend, with HTML, CSS, and JavaScript for the frontend. It performs basic arithmetic operations such as addition, subtraction, multiplication, and division.

## Project Structure
```
calculator/
│
├── app.py                # Main Flask application
│
├── static/
│   ├── css/
│   │   └── style.css      # Stylesheet for the calculator
│   └── js/
│       └── script.js      # JavaScript for dynamic behavior
│
└── templates/
    └── calculator.html    # HTML template for the calculator UI
```
## Features
    Perform basic arithmetic operations (+, -, ×, ÷)
    Simple and responsive design
    User-friendly button layout
    Erase function for clearing single digits
    Clear function to reset the entire input
## Technologies Used
    Flask: Python web framework
    HTML/CSS: For the layout and styling
    JavaScript: For handling button actions and interactions
## app.py: 
  The main Flask application that serves the calculator UI and handles requests.

static/css/style.css: The stylesheet containing all the CSS for the layout, styling, and color schemes of the calculator.

static/js/script.js: JavaScript file that contains the dynamic functionality for handling button clicks, updating the display, and performing operations like clear and erase.

templates/calculator.html: HTML file that serves as the UI for the calculator, defining the structure and integration of JavaScript and CSS.
