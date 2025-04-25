from behave import given,when,then

@then('Verify the right page opens')
def verify_right_page(context):
    context.app.presentation_agency_page.verify_page_open()

@then('Verify the button Publish my company is available')
def verify_button_publish_my_company_is_available(context):
    context.app.presentation_agency_page.verify_button_publish_my_company_is_available()