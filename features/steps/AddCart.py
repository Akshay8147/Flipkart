from behave import *
from Utilities.configreader import ConfigReader
from features.pageobject.AddToCart import Addtocart

@given(u'we navigate to flipkart')
def step_impl(context):
    context.AddToCart = Addtocart(context.driver)
    context.AddToCart.OpenPage(ConfigReader("base info", "URL"))

@then(u'close the popup')
def step_impl(context):
    context.AddToCart.clickclose()

@when(u'click login')
def step_impl(context):
    context.AddToCart.Click_loginhomepage()

@then(u'we type "{username1}" field')
def step_impl(context, username1):
    context.AddToCart.Enter_Username(username1)

@then(u'we type in "{password1}" the field')
def step_impl(context, password1):
    context.AddToCart.Enter_password(password1)

@then(u'we click on the sign in button')
def step_impl(context):
    context.AddToCart.Click_login()


@then(u'we have to type "{search1}" field')
def step_impl(context, search1):
    context.AddToCart.text_Searchbar(search1)


@then(u'Click on the search button')
def step_impl(context):
    context.AddToCart.Click_SEARCHBUTTON()


@then(u'Click on the Product')
def step_impl(context):
    context.AddToCart.Click_PRODUCT()


@then(u'check on add to cart button is clickable')
def step_impl(context):
     context.AddToCart.Click_ADDTOCART()


@then(u'check on plus button is clickable')
def step_impl(context):
    context.AddToCart.Click_PLUSBUTTON()


@then(u'check on minus button is clickable')
def step_impl(context):
    context.AddToCart.Click_MINUSBUTTON()


@then(u'check on save for later button is clickable')
def step_impl(context):
    context.AddToCart.Click_SAVEFORLATER()


@then(u'check on remove button is clickable')
def step_impl(context):
    context.AddToCart.Click_REMOVE()

@then(u'check it is removed')
def step_imp(context):
    context.AddToCart.Click_END()