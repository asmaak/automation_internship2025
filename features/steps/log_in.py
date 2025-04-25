from behave import given,when,then

@when('Log in to the page with {email} and {password}')
def log_in(context,email,password):
    context.app.log_in_page.log_in(email,password)