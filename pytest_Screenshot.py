# import os
# import pytest
# from pywinauto import Application
# from pywinauto import timings
# from PIL import ImageGrab

# @pytest.hookimpl(tryfirst=True)
# def pytest_runtest_makereport(item, call):
#     """
#     This hook is executed after each test run.
#     It captures a screenshot on test failure.
#     """
#     if call.when == "call" and call.excinfo is not None:
#         screenshot_folder = "screenshots"
#         os.makedirs(screenshot_folder, exist_ok=True)

#         screenshot_filename = f"image.png"
#         screenshot_path = os.path.join("C:\Users\admin\Desktop\image.png",screenshot_filename)

#         app = application.Application(backend="uia")
#         app.connect(title_re=".*My CRM (Sample App)*")  # Replace with your application's title
#         window = app.top_window()

#         screenshot = window.capture_as_image()
#         screenshot.save(screenshot_path)

# def pytest_configure(config):
#     """
#     Configure the plugin.
#     """
#     config._screenshot_plugin_initialized = True

# def pytest_unconfigure(config):
#     """
#     Clean up any resources.
#     """
#     if hasattr(config, "_screenshot_plugin_initialized"):
#         del config._screenshot_plugin_initialized
# from PIL import ImageGrab

# # Take a screenshot of the entire screen
# screenshot = ImageGrab.grab()
# screenshot.save("screenshot.png")
# screenshot.show()

# def test_example(app):
    