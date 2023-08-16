
import pytest
from pywinauto import Application
import pytest_html
import os
import time
import logging


def pytest_addoption(parser):
    parser.addoption("--title", action="store", help="title")
    

@pytest.fixture
def params(request):
    params = {}
    params['title'] = request.config.getoption('--title')
    
    if params['title'] is None:
        pytest.skip()
    return params

# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     report = outcome.get_result()
#     extras = getattr(report, "extras", [])
#     if report.when == "call":
#         # always add url to report
#         extras.append(pytest_html.extras.url(r"C://Users//admin//Documents//MyCRM.exe"))
#         xfail = hasattr(report, "wasxfail")
#         if (report.skipped and xfail) or (report.failed and not xfail):
#         # only add additional html on failure
#             extras.append(pytest_html.extras.html("<div>Additional HTML</div>"))
#             report.extras = extras
#         report_directory =os.path.dirname(item.config.option.htmlpath)
#         file_name = str(int(round(time.time()*1000)))+ ".png"
#         # file_name =report.nodeid.replace("::","_")+".png"
#         destinationFile=os.path.join(report_directory,file_name)
#         screenshot = Application.capture_as_image
#         screenshot.save(destinationFile)
#         screenshot.save(destinationFile)
            
#         if file_name:
#                 html ='<div><img src="%s" alt=screenshot style="width:300px;height=200px"'\
#                     'onclick="window.open(this.src)"align="right"/></div>'%file_name
#                 extras.append(pytest_html.extras.html(html))
#                 report.extra=extras

    
        
# @pytest.hookimpl(tryfirst=True,hookwrapper=True) 
# def pytest_runtest_makereport(item,call):    
#     outcome = yield
#     rep = outcome.get_result()

#     if rep.when == "call" and rep.failed:
#         # Take a screenshot using pywinauto
#         title = 'My CRM (Sample App)'
#         app = Application("uia").start(r"C://Users//admin//Documents//MyCRM.exe")
#         app = Application("uia").connect(path = r"C://Users//admin//Documents//MyCRM.exe")
#         # Ajust the window title regex as needed
#         window = app.top_window()
#         screenshot_path = f"screenshots/{item.name}.png"  # Change the path as needed
#         window.capture_as_image()(screenshot_path)
#         print(f"Screenshot saved: {screenshot_path}")

# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_protocol(item, nextitem):
#     with logging.captureWarnings(True):
#         outcome = yield
#     rep = outcome.get_result()
#     setattr(rep, "logs", logging.getLogRecords())
