import pywinauto

# from ..resources import save_image
from ..resources import Constants
from pywinauto import Application
import time
import logging
import sys
import pytest
from ..resources import log_file
import datetime


import logging



#now we will Create and configure logger

# logging.basicConfig(filename="test_log.log",

# format='%(asctime)s %(message)s',
# encoding='utf_8',

# filemode='w')

# logger=logging.getLogger()
# console_handler = logging.StreamHandler()  # Sends logs to console
# formatter = logging.Formatter('%(levelname)s - %(message)s')
# console_handler.setFormatter(formatter)

# # Attach handler to the root logger

# logger.addHandler(console_handler)

# file_handler = logging.FileHandler('test_log.log')  # Logs to a file named "logfile.log"
# formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
# file_handler.setFormatter(formatter)

# # Attach handler to the root logger
# logger = logging.getLogger()
# logger.addHandler(file_handler)



# # #Now we are going to Set the threshold of logger to DEBUG

# logger.setLevel(logging.DEBUG)


logger = logging.getLogger()

def open_crm():
    
    logger.info("Enter the title1")
    title = 'My CRM (Sample App)'
    app = Application("uia").start(r"C://Users//admin//Documents//MyCRM.exe")
    app = Application("uia").connect(path = r"C://Users//admin//Documents//MyCRM.exe")
    main_dig1 = app.window(title = 'My CRM (Sample App)')
    assert main_dig1.exists(), "Main window not found!"
        # assert False, "to check workflow"
    main_dig1 = app.window(title= 'My CRM (Sample App)')
    return main_dig1

# # main_dig1.print_control_identifiers()

def fill_people_name_fields(main_dig1):
    NameBox = main_dig1.People.Name
    NameBox.Edit2.type_keys(Constants.people_name_first)
# #     # assert False,"event fail"
    

    print("People first name exists, -Test passed")
    logger.info("Enter the first name field in people")
    NameBox.Edit.type_keys(Constants.people_name_last)
    assert NameBox.Edit.exists()
    print("People last name is exists, -Test Passed")
    logger.info("Enter the last name in people")
    print("Enter the last name in people")
    NameBox.Button.click()
    assert NameBox.Button.click()
    print("Female button is exists, -Test passed")
    return main_dig1

def fill_people_address_fields(main_dig1):
    AddressBox = main_dig1.People.Address
    AddressBox.Edit4.type_keys(Constants.people_address_add_line1)
    assert AddressBox.Edit4.exists()
    print("People address of AddLine 1 is exists, -Test passed")
    logger.info("Enter the AddLine1 address in people")
    AddressBox.Edit3.type_keys(Constants.people_address_add_line2)
    assert  AddressBox.Edit3.exists()
    print("People address of AddLine 2 field  is exists, -Test passed")
    logger.info("Enter the AddLine2 address in people")
    AddressBox.Edit2.type_keys(Constants.people_address_city)
    assert AddressBox.Edit2.exists()
    print("People city field is exists, -Test passed")
    logger.info("Enter the city name in people")
    AddressBox.Edit7.type_keys(Constants.people_address_zip)
    print(str(AddressBox.Edit7.exists()))
    assert AddressBox.Edit7.exists()
    print("People zip field is exists, -Test passed")
    logger.info("Enter the zip of address in people")
    
    # AddressBox.print_control_identifiers()
    # AddressBox.State.OpenButton.click()
    # print("State field is exists")
    # logger.info("click on the open button")
    # # AddressBox.State.listbox.print_control_identifiers()
    # target_control = AddressBox.State.comboBox
    # target_control.type_keys("{DOWN 4}",pause=0)
    # target_control.type_keys("{ENTER}",set_foreground=False)
    # logger.info("select the state name in people")

def fill_people_phone_fields(main_dig1):
    PhoneBox = main_dig1.People.Phone
    Home =  PhoneBox.child_window(title="Home:", auto_id="textBoxPeopleHomePhone", control_type="Edit")
    print(str(Home.exists()))
    assert Home.exists()
    print( "Home field is exists, - Test passed")
    Home.type_keys(Constants.people_phone_home)
    logger.info("Enter the phone number of home in people")
    Work = PhoneBox.child_window(title="Work:", auto_id="textBoxPeopleWorkPhone", control_type="Edit")
    print(str(Work.exists()))
    assert Work.exists()
    print( "Work button is exists, - Test passed")
    Work.type_keys(Constants.people_phone_work)
    logger.info("Enter the phone number of Work in people")
    Mob =PhoneBox.child_window(title="Mobile:", auto_id="textBoxPeopleMobilePhone", control_type="Edit")
    print(str(Mob.exists()))
    assert Mob.exists()
    print("Mob Field is exists, -Test passed ")
    Mob.type_keys(Constants.people_phone_mobile)
    logger.info("Enter the mobile number in people") 
    
def fill_people_email_fields(main_dig1):  
    EmailBox = main_dig1.People.Email
    # EmailBox.print_control_identifiers()
    Personal = EmailBox.child_window(title="Personal:", auto_id="textBoxPeoplePersonalEmail", control_type="Edit")
    print(str(Personal.exists()))
    assert Personal.exists()
    print("Personal email field is exists - Test passed")
    Personal.type_keys(Constants.people_email_personal)
    logger.info("Enter personal email in people") 
    print("Enter personal email in people")
    Work = EmailBox.child_window(title="Work:", auto_id="textBoxPeopleWorkEmail", control_type="Edit")
    print(str(Work.exists()))
    assert Work.exists()
    print("Work field is exists. -Test passed")
    Work.type_keys(Constants.people_email_work)
    logger.info("Enter the Work email in people") 
    Comments= main_dig1.People.child_window(title="Active", auto_id="checkBox1", control_type="CheckBox").click()
    assert Comments
    print("r'Comments/Notes'  field is exists, -Test passed")
    logger.info("click on r'Comments/Notes' block in people") 

# # open_crm()

def people_form():


    # try:
    main_dig1 = open_crm()
    fill_people_name_fields(main_dig1)
        # method_way.test_example()
    fill_people_address_fields(main_dig1)
    fill_people_phone_fields(main_dig1)
    fill_people_email_fields(main_dig1)
    # main_dig1.close()
    # # except Exception as e:
    # save_image.screen_shot()
    # pytest.fail(e)
    # print(str(e))
    
    main_dig1.close()