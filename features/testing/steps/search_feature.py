from behave import *

from pages.employee_search import EmployeePage
from pages.login_page import LoginPage

use_step_matcher("re")


@given(": Navigate to Home page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.loginPage = LoginPage(context, context.serverPath)
    context.loginPage.open()
    context.loginPage.return_uname_box_element().send_keys(context.user)
    context.loginPage.return_login_password_box_element().send_keys(context.password)



@when(": Enter the valid user credentials")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """



@when(": Click on Employee link")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.search = EmployeePage(context)
    context.search.click_on_search_employee()
    context.re

@when(": Enter the new SSN number into Search box field")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """



@step(": Click on Search button")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """



@then(": Emloyee result should not be displayed in the Search result")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """



@when(": Enter the Existing SSN number into Search box field")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """



@then(": Emloyee result should be displayed in the Search result")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """



@when(": Enter the new Last 4 Digit of SSN and Last Name into Search box field")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """



@when(": Enter the existing Last 4 Digit of SSN and Last Name into Search box field")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
