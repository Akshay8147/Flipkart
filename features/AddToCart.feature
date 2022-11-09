Feature: add to cart flipkart
    Scenario Outline: add to cart data
      Given we navigate to flipkart
      Then close the popup
      When click login
      Then we type "<username1>" field
      And we type in "<password1>" the field
      Then we click on the sign in button
      And we have to type "<search1>" field
      Then click on the search button
      And click on the product
      Then check on add to cart button is clickable
      Then check on plus button is clickable
      Then check on minus button is clickable
      Then check on save for later button is clickable
      Then check on remove button is clickable
      Then check it is removed

      Examples:
        | username1 | password1 | search1 |
      | 6362771063 | Akshay@8147 | clock |

