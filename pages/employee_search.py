from common.left_pannel import LeftPanel
from core.condition.visible import Visible
from core.constants import Constants
from core.element import Element
from core.page import Page


class EmployeePage(Page):
    def __init__(self, context):
        path = "/Person"

        self.Dashboard_Employee_SearchEmployee_SearchField = Element(context, "//input[@name='txt']",
                                                                     Constants.XPATH)
        self.Dashboard_Employee_SearchEmployee_NewEmployee_HeaderTxt = Element(context,
                                                                               "//h4[normalize-space()='Employee Information']",
                                                                               Constants.XPATH)
        super().__init__(context, path, Element(context, "//a[normalize-space()='Employee']", Constants.XPATH))

    def click_on_search_employee(self):
        left_panel = LeftPanel(self.context)
        left_panel.return_dashboard_employee_toggle_element().click()
        left_panel.return_dashboard_search_employee_element().click()

    def return_dashboard_employee_search_employee_search_field(self):
        self.Dashboard_Employee_SearchEmployee_SearchField.should_wait_till(Visible(5))
        return self.Dashboard_Employee_SearchEmployee_SearchField

    def return_dashboard_employee_search_employee_new_employee_header_txt(self):
        self.Dashboard_Employee_SearchEmployee_NewEmployee_HeaderTxt.should_wait_till(Visible(5))
        return self.Dashboard_Employee_SearchEmployee_NewEmployee_HeaderTxt
