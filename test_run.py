import argparse
import sys

from .tests  import test_crm_people,test_crm_company,test_crm_other
import pytest_html
import pytest
import logging







# def test_print_name(params):
#     # print(title)
#  print("Displaying name: %s" %params)



def test_main(params):
    test_crm_people.people_form()
    
    # test_print_name()
    print(params)
    test_crm_company.company_form()
    test_crm_other.other_form()
    

    if __name__ == "__main__":
        test_main()
    



