from behave import given,when,then

@then('Verify the Market page opens.')
def verify_market_page(context):
    context.app.market_page.verify_market_page()
@when('Click on the Add Company button')
def click_add_company_button(context):
    context.app.market_page.click_company_button()