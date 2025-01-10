from core.constants import Constants
from core.element import Element
from core.page import Page
from core.condition.visible import Visible


class LeftPanel(Page):
    def __init__(self, context):
        path = "/Person"

        self.Dashboard_EmployeeToggle = Element(context, "//a[normalize-space()='Employee']",
                                                Constants.XPATH)
        self.Dashboard_Employee_SearchEmployee = Element(context, "///a[normalize-space()='Search Employee']",
                                                         Constants.XPATH)
        self.Dashboard_Employee_SearchEmployee_SearchField = Element(context, "//input[@name='txt']",
                                                                     Constants.XPATH)
        self.Dashboard_Employee_SearchEmployee_SearchBt = Element(context, "(//i[@class='fa fa-plus'])[1]",
                                                                  Constants.XPATH)
        self.Dashboard_Employee_SearchEmployee_NewEmployee_HeaderTxt = Element(context,
                                                                               "//h4[normalize-space()='Employee Information']",
                                                                               Constants.XPATH)
        super().__init__(context, path, Element(context, "//a[normalize-space()='Employee']", Constants.XPATH))

    def return_dashboard_employee_toggle_element(self):
        self.Dashboard_EmployeeToggle.should_wait_till(Visible(5))
        return self.Dashboard_EmployeeToggle

    def return_dashboard_search_employee_element(self):
        self.Dashboard_Employee_SearchEmployee_SearchBt.should_wait_till(Visible(5))
        return self.Dashboard_Employee_SearchEmployee_SearchBt
