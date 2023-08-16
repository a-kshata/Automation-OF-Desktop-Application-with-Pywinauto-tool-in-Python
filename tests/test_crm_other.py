import pywinauto
from ..resources import Constants
from pywinauto import Application
import time
from pywinauto import keyboard
import logging
from ..resources import log_file
import sys
# stdout = logging.StreamHandler(sys.stdout)

# logging.basicConfig(
#     level=logging.DEBUG,
#     format="[{%(filename)s:%(lineno)d} %(levelname)s - %(message)s",
#     handlers=[stdout],
# )
logger = logging.getLogger()

def open_crm():
    app = Application("uia").start(r"C://Users//admin//Documents//MyCRM.exe")
    app = Application("uia").connect(path = r"C://Users//admin//Documents//MyCRM.exe")
    logger.info("open the application'MY_CRM(Sample_App)'")
    main_dig1 = app.window(title= 'My CRM (Sample App)')
    assert main_dig1.exists(), "Main window not found!"
    
    # main_dig1.print_control_identifiers()
    Other_win=main_dig1.child_window(title="Other", control_type="TabItem")
    print(str(Other_win.exists()))
    assert Other_win.exists()
    print("Other tab is exists, -Test passed")
    Other_win.click_input()
    logger.info("click on other TabItem")
    return main_dig1

def fill_other_information_fields(main_dig1):
    Other_Information1= main_dig1.Other_win.Other_Information
    # Other_Information1.print_control_identifiers()
    Generic1=Other_Information1.child_window(title="Other:", auto_id="textBox8", control_type="Edit")
    assert Generic1.exists()
    print("Generic1 field is exists, Test passed")
    Generic1.type_keys(Constants.generic_1)
    logger.info("click on field generic1 in other information")
    Generic2=Other_Information1.child_window(auto_id="textBox7", control_type="Edit")
    assert Generic2.exists()
    print("Generic2 field is exists, -Test passed")
    Generic2.type_keys(Constants.generic_2)
    logger.info("click on field generic2 in other information")
    Generic3=Other_Information1.child_window(auto_id="textBox3", control_type="Edit")
    assert Generic3.exists()
    print("Generic3 field is exists, -Test passed")
    Generic3.type_keys(Constants.generic_3)
    logger.info("click on field generic3 in other information")
    Generic4=Other_Information1. child_window(auto_id="textBox2", control_type="Edit")
    assert Generic4.exists()
    print("Generic4 field is exists, -Test passed")
    Generic4.type_keys(Constants.generic_4)
    logger.info("click on field generic4 in other information")
    Generic5=Other_Information1.child_window(auto_id="textBox1", control_type="Edit")
    assert Generic5.exists()
    print("Generic5 field is exists, -Test  passed")
    Generic5.type_keys(Constants.generic_5)
    logger.info("click on field generic5 in other information")
    Generic6=Other_Information1.child_window(auto_id="textBox13", control_type="Edit")
    assert Generic6.exists()
    print("Generic6 field is exists, -Test passed")
    Generic6.type_keys(Constants.generic_6)
    logger.info("click on field generic6 in other information")
    Generic7=Other_Information1.child_window(auto_id="textBox12", control_type="Edit")
    assert Generic7.exists()
    print("Generic7 field  is exists, - Test passed")
    Generic7.type_keys(Constants.generic_7)
    logger.info("click on field generic7 in other information")
    Generic8=Other_Information1.child_window(auto_id="textBox11", control_type="Edit")
    assert Generic8.exists()
    print("Generic8 field is exists, - Test passed")
    Generic8.type_keys(Constants.generic_8)
    logger.info("click on field generic8 in other information")
    Generic9=Other_Information1.child_window(auto_id="textBox10", control_type="Edit")
    assert  Generic9.exists()
    print("Generic9 field is exists, -Test passed")
    Generic9.type_keys(Constants.generic_9)
    logger.info("click on field generic9 in other information")
    Generic10=Other_Information1. child_window(auto_id="textBox9", control_type="Edit")
    assert Generic10.exists()
    print("Generic10 field  is exists, -Test passed")
    Generic10.type_keys(Constants.generic_10)
    logger.info("click on field generic10 in other information")
    Save=Other_Information1.child_window(title="Save", auto_id="button1", control_type="Button")
    Save.click()
    assert Save.click()
    print("In Other Save Button is exists, -Test passed")
    logger.info("click on save field in other information")
    
    
def other_form():
    main_dig1 = open_crm()
    fill_other_information_fields(main_dig1)
    
        
    main_dig1.close()


