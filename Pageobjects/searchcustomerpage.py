class SearchCustomer():

    inputEmail_id = "SearchEmail"
    inputFirstName_id="SearchFirstName"
    inputLastName_id="SearchLastName"
    buttonSearch_id="search-customers"
    tableSearchResults_xpath="//table[@role='grid']"
    table_xpath="//table[@id='customers-grid']"
    tableRows_xpath="//table[@id='customers-grid']//tbody/tr"
    tableColumns_xpath="//table[@id='customers-grid']//tbody/tr/td"

    def __init__(self, driver):
        self.driver = driver

    def EnterEmail(self,email):
        self.driver.find_element_by_id(self.inputEmail_id).clear()
        self.driver.find_element_by_id(self.inputEmail_id).send_keys(email)

    def EnterFirstName(self,fname):
        self.driver.find_element_by_id(self.inputFirstName_id).clear()
        self.driver.find_element_by_id(self.inputFirstName_id).send_keys(fname)

    def EnterLastName(self,lname):
        self.driver.find_element_by_id(self.inputLastName_id).clear()
        self.driver.find_element_by_id(self.inputLastName_id).send_keys(lname)

    def ClickSearch(self):
        self.driver.find_element_by_id(self.buttonSearch_id).click()

    def GetNoOfRows(self):
        return len(self.driver.find_elements_by_xpath(self.tableRows_xpath))

    def GetNoOfColumns(self):
        return len(self.driver.find_elements_by_xpath(self.tableColumns_xpath))

    def searchCustomerByEmail(self,email):
        flag=False
        for r in range(1,self.GetNoOfRows()+1):
          table=self.driver.find_element_by_xpath(self.table_xpath)
          emailid=table.find_element_by_xpath("//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[2]").text
          if emailid == email:
              flag = True
              break
        return flag

    def searchCustomerByName(self,Name):
        flag=False
        for r in range(1,self.GetNoOfRows()+1):
          table=self.driver.find_element_by_xpath(self.table_xpath)
          name=table.find_element_by_xpath("//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[3]").text
          if name == Name:
              flag = True
              break
        return flag