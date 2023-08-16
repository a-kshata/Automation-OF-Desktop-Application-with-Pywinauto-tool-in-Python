import pywinauto
from ..resources import Constants
from pywinauto import Application
import time
from pywinauto import keyboard

import sys
from ..resources import log_file

import logging



# #now we will Create and configure logger

# logging.basicConfig(filename="std_demo.log",

# format='%(asctime)s %(message)s',

# filemode='w')



# #Let us Create an object

logger = logging.getLogger()



# #Now we are going to Set the threshold of logger to DEBUG

# logger.setLevel(logging.DEBUG)

def open_crm():
    app = Application("uia").start(r"C://Users//admin//Documents//MyCRM.exe")
    app = Application("uia").connect(path = r"C://Users//admin//Documents//MyCRM.exe")
    logger.info("open the application 'MY_CRM(Sample_App)'")
    main_dig1 = app.window(title= 'My CRM (Sample App)')
    assert main_dig1.exists(), "Main window not found!"
    return main_dig1
    # main_dig1.print_control_identifiers()


def fill_company_name_fields(main_dig1):

    company_win = main_dig1.child_window(title="Company ", control_type="TabItem")
    company_win.click_input()
    Company_Name = main_dig1.company_win.Company_Name
    # Company_Name.print_control_identifiers()
    Work=Company_Name. child_window(title="Work:", auto_id="textBoxCompaniesName", control_type="Edit")
    print(str(Work.exists()))
    assert Work.exists()
    print("Company-Work button is exist - Test passed")
    Work.type_keys(Constants.company_name)
    logger.info("Enter the name of company")
    
def fill_company_address_fields(main_dig1):
    AddressBox= main_dig1.company_win.AddressBox
# AddressBox.print_control_identifiers()
    AddLine1=AddressBox.child_window(title="Add Line 1:", auto_id="textBoxCompaniesAddLine1", control_type="Edit")
    print(str(AddLine1.exists()))
    assert AddLine1.exists()
    print("AddLine 1 field is exists, -Test passed") 
    AddLine1.type_keys(Constants.company_address_line1)
    logger.info("Enter the first name in Company")
    AddLine2=AddressBox.child_window(title="Add Line 2:", auto_id="textBoxCompaniesAddLine2", control_type="Edit")
    print(str(AddLine2.exists()))   
    assert AddLine2.exists()
    print("AddLine 2 field is exists, -Test passed")
    AddLine2.type_keys(Constants.company_address_line2)
    logger.info("Enter the last name in company")
    City=AddressBox.child_window(title="City:", auto_id="textBoxCompaniesAddressCity", control_type="Edit")
    assert City.exists()
    print("City field is exists, -Test passed")
    City.type_keys(Constants.company_address_city)
    logger.info("Enter the city in Company")
    
    AddressBox.State.OpenButton.click()
    print("In Company State field   is exists, -passed")
    logger.info("click on open button in company")
    # AddressBox.State.listbox.print_control_identifiers()
    target_control = AddressBox.State.comboBox
    # target_control.print_control_identifiers()
    target_control.type_keys("{DOWN 4}",pause=0)
    target_control.type_keys("{ENTER}",set_foreground=False)
    logger.info("select the state in company")
    Zip=AddressBox.child_window(title="Zip:", auto_id="textBoxCompaniesAddressZip", control_type="Edit")
    print(str(Zip.exists()))  
    assert Zip.exists()
    print("Zip field  is exists, - Test passed")
    Zip.type_keys(Constants.company_address_zip)
    logger.info("Enter the zip number in address of company")
    
def fill_company_phone_fields(main_dig1):
        PhoneBox= main_dig1.company_win.Phone
        # PhoneBox.print_control_identifiers()
        Main=PhoneBox.child_window(title="Main:", auto_id="textBoxCompaniesMainPhone", control_type="Edit")
        print(str(Main.exists()))
        assert Main.exists()
        print("Main Phone number field is exists -Test passed ")
        Main.type_keys(Constants.company_phone_main)
        logger.info("Enter the main phone number of company")
    
        Other=PhoneBox.child_window(title="Other:", auto_id="textBoxCompaniesOtherPhone", control_type="Edit")
        print(str(Other.exists()))
        assert Other.exists()
        print("Other field  is exists, -Test passed")
        Other.type_keys(Constants.company_phone_other)
        logger.info("Enter the other phone number of company")
    # main_dig1.print_control_identifiers()
    
    
def fill_company_comments_fields(main_dig1):
    comment=main_dig1.child_window(auto_id="textBoxCompaniesComments", control_type="Edit")
    assert comment
    print("Company-Comment is exists, -Test passed")
    comment.type_keys(Constants.comments)
    logger.info("Enter the value in r'Comment/Notes'")
        
def company_form():
    main_dig1 = open_crm()    
    fill_company_name_fields(main_dig1)
    fill_company_address_fields(main_dig1)
    fill_company_phone_fields(main_dig1)
    fill_company_comments_fields(main_dig1)
    
    main_dig1.close()

