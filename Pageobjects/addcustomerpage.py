import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

class Addcustomer:

    link_customermenu_xpath = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/a"
    link_menuitem_customer_xpath = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/ul/li[1]/a/p"
    button_addnewcustomer_xpath = "//body/div[3]/div[1]/form[1]/div[1]/div[1]/a[1]"
    input_email_xpath = "//input[@id='Email']"
    input_password_xpath = "//input[@id='Password']"
    input_firstname_xpath = "//input[@id='FirstName']"
    input_lastname_xpath = "//input[@id='LastName']"
    radio_male_id = "Gender_Male"
    radio_female_id = "Gender_Female"
    input_DOB_xpath = "//input[@id='DateOfBirth']"
    input_companyname_xpath = "//input[@id='Company']"
    chkbox_tax_id = "IsTaxExempt"
    input_newsltr_xpath = "//div[@class='k-widget k-multiselect k-multiselect-clearable k-state-hover']//div[@role='listbox']"
    input_customerroles_xpath = "//div[@class='input-group-append input-group-required']//div[@role='listbox']"
    listitem_admin_xpath = "//li[normalize-space()='Administrators']"
    listitem_forummoderators_xpath = "//li[normalize-space()='Forum Moderators']"
    listitem_guest_xpath = "//li[normalize-space()='Guests']"
    listitem_vendors_xpath = "//li[contains(text(),'Vendors')]"
    listitem_registered_xpath = "//li[@id='be54aee5-34b7-4d80-9988-51d478510b25']"
    dropdwn_mgrofvendor_id = "VendorId"
    input_admincontent_xpath = "//textarea[@id='AdminComment']"
    btn_save_xpath = "//button[@name='save']"
    
    
    def __init__(self, driver):
        self.driver = driver
    
    def ClickCustomermenu(self):
        self.driver.find_element_by_xpath(self.link_customermenu_xpath).click()

    def ClickCustomer(self):
        self.driver.find_element_by_xpath(self.link_menuitem_customer_xpath).click()

    def ClickAddcustomer(self):
        self.driver.find_element_by_xpath(self.button_addnewcustomer_xpath).click()

    def EnterEmail(self, email):
        self.driver.find_element_by_xpath(self.input_email_xpath).send_keys(email)

    def EnterPassword(self, password):
        self.driver.find_element_by_xpath(self.input_password_xpath).send_keys(password)

    def EnterFirstname(self, firstname):
        self.driver.find_element_by_xpath(self.input_firstname_xpath).send_keys(firstname)

    def EnterLastname(self, lastname):
        self.driver.find_element_by_xpath(self.input_lastname_xpath).send_keys(lastname)

    def SelectGender(self, gender):
        if gender == 'Male':
            self.driver.find_element_by_id(self.radio_male_id).click()
        elif gender == 'Female':
            self.driver.find_element_by_id(self.radio_female_id).click()
        else:
            self.driver.find_element_by_id(self.radio_male_id).click()

    def EnterCompanyname(self, name):
        self.driver.find_element_by_xpath(self.input_companyname_xpath).send_keys(name)

    def EnterDOB(self, dob):
        self.driver.find_element_by_xpath(self.input_DOB_xpath).send_keys(dob)

    def EnterNLname(self, NLname):
        self.driver.find_element_by_xpath(self.input_newsltr_xpath).send_keys(NLname)

    def SelectCustomerRoles(self, role):
        self.driver.find_element_by_xpath(self.input_customerroles_xpath).click()
        time.sleep(3)
        if role == 'Registered':
            self.item = self.driver.find_element_by_xpath(self.listitem_registered_xpath)
        elif role == 'Administrators':
            self.item = self.driver.find_element_by_xpath(self.listitem_admin_xpath)
        elif role == 'Guests':
            # Here user can be Registered( or) Guest, only one
            time.sleep(3)
            self.driver.find_element_by_xpath("//span[@title='delete']").click()
            self.item = self.driver.find_element_by_xpath(self.listitem_guest_xpath)
        elif role == 'Registered':
            self.item = self.driver.find_element_by_xpath(self.listitem_registered_xpath)
        elif role == 'Vendors':
            self.item = self.driver.find_element_by_xpath(self.listitem_vendors_xpath)
        elif role == 'Forum Moderators':
            self.item = self.driver.find_element_by_xpath(self.listitem_forummoderators_xpath)
        else:
            self.item = self.driver.find_element_by_xpath(self.listitem_guest_xpath)
        time.sleep(3)
        # self.listitem.click()
        self.driver.execute_script("arguments[0].click();", self.item)

    def SelectManagerOfVendor(self, value):
        drp = Select(self.driver.find_element_by_id(self.dropdwn_mgrofvendor_id))
        drp.select_by_visible_text(value)

    def EnterAdminContent(self, content):
        self.driver.find_element_by_xpath(self.input_admincontent_xpath).send_keys(content)

    def ClickSave(self):
        self.driver.find_element_by_xpath(self.btn_save_xpath).click()





