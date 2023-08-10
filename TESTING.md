# Flower House- Testing details

[Main README.md file](README.md)

[View the live project here](https://flowerhouse-3853febb8d54.herokuapp.com/)

## Table of content
## Automated Testing
### Validation:
- W3C Markup Validation HTML
  - [HTML Validator](https://validator.w3.org/#validate_by_input) was used to validate HTML.
  Result for Index.html:
    - [Validator Index.html ](media/test/result_html_validator_index.jpeg)
  Resultat for products.html:
    - [Validator products.html](media/test/resultat_html_products.jpeg)
  Result for ptoduct_detail.html:
    - [Validator product_detail.html](media/test/result_product_detail_html.jpeg)  
  Result for bag.html:
    - [Validator bag.html](media/test/result_bag_html.jpeg)
  Result for checkout_success.html:
    - [Validator checkout_success.html](media/test/result_html_checkout_success.jpeg)
  Result for blog_category.html:
    - [Validator blog_category.html](media/test/result_html_blog_category.jpeg)
  Result for florist_blog.html:
    - [Validator florist_blog.html](media/test/result_html_florist_blog.jpeg)

- W3C CSS validation CSS
  - [Validator.w3](https://validator.w3.org/nu/#textarea) was used to validate CSS.

  Result base.css:
    - [Base.css](media/test/base.css.jpeg)
    - [Blog.css](media/test/blog.css.png)

- JSHint JavaScript
  - [JSHint](https://jshint.com/) was used to validatw JS.

 [ Result stripe_elements.js](media/test/js.jpeg)

- Pep8 Python
  - [Python pep8](https://pep8ci.herokuapp.com/#) was used to validate Python code.

  -  Result for Bag bag_tools.py:
    - [Result Bag bag_tools.py ](media/test/result_pep8bagtools.png)
  - Result for Bag contexts.py:
    - [Result Bag contexts.py part1 ](media/test/result_pep8_contexts_part1.png)
    - [Result Bag contexts.py part2](media/test/result_pep8_contexts_part2.png)
  - Result for Bag urls.py:
    - [Result Bag urls.py ](media/test/result_pep8_bag_urls.png)
  - Result for Bag views.py:
    - [Result Bag views.py part1](media/test/result_pep8_bag_views_part1.png)
    - [Result Bag views.py part2](media/test/result_pep8_bag_views_part2.png)
    - [Result Bag views.py part3](media/test/result_pep8_bag_views_part3.png)
  - Result for Checkout admin.py:
    - [Result Checkout admin.py](media/test/result_pep8_checkout_admin.png)
  - Result for Checkout apps.py:
    - [Result Checkout apps.py](media/test/result_pep8_checkout_apps.png)
  - Result for Checkout forms.py:
    - [Result Checkout forms.py part1](media/test/result_pep8_checkout_forms_part1.png)
    - [Result Checkout forms.py part2](media/test/result_pep8_checkout_forms_part2.png)
  - Result for Checkout models.py:
    - [Result Checkout models.py part1](media/test/result_pep8_checkout_models_part1.png)
    - [Result Checkout models.py part2](media/test/result_pep8_checkout_models_part2.png)
    - [Result Checkout models.py part3](media/test/result_pep8_checkout_models_part3.png)
  - Result for Checkout signals.py:
    - [Result Checkout signals.py](media/test/result_pep8_checkout_signals.png)
  - Result for Checkout urls.py:
    - [Result Checkout urls.py](media/test/result_pep8_checkout_urls.png)
  Result for Checkout views.py:
    - [Result Checkout views.py part1](media/test/result_pep8_checkout_views_part1.png)
    - [Result Checkout views.py part2](media/test/result_pep8_checkout_views_part2.png)
    - [Result Checkout views.py part3](media/test/result_pep8_checkout_views_part3.png)
    - [Result Checkout views.py part4](media/test/result_pep8_checkout_views_part4.png)
    - [Result Checkout views.py part5](media/test/result_pep8_checkout_views_part5.png)
    - [Result Checkout views.py part6](media/test/result_pep8_checkout_views_part6.png)
    - [Result Checkout views.py part7](media/test/result_pep8_checkout_views_part7.png)
  Result for Checkout webhook_handler.py:
    - [Result Checkout webhook_handler.py part1](media/test/result_pep8_checkout_webhook_handler_part1.png)
    - [Result Checkout webhook_handler.py part2](media/test/result_pep8_webhook_handler_part2.png)
    - [Result Checkout webhook_handler.py part3](media/test/result_pep8_webhook_handler_part3.png)
    - [Result Checkout webhook_handler.py part4](media/test/result_pep8_webhook_handler_part4.png)
    - [Result Checkout webhook_handler.py part5](media/test/result_pep8_webhook_handler_part5.png)
    - [Result Checkout webhook_handler.py part6](media/test/result_pep8_webhook_handler_part6.png)
  Result for Checkout webhooks.py:
    - [Result Checkout webhooks.py part1](media/test/result_pep8_webhooks_part1.png)
    - [Result Checkout webhooks.py part2](media/test/result_pep8_webhooks_part2.png)
  Result for Home urls.py:
    - [Result Home urls.py](media/test/result_pep8_home_urls.png)
  Result for Home views.py:
    - [Result Home views.py](media/test/result_pep8_home_views.png)
  Result for Products admin.py:
    - [Result Products admin.py part1](media/test/result_pep8_products_admin.png)
    - [Result Products admin.py part2](media/test/result_pep8_products_admin_part2.png)
  Result for Products forms.py:
    - [Result Products forms.py](media/test/result_pep8_products_forms.png)
  Result for Product models.py:
    - [Result Products moedls.py part1](media/test/result_pep8_products_moedls_part1.png)
    - [Result Products moedls.py part2](media/test/result_pep8_products_models_part2.png)
    - [Result Products moedls.py part3](media/test/result_pep8_products_models_part3.png)
  Result for Products urls.py:
    - [Result Products urls.py](media/test/result_pep8_urls_products.png)
  Result for Product views.py:
    
    - [Result Product views.py part1](media/test/result_pep8_products_views_part1.png)
    - [Result Product views.py part2](media/test/result_pep8_products_views_part2.png)
    - [Result Product views.py part3](media/test/result_pep8_products_views_part3.png)
    - [Result Product views.py part4](media/test/result_pep8_products_views_part4.png)
    - [Result Product views.py part5](media/test/result_pep8_products_views_part5.png)
    - [Result Product views.py part6](media/test/result_pep8_products_views_part6.png)
    - [Result Product views.py part7](media/test/result_pep8_products_views_part7.png)
    - [Result Product views.py part8](media/test/result_pep8_products_views_part8.png)

  Result for Profile forms.py:
    - [Result Profile forms.py](media/test/result_pep8_profile_forms.png)

  Result for Profile models.py:
    - [Result Profile models.py part1](media/test/result_pep8_profile_models_part1.png)
    - [Result Profile models.py part2](media/test/result_profile_pep8_models_part2.png)

  Result for Profile urls.py:
    - [Result Profile urls.py](media/test/result_pep8_profile_urls.png)

  Result for Profile views.py:
    - [Result Profile views.py part1](media/test/result_profile_pep8_views_part1.png)
    - [Result Profile views.py part2](media/test/result_profile_pep8_views_part2.png)

  Result for Blog admin.py:
    - [Result Blog admin.py](media/test/result_pep8_blog_admin.png)  

  Result for Blog forms.py:
    - [Result Blog forms.py](media/test/result_pep8_blog_forms.png)
  
  Result for Blog models.py:
    - [Result Blog models.py part1](media/test/result_pep8_blog_models_part1.png)
    - [Result Blog models.py part2](media/test/result_pep8_blog_models_part2.png)

  Result for Blog urls.py:
    - [Result Blog urls.py](media/test/result_pep8_blog_urls.png)

  Result for Blog views.py:
    - [Result Blog views.py part1](media/test/result_pep8_blog_views_part1.png)
    - [Result Blog views.py part2](media/test/result_pep8_blog_views_part2.png)
    - [Result Blog views.py part3](media/test/result_pep8_blog_views_part3.png)  
  
  
## Manual Testing 


### User Stories Testing

1 USER STORY: SEO #1
  - As a **Site User** I can **find the site through web searches** so that I can **easily access the site**

    - Conted to meta name keywords have been updated. Thanks to this, the user is likely to quickly come across this page, because the keywords have been updated with the words that users most often use when searching for a flower boutique via google.
2 USER STORY: ERROR 404 OR 500 #2
  - As a **Site User efter http 404 or 500 response** I can **come back to the previous page and continue my shopping.**

    - Pages 404 and 500 have been updated so that the user can go back to the previous page and continue shopping.
3 USER STORY: Facebook page #3
  - As a **Site User** I can **go to the Facebook page to currently follow the news of products in the flower shop.**

    - The business Facebook page was created to attract more customers. It is updated so that all news, curiosities and discounts are available there.
4 USER STORY: Delete product #4
  - As a **Admin** I can **delete a product** so that **I can remove the product from the database.**
    - As an Admin, I have the ability to remove products right on the page.
5 USER STORY: Update details #5
  - As a **Admin** I can **edit or update details for a product**  so that **I can change the price.**
  - As a **Admin** I can **access to all products details**   
    - As an Admin, I have the ability to change the data entered into the product at any time, when the product properties change (such as: price, image, description, title,)  or it is necessary to add new properties.
6 USER STORY: Email confirmation #6
  - As a **Site User** I can **receive an email confirmation after checking out** so that **I have saved my purchases.**
    - An email confirming the purchases made by the user is sent as soon as the order is completed.
7 USER STORY: Total price #7
  - As a **Site User** I can **get confirmation after shopping** so that **I can see the total price.** 
    - The price of the products is calculated as soon as the product is added to the basket, by going to the basket page by the user, the user has the opportunity to see the final price of all products added to the basket.
8 USER STORY: Payment details #8
  - As a **Site User** I can **enter my payment details** so **them keep safe.** 
    - When the user has made a shopping list and wants to go further to the payment page, the data is entered in a secure way.
9 USER STORY: Checkout page #9
  - As a **Site User** I can **move on to the checkout page** so that **I can see the list of my purchases, total price** and also **enter my address details.**
  10 USER STORY: Manage shopping bag. #10
  - As a **Site User** I can **manage my shopping bag** so that **I can insert products I want to buy** and also **remove them from the shopping bag.** 
   - As a **Site User** I can **enter the number of products in the bag** so that I **can easily change the quantity** and **move on to the payment page.**
    - The checkout page is structured in a specific way so that the user has the ability to check all purchases added to the basket, has the option of removing them from the basket, or adding a quantity of products. Then the user also has the option to see the price and, going further, to enter users address details.

11 USER STORY: Search #11
  - As a **Site User** I can **use the search function** so that **I can see if the product I am looking for is available.**
    - The search option is added so that the user can find what she/ he needs in a very simple way. -The user can search for a specific product, or just any word that is used in the product description.

13 USER STORY: Selecting product #13
  - As a **Site User** I can **see pictures of all products** so that **I can select one of them** and **see product details.**
    - The product detail page is designed so that the user can see a detailed description of the product, as well as the product title, price, category in which the product is located, rating, the ability to enter the quantity of the product ordered. Finally, the user has the option to choose to continue to the shopping cart page or stay on the product page.
14 USER STORY: Profil page #14
  - As a **Site User** I can **log in into the profil page** and **enter personal details.**
    - By using the options in the navigation bar on the right, there is a dropdown. By pressing on this option, the user has the option to select 'My profile'. Going to this page, the user can see a form. While completing the form, the user should enter: Phone Number, Street Address 1, Street Address 2, Town or City, Country State or Locality, Postal Code, Country. By filling out the form, the user has the opportunity to quickly complete orders for future purchases on the website.
19 USER STORY: Registration #20
  - As a **Site User** I can **register an account**
  - As a **Site User** I can **register** by **entering my email, password and confirming my password.**
  - As a **Site User** I can **register or login** so that **I can manage my booking requests.**
  - As a **Story User** I can **log into the website** by **entering my email/username and password**
  - As a **Site User** I can **get an email with my password if I had forgotten it** so that I can log in again.
    - The layout of the Flower House Log in/log out Page is built in the following way:
      - On the sign up page, the user is required to provide the contact phrase so that later can easily log in to the login page using the username and password.
      - Wanting to fulfill orders without being logged in, a message is displayed that the user must first log in.
21 USER STORY: Navigation bar #22
  - As a **Site User** I can **use navigation menu** to **switch to other options**
    - on the left side, in the first place, there is an option: 'About us', after pressing it, the user can see information about the florist.
- another of the option is a blog, where the user can see the news about the florist, as well as discounts and other curiosities.
- next is a dropdown called: 'Shop' from the behavior of products for sale.
- after that there is the 'search' option where the user can search for a specific product, or just any word that is used in the product description, by which the user can easily find what needs.
- If the user is not authenicated, he/she should see two buttons on the right side:
    - Log in
    - Sign up
If the user is authenicated, on the right side should be:
     - dragdown with the user's icon and the username, after pressing on it, the user can choose one of the options:
        - User Profile
        - Log out
    - icon with a handbag, after pressing on it, the user can go to the page with the list of products that the user has added to the basket.

### Testing on desktop
All steps are performed in browsers:
- Chrome - Version 111.0.5563.65 (Officiell version) (64 bitar)
- Microsoft Edge - Version 111.0.1661.44 (Officiell version) (64 bitar)
- Firefox - 111.0 (64-bitars)

#### This has been verified on every page:
- Navigation bar:
  - Hover over each link has been made. The effect has been confirmed to be correct.
  - The 'FLOWER HOUSE' logo has been pressed and confirmed to take the user to the Home page.
  - The drapdown SHOP has been pressed and confirmed that the following options openeds up:
    - Birthday Flowers
      - The 'Birthday Flowers' has been pressed and confirmed to take the user to the Products page with category 'Birthday Flowers'.
    - Bouquets
      - The 'Bouquets' has been pressed and confirmed to take the user to the Products page with category 'Bouquets'.
    - Wedding Flowers
      - The 'Wedding Flowers' has been pressed and confirmed to take the user to the Products page with category 'Wedding Flowers'.
    - All Products
      - The 'All products' has been pressed and confirmed to take the user to the Products page with all products aviliable.

  - The BLOG page link has been pressed and confirmed to take the user to the BLOG page.
  - The ABOUT US page link has been pressed and confirmed to take the user to the ABOUT US page.
  - The 'Search' option has been pressed and suggested word like: 'roses' or 'tulips' has been passed, and after pressing enter ha been  confirmed to take the user to the responsive page.

  If user is authenticated:
    - The  drapdown {{ user }} has been pressed and confirmed that the following options openeds up: 
      - Product Management
      - My Profile
        - The 'My Profile' page link has been pressed and confirmed to take the user to the My Profile page.
      - My Bag
        - The 'My Bag' page link has been pressed and confirmed to take the user to the My Bag page.
      - Logout
        - The 'Logout' page link has been pressed and confirmed to take the user to the Logout page.
  If user is not authenticated:
     - The  drapdown {{ user }} has been pressed and confirmed that the following options openeds up:
        - Register
          - The Register link has been pressed and confirmed to take the user to the responsive page.
        - Login 
          - The Login link has been pressed and confirmed to take the user to the responsive page.

- Footer:
  - It has been verified that the footer is displayed as expected.

#### Home Page (Logo 'FLOWER HOUSE'):
  1. Home Page Image:
    - It has been confirmed that the main image on the site is clear and shows up after the page loads.
    - It has been confirmed that the main page on the home page have been verified to be the correct size.

  2. Home Page Text
    - It has been confirmed that the title and text are correct and display correctly.
    - It has been confirmed that button 'Send Flowers' are correct and display correctly and change color by hovering over it.

#### Products, Category 'Birthday Flowers' Page:
  1. Products- Category 'Birthday Flowers' Page Images:
    - It has been confirmed that the main image to category 'Birthday Flowers' on the site is clear and shows up after the page loads.
    - All products images belonged to category 'Birthday Flowers' have been reviewed and verified to be the correct size and shows up after the page loads.

  2. Products- Category 'Birthday Flowers' Page Text:
    - It has been confirmed that the title and description of category 'Birthday Flowers' are correct and display correctly.
    - It has been confirmed that the title, price, rating of prodcuts belonged to category 'Birthday Flowers' are correct and display correctly.
    - if request user is superuser, the option 'Edit' and *Delete' to all products in the category are correct and display correctly.
      - It has been confirmed that after the option 'edit' has been pressed, the page 'edit product' is displaing correctly and editing of a products is possible.

#### Products, Category 'Bouquets' Page:
  1. Products, Category 'Bouquets' Page Images:
    - It has been confirmed that the main image to category 'Bouquets' on the site is clear and shows up after the page loads.
    - All products images belonged to category 'Bouquets' have been reviewed and verified to be the correct size and shows up after the page loads.

  2. Products, Category 'Bouquets' Page Text:
    - It has been confirmed that the title and description of category 'Bouquets' are correct and display correctly.
    - It has been confirmed that the title, price, rating of prodcuts belonged to category 'Bouquets' are correct and display correctly.
    - if request user is superuser, the option 'Edit' and *Delete' to all products in the category are correct and display correctly.
      - It has been confirmed that after the option 'edit' has been pressed, the page 'edit product' is displaing correctly and editing of a products is possible.

#### Products, Category 'Wedding Flowers' Page:
  1. Products, Category 'Wedding Flowers' Page Images:
    - It has been confirmed that the main image to category 'Wedding Flwers' on the site is clear and shows up after the page loads.
    - All products images belonged to category 'Wedding Flowers' have been reviewed and verified to be the correct size and shows up after the page loads.

  2. Products, Category 'Wedding Flowers' Page Text:
    - It has been confirmed that the title and description of category 'Wedding Flowers' are correct and display correctly.
    - It has been confirmed that the title, price, rating of prodcuts belonged to category 'Wedding Flowers' are correct and display correctly.
    - if request user is superuser, the option 'Edit' and *Delete' to all products in the category are correct and display correctly.
      - It has been confirmed that after the option 'edit' has been pressed, the page 'edit product' is displaing correctly and editing of a products is possible.

#### Products Page, option 'All products':
  1. Products Page, option 'All products' Images:
    - All products images have been reviewed and verified to be the correct size and shows up after the page loads.

  2. Products Page, option 'All products' Text:
    - It has been confirmed that the title, price, rating of all prodcuts are correct and display correctly.
    - if request user is superuser, the option 'Edit' and 'Delete' to all products are correct and display correctly.
      - It has been confirmed that after the option 'edit' has been pressed, the page 'edit product' is displaing correctly and editing of a products is possible.             

#### Blog Page:
  1. Blog Page Images:
    - It has been confirmed that the all images on the site is clear and shows up after the page loads.
    - All pictures on the home page have been reviewed and verified to be the correct size.

  2. Blog Page Text:
    - It has been confirmed that the title and text are correct and display correctly.

  3. Blog Category:
    - It has been confirmed that the categories of post on the blog with post title and current category image are correct and display correctly.

#### About Us Page:
  1. About Us Page Images
    - It has been confirmed that the main image on the site is clear and shows up after the page loads.
    - All pictures on the 'About Us' page have been reviewed and verified to be the correct size.

  2. About Us Page Text
    - It has been confirmed that the title and text are correct and display correctly.

#### Log in

1. Log in Page Image next to the form
    - It has been confirmed that the main image on the site is clear and shows up after the page loads.

2. Log in Page Text
    - It has been confirmed that the title and text are correct and display correctly and on correctly place.

3. Log in Page Form
    - It has been confirmed that the online booking page form is laid out as expected.
    - It has been confirmed that if a user submits a form without filling out the required fields, a message is shown to complete them.
     - It has been confirmed that it shows a message with a valid username if the user enters a name other the username in the username input field.
     - It has been confirmed that it shows a message with a valid password if the user enters a name other the password in the password input field.
    - it has been confirmed that after completing the form correctly and pressing submit, the user will go to the home page.

#### Sign Up

1. Sign Up Page Image next to the form
    - It has been confirmed that the main image on the site is clear and shows up after the page loads.

2. Log in Page Text
    - It has been confirmed that the title and text are correct and display correctly and on correctly place.

3. Log in Page Form
    - It has been confirmed that the online booking page form is laid out as expected.
    - It has been confirmed that if a user submits a form without filling out the required fields, a message is shown to complete them.
     - It has been confirmed that it shows a message with a valid e-mail address if the user enters a name other the e-mail address in the e-mail input field.
     - Confirmed to display a message with the correct password if the user enters a different password than the first time, or if the password does not match the required arrangement.
    - it has been confirmed that after completing the form correctly and pressing submit, the user will go to the home page.

#### Log out Page

1. Log out Page Text
    - It has been confirmed that the title and text are correct and display correctly and on correctly place.
    - The button works properly, and after pressing log out button, the user is logged out.

