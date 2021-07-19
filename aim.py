from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

class Aim:

    _id = 0
    _class = 1
    _text = 2

    def __init__(self):
        """
        Creates a web driver for the Aim instance
        """
        #initialize driver with driver path
        option = webdriver.ChromeOptions()
        option.add_argument('headless')
        self.driver = webdriver.Chrome(executable_path="C:\\WebDriver\\bin\\chromedriver.exe", options=option)
    
    def login(self):
        """
        Logs user into the Aim database and sets driver to home page.
        """
        #Retrieve login details
        user = input("NetID Username: ")
        password = input("NetID Password: ")

        #open assetworks
        self.driver.get("https://wisc.assetworks.hosting/fmax/screen/WORKDESK")

        #Login process
        self.driver.find_element_by_id("j_username").send_keys(user)
        self.driver.find_element_by_id("j_password").send_keys(password)
        self.driver.find_element_by_name("_eventId_proceed").click()
        self.driver.switch_to.frame("duo_iframe")
        send_push = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "auth-button")))
        send_push.click()
        print("Waiting for DUO approval...")
        self.driver.switch_to_default_content

        #Wait for duo to be accepted
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.LINK_TEXT, "Purchasing")))

    def click(self, selector, id):
        """
        Clicks the element located by the following way id, class, or inner-link-text

        Paramaters:
            selector: the way to locate the button. Use aim._id, aim._class or aim._text
            id: the id, class name, or inner-link-text
        """
        if(selector == self._id):
            self.driver.find_element_by_id(id).click()
        elif(selector == self._class):
            self.driver.find_element_by_class(id).click()
        elif(selector == self._text):
            self.driver.find_element_by_link_text(id).click()

    def select(self, selector, id, value):
        """
        Selects a value from a selector located by the following way id, class, or inner-link-text
            
        Paramaters:
            selector: the way to locate the button. Use aim._id, aim._class or aim._text
            id: the id, class name, or inner-link-text
            value: the value to select
        """
        if(selector == self._id):
            Select(self.driver.find_element_by_id(id)).select_by_value(value)
        elif(selector == self._class):
            Select(self.driver.find_element_by_class(id).click()).select_by_value(value)
        elif(selector == self._text):
            Select(self.driver.find_element_by_link_text(id).click()).select_by_value(value)

    def text(self, selector, id):
        """
        Returns the inner text of an element located by the following way id, class, or inner-link-text

        Paramaters:
            selector: the way to locate the button. Use aim._id, aim._class or aim._text
            id: the id, class name, or inner-link-text
        """
        if(selector == self._id):
            return self.driver.find_element_by_id(id).get_attribute("innerHTML")
        elif(selector == self._class):
            return self.driver.find_element_by_class(id).get_attribute("innerHTML")
        elif(selector == self._text):
            return self.driver.find_element_by_link_text(id).get_attribute("innerHTML")

    def insert(self, id, val):
        """
        Inserts an element into the provided id identified text field

        Paramaters:
            id: the id to insert the val into
            val: the text value to insert
        """
        self.driver.execute_script('document.getElementById(arguments[0]).value = arguments[1];', id, val)

    def table(self, id, row, col):
        """
        Returns the text value of a certain row/col of a table

        Paramaters:
            xpath: the path, with {} where row/col inserted
        """
        table = self.driver.find_element_by_id(id)
        rows = table.find_elements_by_class_name("browseRow")
        cols = rows[row].find_elements_by_tag_name('td')
        return cols[col].get_attribute("innerHTML")


    def wait(self, seconds):
        self.driver.implicitly_wait(seconds)