from selenium import webdriver
import pytest

# @pytest.fixture()
# def setup():
#     driver = webdriver.Chrome()
#     driver.get("https://automation.credence.in/")
#     driver.implicitly_wait(10)
#     return driver


def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("launching chrome browser")

    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("launching firefox browser")

    elif browser == 'edge':
        driver = webdriver.Edge()
        print("launching edge browser")

    else:
        print("Headless Mode")
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("headless")
        driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    driver.maximize_window()
    return driver

def pytest_metadata(metadata):
     # To Add
    metadata["Environment"] = "Test"
    metadata["Project Name"] = "CredenceSoftware"
    metadata["Module Name"] = "Login"
    metadata["Tester"] = "Arshad"
    # To remove
    metadata.pop("Packages", None)
    metadata.pop("Plugins", None)

@pytest.fixture(params=[
    ("Credtest@gmail.com","cred123","Pass"),
    ("Credtest@gmail.com1","cred123","Fail"),
    ("Credtest@gmail.com","cred1231","Fail"),
    ("Credtest@gmail.com1","cred1231","Fail")
])
def getDataforlogin(request):
    return request.param