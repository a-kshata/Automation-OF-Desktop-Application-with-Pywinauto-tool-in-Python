**Automation OF Desktop Application with Pywinauto tool in Python**

Pywinauto is a powerful Python library for automating GUI applications on Windows. With Pywinauto, you can interact with and control windows, dialogs, and controls in GUI applications, making it ideal for automating testing, data entry, and repetitive tasks.


### Installation:
    Before we get started, you need to have Python and pip installed on your machine. You can download the latest version of Python from the official website 
    - https://www.python.org/downloads/. 
  
    you can also use Any IDE for handling the python code like Visual Studio Code.
    In that you have to install Pywinauto by using command.
  
  
### Platform Support:
  Windows OS:
   Pywinauto is primarily designed for Windows GUI automation, so you need a Windows operating system to run the application.
  
  
### Software Required:
    1. Visual Studio Code IDE
    2. python Latest version
    3. pywinauto library
    4. element Inspecting tool "py_inspect"
                                              
### How to setup:
   1. Clone the repo into your local machine
   2. Open the Visual Studio IDE
   3. For using the pywinauto tool we have to use the syntax:
   4. import pywinauto
       cmd: py -m venv venv
   5. Activate the venv folder
       cmd: venv\script\Activate
   6. Install the all required libraries
       cmd: pip install -r req.txt
Desktop application automation using pywinauto

Pywinauto is a powerful Python library for automating GUI applications on Windows. With Pywinauto, you can interact with and control windows, dialogs, and controls in GUI applications, making it ideal for automating testing, data entry, and repetitive tasks.


### Installation:
    Before we get started, you need to have Python and pip installed on your machine. You can download the latest version of Python from the official website 
    - https://www.python.org/downloads/. 
  
    you can also use Any IDE for handling the python code like Visual Studio Code.
    In that you have to install Pywinauto by using command.
  
### Platform Support:
  Windows OS:
   Pywinauto is primarily designed for Windows GUI automation, so you need a Windows operating system to run the application.
    
### Software Required:
    1. Visual Studio Code IDE
    2. python Latest version
    3. pywinauto library
    4. element Inspecting tool "py_inspect"
                                              
### How to setup:
    1. Clone the repo into your local machine
    2. Open the Visual Studio IDE
    3. For using the pywinauto tool we have to use the syntax:
    4. import pywinauto
       cmd: py -m venv venv
    5. Activate the venv folder
       cmd: venv\script\Activate
    6. Install the all required libraries
       cmd: pip install -r req.txt

### Folder Structure:
    1. resources -   Constants.py,
    2. tests     -   CRM_PEOPLE, CRM_COMPANY, CRM_OTHER 
    3. run.py    -   used to run all test cases
    4. req.txt   -  contains all required dependencies used in the framework.       
   
 Note
  - Before setup project into the local machine please install the required softwares.

### Supported technologies:
     Win32 API (backend="win32"; used by default), MS UI Automation (backend="uia"). User input emulation modules mouse and keyboard work on both Windows and Linux.

### How to inspect window application elements :
    1. Install required libraries.
    2. Locate the desktop application by giving there path.
    3. Identify the UI elements.
    4. Inspect UI element properties.
    5. Interact with UI elements.(you can click a button or type text into textbox).
    6. run the application.

### How to run test :
    1. After updating the application information, save the run.py file.
    2. Use following command to run the Application.
        python run.py 
    3. When we Pass the argument like title in run.py, that time use the command:
    4. python run.py '--title' 'My CRM (Sample App)'
 
### Observe the Automation:
     The script will automate interactions with the target desktop application based on the code you provided. Ensure that the automation executes as expected.

### Folder Structure:
    1. resources-   Constants.py,
    2. tests   -   CRM_PEOPLE, CRM_COMPANY, CRM_OTHER
    3. run.py - use to run all test.
    3. req.txt -  contains all required dependencies used in the framework.       

 Note
  - Before setup project into the local machine please install the required softwares.

### Supported technologies:
    Win32 API (backend="win32"; used by default), MS UI Automation (backend="uia"). User input emulation modules mouse and keyboard work on both Windows and Linux.
    

### How to inspect window application elements :
    1. Install required libraries.
    2. Locate the desktop application by giving there path.
    3. Identify the UI elements.
    4. Inspect UI element properties.
    5. Interact with UI elements.(you can click a button or type text into textbox).
    6. run the application.


### How to run test :
    1.After updating the application information, save the run.py file.
    2.Use following command to run the Application.
      python run.py 
    3. When we Pass the argument like title in run.py, that time use the command:
    4. python run.py '--title' 'My CRM (Sample App)'
 
### Observe the Automation:
     The script will automate interactions with the target desktop application based on the code you provided. Ensure that the automation executes as expected.

     >pytest --capture=tee-sys test_run.py --title My_CRM --html=report.html


