from behave import given,when,then

@given ('Open the main page')
def open_main_page(context):
    context.app.main_page.open_main_page()

@when ('Click on {name_of_menu} at the left side menu')
def click_menu(context, name_of_menu):
    context.app.side_menu_page.click_menu(name_of_menu)