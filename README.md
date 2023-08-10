# Flower house

[View the live project here](https://flowerhouse-3853febb8d54.herokuapp.com/)
Here is the E-commerce Applications for Flower House created in Django for Portfolio Project 5 - Python + Django Essentials for Diploma in Full Stack Software Development at [Code Institute](https://codeinstitute.net/se/).

Here is a project built with a full stack site based on business logic used to control a central dataset. The mechanism is configured for authentication and provides paid access to site data and data such as product purchase.


This is e-commerce application which is built to make it easy for customers to find the products they are looking for. There sells bridal bouquet, flower bouquets, summer flowers, cut flowers, roses, tulips and pots. The products are placed in different categories, so that the customer can easily find what they are looking for. The customer can also create their own bouquet by filling out a simple form. The site is designed to encourage the customer to buy.

 # Table of content

 # User Experience (UX)
## USER STORIES:

[Kanban board](https://github.com/users/mariaarnesson/projects/18/views/1) with my defined [USER STORIES](https://github.com/mariaarnesson/florist_shop/issues) and their acceptance criteria are available here.

- USER STORY: SEO #1
  - As a **Site User** I can **find the site through web searches** so that I can **easily access the site**
- USER STORY: ERROR 404 OR 500 #2
  - As a **Site User efter http 404 or 500 response** I can **come back to the previous page and continue my shopping.**
- USER STORY: Facebook page #3
  - As a **Site User** I can **go to the Facebook page to currently follow the news of products in the flower shop.**
- USER STORY: Delete product #4
  - As a **Admin** I can **delete a product** so that **I can remove the product from the database.**
- USER STORY: Update details #5
  - As a **Admin** I can **edit or update details for a product**  so that **I can change the price.**
- USER STORY: Email confirmation #6
  - As a **Site User** I can **receive an email confirmation after checking out** so that **I have saved my purchases.**
- USER STORY: Total price #7
  - As a **Site User** I can **get confirmation after shopping** so that **I can see the total price.** 
- USER STORY: Payment details #8
  - As a **Site User** I can **enter my payment details** so **them keep safe.** 
- USER STORY: Checkout page #9
  - As a **Site User** I can **move on to the checkout page** so that **I can see the list of my purchases, total price** and also **enter my address details.**
- USER STORY: Manage shopping bag. #10
  - As a **Site User** I can **manage my shopping bag** so that **I can insert products I want to buy** and also r**emove them from the shopping bag.** 
- USER STORY: Search #11
  - As a **Site User** I can **use the search function** so that **I can see if the product I am looking for is available.**
- USER STORY: Selecting product #13
  - As a **Site User** I can **see pictures of all products** so that **I can select one of them** and **see product details.**
- USER STORY: Profil page #14
  - As a **Site User** I can **log in into the profil page** and **enter personal details.**
- USER STORY: Password #15
  - As a **Site User** I can **get an email with my password if I had forgotten it** so that I can log in again.
- USER STORY: Quanity of products #16
  - As a **Site User** I can **enter the number of products in the bag** so that I **can easily change the quantity** and **move on to the payment page.**
- USER STORY: User can log in #18
  - As a **Site User** I can **register or login** so that **I can manage my booking requests.**
- USER STORY: Account registration: #19
  - As a **Site User** I can **register an account**
- USER STORY: Registration #20
  - As a **Site User** I can **register** by **entering my email, password and confirming my password.**
- USER STORY: Login #21
  - As a **Story User** I can **log into the website** by **entering my email/username and password**
- USER STORY: Navigation bar #22
  - As a **Site User** I can **use navigation menu** to **switch to other options**
- USER STORY: Admin account #23
  - As a **Admin** I can **access to all products details**


# Features
## Existing Features

### Navigation bar   
Below are descriptions of the main features of the application. Many of the features are based on the Boutique Ado walkthrough project and SEO and Web Marketing modules of the course.

The navigation bar is structured as follows:
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

- This is what the navigation bar looks like when a user is logged in:
![nav logged in](media/navigation_bar_user_loggedin.png)

- This is what the navigation bar looks like when a user is not logged in:
![nav user not logged in](media/navigation_bar_user_not_logged_in.png)

#### Home Page

#### Prodcts Page
- In a very simple way, using the navigation bar, the user can see all the products, or if she/ he prefers, go straight to a specific category, or use the search option to find what the user wants. The list of products available on the page for purchase includes: product name, price, category, rating. At the top of the page can user also see how many products are on the page.

##### All Products:
![products categories](media/products_categories.png)
![all products](media/all_products.jpeg)


##### Products Categories
  When the user selects one of the categories, the category photo, title and description are displayed. All products from the given category are displayed below:

  - Products in category Birthday flower.
  ![birthday flowers](media/birthday_flowers.jpeg)

   - Products in category Bouquets.

  ![bouquets category all products](media/bouquets.jpeg)
  

  - Products in category Wedding flowers.

  ![wedding flowers all products](media/wedding_flowers.jpeg)

### Product Detail Page

On the product details page, the user has access to see a larger size image of the product, and other details such as: 
  - a heart icon which make a user possibility to add a product to favorites page.
  - title of the product
  - price of the product 
  - product's category
  - rating
  - product's description

 Below that the user has the opportunity to rating the product and leave own review. 
 Below that is the possibility to order a quantity of the product. 
 At the very end, the user should choose whether he/she wants to continue to the page with the ordered products, or stay on the product page to add more products to the basket.

#### If a user is not authenticated:

A user who is not logged in can see the products existing on the site and the product details page. The user cannot leave a review before logging in.
![prodcut detail user is not authenicated](media/product_detail_user_not_authenicated.jpeg)

When the user presses the heart icon, the modal with the message below is displayed:
![modal favorites](media/modal_favorites.png)

However, if the user presses the 'ADD TO BAG' button, the product will be added to the bag even if the user is not logged in to give the opportunity to make a purchase without logging in.

#### If a user is authenticated:

- Favorites 

To add a product to favorites, the user needs to press the heart icon located next to the image of the product, and then even the heart icon in the navigation bar leading to the favorites page turns to red, and the message: 'The product has been added to your favorites.' shows up.

![Adding to favorite](media/add_to_favorites.png)

To remove a product from the favorites page, a user need to just press the heart icon again.

![Ramoving from favorite](media/removed_from_favorite.png)

This is what the favorites page looks like. By clicking on the image, name or price of the product, the user goes to the product details page, and by clicking on the 'x' the product is removed from the favorites page.
![Favorites Page](media/favorites_page.png)


- Review

When a user is logged in, he has the ability to leave a review, edit and delete it. 

![Review ](media/review_product.jpeg)

By pressing the 'Write a Review' button, a modal shows where the user can rate on a scale of 1-5 how much they rate the product and also write their opinion in the field: 'Write your review here...'. By pressing button 'Submit Review', a message 'Review added successfully!' is displaing.

![Add a review](media/add_a_review.png)

To make changes to a posted opinion, the user has the option to press 'edit', then the modal reappears and the user has the option to re-enter his opinion. By pressing button 'Save Changes', a message 'Review updated successfully.' is displaing.

![Edit review product](media/edit_review_product.png)

To delete a review, the user just needs to press 'Delete' and the review will be deleted and the message 'Review deleted successfully.' will be displaing.

####  if request user is superuser

If the user is the administrator of the site, has the option to delete reviews that other users have posted, and this is what the review page in product detail looks like:

![Review admin ](media/reviews_admin.png)

### My Profile Page

On the My Profile Page, the user has the option to enter contact details and save them. In this way, the user does not have to enter them again while going to the checking.html page after putting the products to the bag. On My Profile Page there are also orders that have already been completed by the user before.

![My Profile Page](media/my_profile_page.png)

### Shopping Bag Page

The icon in the navigation bar resembling a bag is a link to the shopping bag page. Under the icon, the total price is shown after putting the products into the bag, and the color of the bag turns to red when the products are inside. By pressing the bag icon, we go to the shopping bag page. 

This is what the page looks like when the bag is empty: 
![empty bag](media/bag_empty.png)

This is what it looks like when products are added to the bag:
![shopping bag](media/shopping_bag.jpeg)

### Checkout Page

On the Shopping Bag Page with the products added by the user, we have the option of pressing the 'SECURE CHECKOUT' button. By doing so, the user is taken to the checkout.html page.

![Checkout Page](media/checkout_page.jpeg)

By completing the provided form by entering the user's name and payment card number, the user need to press the 'Complete Order' button. Then the Page Checkout Success is displaing. This page provides the details of the order and the user's contact details, as well as a notice that the user will receive a confirmation email at the email address provided:

![Chackout Success Page](media/checkout_success.jpeg)

The content of the confirmation email looks like this:

![Confirmation Email](media/confirmation_email.png)


### Product Management

On the 'Product Management' page, the Site Administrator has the ability to add, edit or remove a product available for purchase.

![Add product](media/add_product_management.jpeg)

![Edit Product](media/edit_product.jpeg)

### Blog Page


![blog categories](media/blog_categories.png)

- Category Flowers Interior Decor:
![poat3](media/post3.png)
![post3 detail](media/post3_detail.jpeg)


- Category About Flowers:

![post1](media/post1.png)
![post1 detail](media/post1_detail.jpeg)
![post4](media/post4.png)
![post4 detail](media/post4_detail.jpeg)

- Category Flower Tips
![post2](media/post2.png)
![post2 detail](media/post2_detail.jpeg)

## Diagram

![Diagram](media/diagram.png)

## Wireframes
- [Home Page- Desktop](media/wireframes/homepage_desktop.png)
- [Products- Desktop](media/wireframes/products_desktop.png)
- [Product Detail Desktop](media/wireframes/product_detail_desktop.png)
- [Favorites Desktop](media/wireframes/favorites_desktop.png)
- [Product management- desktop](media/wireframes/product_management_desktop.png)
- [Favorites Ipad](media/wireframes/favorites_ipad.png)
- [Homepage Ipad](media/wireframes/homepage_ipad.png)
- [Product Ipad](media/wireframes/products_ipad.png)



# Testing 

Testing information can be found in separate [TESTING.md](TESTING.md) file. 

# Deployment:


## Deploying the app to Heroku

### Create a Heroku app.
To create a [Heroku](https://dashboard.heroku.com) application, after log in, on the main page you should press the button: 'New', which is located on the upper right side. From the dropdown you should select: 'Create new app' option. Then you go to the next page, where you should fill a form with the following data: 'App name' and 'Choose a region', and then you should press button: 'Create app'.

Once the Heroku app is created, the next step is to go to option: 'settings'. In the category called 'Config Vars', you should press 'Reveal Config Vars' button, and then you have possibility to enter the KAY and VALUE for individual properties of:

- DATABASE_URL:

To create DATABASE_URL, you need log in to the [ElephantSQL](https://www.elephantsql.com/). On the top right side of this page, you need to press button: 'Creata New Instance'. Then you need to fill out a short form, where you select a plan and name. After that you should press 'Select Region'button. After entering the region, press the button: 'review' and then your instance is created. On your instance's panel, you can see the details. Then you should copy the link, which is placed next to option 'URL'. 

This link is needed to enter as VALUE to KEY - DATABASE_URL to Config Vars on Heroku.

- SECRET_KEY

To create a SECRET_KEY you can use the [Django Secret Key Generator](https://miniwebtool.com/django-secret-key-generator/). You should press a button: 'Generate Django Secret Key' and copy Generated Django Secret Key.

This key is needed to enter as VALUE to KEY - SECRET_KEY to Config Vars on Heroku.


- DISABLE_COLLECTSTATIC

Value of DISABLE_COLLECTSTATIC should be 1

- STRIPE_PUBLIC_KEY and STRIPE_SECRET_KEY:

To create STRIPE_PUBLIC_KEY and STRIPE_SECRET_KEY you need to log in to [Stripe](https://dashboard.stripe.com/). On the top right site is a button 'developer' which you should press. in the API-key option, scrolling down, there is your public and secret key that you should enter into Heroku.

- STRIPE_WH_SECRET

On the same page, by selecting the 'Webhooks' option, you go to the page where you can create an endpoint. By pressing the 'Add a endpoint' button, a form to be filled is displayed. In the first field marked Endpoint URL, you should enter the link to your website in Heroku, adding at the end: '/checkout/wh'. Then select receive all events and press the button: 'add endpoint'.
After clicking on the endpoint you created, next to the option: Signature secret, select: 'show', and then the value of STRIPE_WH_SECRET appears, which you should enter into Heroku Config Vars.


## Creating a respository on GitHub

[GitHub Full Template](https://github.com/Code-Institute-Org/gitpod-full-template) was used to create my project. The green dropdown placed on the top right side on this page: 'Use this template' was pressed. After that 'Create a new respository' button was selected. After that you will be taken to another page, on a tab: 'Owner*', is your username selected, on a tab: 'Repository name*' you should give a name to your repository. Bellow that, in a tab 'Description (optional)' you have possibility to give your repository a short description.
Below that, there is an option to choose to make your repository private or public.
Finally, when everything is filled, you should press the button: 'Create repository'.

On the [GitPod Page](https://gitpod.io/workspaces), on the top right side, there is a button: 'New Workspace'. After selected that, you can add a new workspace. In a tab 'Select a repository', you can paste URL link to your repository, which you have built before. After that, eneter button 'Continue', and the workspace will start to build. You have to wait a while the workspace builds up.
Next you should install Django and supporting libraries:
1. Install Django and gunicorn with command in terminal: 'pip3 install django gunicorn'
2. Install supporting libraries with command in terminal: 'pip3 install dj_database_url psycopg2'
3. Install 'pip3 install django-storages'
4. Create requirements file with command in terminal: 'pip3 freeze --local > requirements.txt'
5. Create Project with command in terminal: 'django-admin startproject PROJ_NAME .'
6. Create App with command in terminal: 'python3 manage.py startapp APP_NAME'

Now you should create a new env.py file on top of directory level and include database:
- import os library by typing 'import os' on the top in env.py file.
- now you should set environment variables by typing:
    - os.environ["DATABASE_URL"] = "Paste the same value as pasted in Heroku Config Vars"
    - os.environ["SECRET_KEY"] = "Paste the same value as pasted in Heroku Config Vars"
    - os.environ["DEVELOPMENT"] = "1"

After logged in into [Stripe](https://dashboard.stripe.com/), in terminal you should add:
- export STRIPE_PUBLIC_KEY=(provide your stripe public key value)
- export STRIPE_SECRET_KEY=(provide your stripe secret key value)

You should create a new endpont to webhook and add to the terminal:
- export STRIPE_WH_SECRET=(provide your webhook public key value)    

Now you should create Procfile on the top level directory and type 'web: gunicorn PROJ_NAME.wsgi'.

## Set up Amazon Web Services' S3
The steps were done using [AWS setup new UI](https://codeinstitute.s3.amazonaws.com/fullstack/AWS%20changes%20sheet.pdf).

Creta a account on [AWS Amazon](https://signin.aws.amazon.com/). 
1. On the top left, press the 'Services' option and then 'S3'. 
2. When the column: 'Amazon S3' appears on the left, select the first option: 'Basket'. Then press the orange 'Create bucket' button on the right side. Fill out the form with the name of the bucket and the location that is closest to you. Going down, select: 'Block all public access'. Then press the orange 'Create bucket' button at the bottom of the page. 
3. In the bucket you created:  
  - select the 'Properties' option and by going to the bottom of site, on 'Static website hosting' option, press the 'edit' button. Then select: 'Static website hosting', and in the form, in the place of index document, enter 'index.html', and in the place of error document, enter error.html. Then press the 'Save' button.
  - select the 'Permissions' option and choose:
    -  'Cross-origin resource sharing (CORS)'and enter it in the field provided:
        [
      {
          "AllowedHeaders": [
              "Authorization"
          ],
          "AllowedMethods": [
              "GET"
          ],
          "AllowedOrigins": [
              "*"
          ],
          "ExposeHeaders": []
      }
    ]
    - Then select 'Bucket Policy'. At the bottom of the page, select 'Policy generator'. Now the page titled 'AWS Policy Generator' is displayed. In the first 'Select Type of Policy' field, select 'S3 Bucket Policy'. For 'Effect', select 'Allow'. For 'Principal', select '*', For 'AWS Service', select 'Amazon S3'. Under 'Actions', select 'GetObject'. Then copy this policy into the bucket policy editor and paste into 'Amazon Resource Name (ARN)'. Press the 'Add Statement' button. And then the 'Generate Policy' button. Copy the policy JSON Document that then shows up and paste the into the previous page 'Bucket policy editor'. Then press the 'Save' button.

4. On the top left, press the 'Services' option and then 'IAM'. 
5. When the column: 'Identity and Access Management (IAM)' appears on the left, select the option: 'Groups' and after that 'Creata New Group' button. After that set group name and press button 'Next Step'. 
6. On the left select te option 'Create policy', select option 'JSON', 'Import Managed policies' and search after 's3', from following options choose 'AmazonS3FullAccess' and choose button 'Import'. 
7. In 'Create policy' JSON code add 'Amazon Resource Name (ARN)' and add '/*'
8. In 'Review Policy' add a name, add description and then a message to confirm that the policy has been created is displaing. 
9. then press button 'Atach Policy'. 
10. Press button 'add user' and select access type programmatic access. When user is added, you can download 'csv. 
11. In downloaded file your AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY is displaing and you need to add the values of them to Heroku config vars. 



- Create an AWS Account by going to aws.amazon.com.
- Create a new bucket, give it a name and choose the region which isnclosest to you.
- Uncheck Block all public access, to make bucket public.
- From Object Ownership, make sure to have ACLs enabled, and Bucket owner preferred selected.
- From the Properties tab, turn on static website hosting, and type index.html and error.html in their respective field and save that.
- Paste in the following CORS configuration to the Permissions tab:
[
	{
		"AllowedHeaders": [
			"Authorization"
		],
		"AllowedMethods": [
			"GET"
		],
		"AllowedOrigins": [
			"*"
		],
		"ExposeHeaders": []
	}
]

Copy your ARN string.

From the Bucket Policy tab, select the Policy Generator link, and use the following steps:

Policy Type: S3 Bucket Policy

Effect: Allow

Principal: *

Actions: GetObject

Amazon Resource Name (ARN): paste-your-ARN-here

Click Add Statement

Click Generate Policy

Copy the entire Policy, and paste it into the Bucket Policy Editor

{
	"Id": "Policy1234567890",
	"Version": "2012-10-17",
	"Statement": [
		{
			"Sid": "Stmt1234567890",
			"Action": [
				"s3:GetObject"
			],
			"Effect": "Allow",
			"Resource": "arn:aws:s3:::your-bucket-name/*"
			"Principal": "*",
		}
	]
}
- add /* to the end of the Resource key in the Bucket Policy Editor (like above) and save.

- From the Access Control List (ACL) section, click "Edit" and enable List for Everyone (public access), and accept the warning box.

- If the edit button is disabled, you need to change the Object Ownership section above to ACLs enabled (mentioned above).

- Download the CSV file with the secret keys.


## Connecting the Heroku application to the GitHub repository

On the [Heroku page](https://dashboard.heroku.com), select the panel of your application that you have already created and press 'deploy'. Under the 'Deployment method' category, select the option: 'Connect to GitHub'. Below you will find: 'Search for a repository to connect to'. Bellow that enter your GitHub username, and your repository name, then press button: 'Search'. Underneath you should see the name of your GitHub respository and a 'Connect' button. Now there are two options to choose: either use 'Automatic deploys' or 'Manual deploy'.

I use the option: 'Manual deploy'. Next to a option: 'Choose a branch to deploy', select: 'main' and press button: 'Deploy Branch'. You have to wait a while while branch main builds up. When the branch is build and completed successfully, you will see a message: 'Your app was successfully deployed' and a button: 'View'. Enter 'View' to see the live project.
The live link can be found here - [View the live project here](https://flowerhouse-3853febb8d54.herokuapp.com/).




## The final steps that should be taken to deploy the application:

- The application can be prepared for Heroku deployment, when code changes have been completed and tested on localhost.

    - in settings.py the DEBUG flag should be set to False.
    - in settings.py 'X_FRAME_OPTIONS' should be set to 'SAMEORIGIN'.
    - use the command: 'pip3 freeze --local > requirements.txt' to make the requirements.txt file up-to-date.
    - Config Vars 'DISABLE_COLLECTSTATIC' in Heroku should be now deleted. 
    - On the Heroku dashboard go to the Deploy tab for the application and click on deploy branch.


## Detailed desciption steps to clone the repository:
- go to this page: https://flowerhouse-3853febb8d54.herokuapp.com/
- press button 'Code' and copy the link placed under HTTPS.
- after opening GitBush terminal, you should navigate to the directory and locate the clone. 
- to begin the clone process, on the command line, type "git clone" then paste in the copied url and press the Enter key.
- use the command : pip install -r requirements.txt to install the packages required by the application. 
- set DEBUG=True in the settings.py file, to developing and running the application locally.
- using the following commands, changes made to the local clone can be pushed back to the repository:
    - git add . (or filenames)
    - git commit -m "describe a message with changes that have been made"
    - git push
- N.B. Any changes pushed to the master branch will take effect on the live project once the application is re-deployed from Heroku

# SEO
To find the relevant keywords for my project I made the following searches on Google and Word Tracker along with a few combinations:

- Flower shop
- Flowers
- Bouquets 
- Sale 
- London 
- Home delivery 
- Occassions 
- Buy online 
- Summer flowers
- Flower for every occassion
- Create your own bouquets
- Florist in the heart of London
- A section of beautifule flowers for wedding
- Fresh products delivered to your home

Of the above, the top combination of searches I found were: 

- Flower shop near me
- Send flowers
- Unique bouquets
- Home delivery flowers London
- Special occassion
- Spring wedding flowers UK
- Sale florist
- London flowers delivery
- Bouquets of flowers
- Long-lasting summer flowers
- Flower for every session
- Flowers for everyone
- Best flowers to give a girl
- What flowers represent each month
- occassin to give flowers
- Designe your own bouquet online
- Create your own bouquet virtual
- Event Florists London
- Beautifule flowers for home
- Fresh products delivery to your door
- Good Luck flowers for wedding
- Best florist in London 


Of the above searches "Flwer shop near me" best suited what my project is selling and had the highest search rate of all keywords attempted. With that in mind, I have selected the following to be included in my projects metadata: 

- Flower shop near me
- Send flowers
- Unique bouquets
- Home delivery flowers London
- Special occassion
- Spring wedding flowers UK
- Long-lasting summer flowers
- Flowers for everyone
- Best flowers to give a girl
- Designe your own bouquet online
- Event Florists London
- Beautifule flowers for home
- Fresh products delivery to your door


Also, I included "Send Flowers" within the homepage message’ along with a subheading of "Home delivery flowers London".

# Marketing Strategies

1. Would your users use social media? If yes, which platforms do you think you would find them on? 
    - Instagram. 

       - Users can get inspiration from the instagram platform, showing photos with the title "How to decorate the interior with flowers?". And also included useful information about flowers and how to care for them. 

       - Video clips are posted for various occasions, such as a wedding or birthday party where flowers are prominently featured. 

    - Facebook. 
    
      -  Users can get inspiration from the instagram platform, showing photos under the title "How to decorate the interior with flowers?". And also included useful information about flowers and how to care for them. 

      - Video clips are posted for various occasions, such as a wedding or birthday party where flowers are prominently featured. 

    - Event Decor. 
      - The Event Decor function is a blog where large amounts of photos and information about flowers are also posted. 
      - Contests would be held where the winner could win a gift card. 

    - Email. Promotions and inspirations are sent to the user's e-mail. Large pictures are posted and discounted prices are posted in larger fonts to catch the recipient's attention. 

2. Would your business run sales or offer discounts? How do you think your users would most like to hear about these offers? 
    - Promotions are updated every week. 
    - Gift cards
    - Gift baskets
    - Free shipping on purchases over $50

3. What do your users need? Could you meet that need with useful content? If yes, how could you best deliver that content to them?

Users need flowers for home. With the help of the text and its content, I could present:
 
- How flowers have a positive effect on our mood
- How beautiful they can decorate the house
- What different flowers mean
- what flowers are best to buy for girls
- suggestions for bouquets of flowers for weddings and other parties
- Information and good advice on how to handle flowers correctly way.
- Information that if a customer wants to know more about their flowers, they can contact us
- Information about how to keep cut flowers alive longer
-  Information about how to effectively dry flowers.
 
4. What are the goals of your business? Which marketing strategies would offer the best ways to meet those goals?

My company's goal is that customers buy often and a lot of products. I want to post something that catches the eye. I tried to make the interior of my website well-chosen, the colors were chosen to match the color of the flowers, the photos were carefully chosen to arouse people's curiosity.

- In order for people to visit my flower shop often, I would like to have a friendly atmosphere, which I could achieve by posting short posts that are interesting, sometimes funny, for my blogs, facebook and instagram.

- With every post, I would have to include a photo.
- My site would be updated very often under various titles such as "Valentine's Day", "Flowers for Mother's Day", "Flowers for Easter" with suggestions on which flowers to buy for a given occasion.
- Marketing types like facebook, instagram, email, blog would definitely help me in my goal.


## Facebook business page

This is evidence of either a real Facebook business page for the purposes of digital marketing:
![fb](media/fb.png)
![Facebook part1](media/facebook_page1.png)
![Facebook part2](media/facebook_page2.png)
![Facebook part3](media/facebook_page3.png)
![Facebook part4](media/facebook_page4.png)



# Planning
## Technologies Used
### Languages Used
- [HTML](https://sv.wikipedia.org/wiki/HTML)
- [CSS](https://en.wikipedia.org/wiki/CSS)
- [PYTHON](https://en.wikipedia.org/wiki/Python_(programming_language))
- [JQUERY](https://en.wikipedia.org/wiki/JQuery)
- [JAVA SCRIPT](https://en.wikipedia.org/wiki/JavaScript)

### Frameworks, Libraries and Programs Used:

- [Balsamiq](https://balsamiq.com/) was used to create wireframes.
- [Font Awesome](https://fontawesome.com/) was used to create icons to footer and home page, logo.
- [Google Fonts](https://fonts.google.com/?preview.text=Love%20Running&preview.text_type=custom) was used to import 'Caveat', 'Courier New' that have been used for each page.
- [Git](https://git-scm.com/) was used  by utilising the Gitpod terminal to commit to Git and Push to GitHub.
- [GitHub](https://github.com/) was used as a repository for code of the project. 
- [Django](https://www.djangoproject.com/) was used as the framework to support rapid and secure development of the application.
- [Bootstrap](https://getbootstrap.com/) was used to build responsive webbpages.
- [Heroku](https://id.heroku.com/) was used to deploy the project.
- [Lucid Chart](https://lucid.app/lucidchart) was used to create a diagram to models database.
- [Pep8](https://pep8ci.herokuapp.com/#) was used to validate Python code.
- [AWS](https://aws.amazon.com//) was used to store the images used by the application
- [JSHint](https://jshint.com/) was used to validate JavaScript code.
- [PostgreSQL](https://www.elephantsql.com/) was used for database.
- [SQLite](https://www.sqlite.org/) was used for databse.
- [Django Allauth](https://django-allauth.readthedocs.io/en/latest/index.html) was used for registration.
- [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) was used to get a form crispy.
- [STRIPE](https://stripe.com/) was used to enable the customer to pay with a payment card.


## Credits 
### Codes

- Part of my project is based on Code Institue Building an E-Commerce Platform.

- Florist Blog is based on the "I think, therefore I blog" guide in the Code Institute Full Stack Frameworks module.


### Information about flowers:
- [Freepik](https://www.pexels.com/sv-se/)
- [Pexels](https://www.freepik.com/search?format=search&query=children)
- [Bouquet- description](https://urocznica.pl/letni-bukiet-kwiatow-inspiracje-i-cytaty/)
- [Wedding flowers- description](https://www.partyflowers.pl/2018/06/bukiet-slubny-do-czego-musi-pasowac-2/)
- [blog- roses](https://www.e-kwiaty.pl/blog/jak-dbac-o-kwiaty-ciete.html)
- [footer- content about delivery](https://www.bukiety.com/about)
- [image- bag is empty](https://img.freepik.com/free-vector/no-data-concept-illustration_114360-2506.jpg?w=1060&t=st=1687441450~exp=1687442050~hmac=ce019363ef95c3a93f0b9fbbff7b237774f69215e5591d6fa86fc8bdd77c49f3)
- [Red roses meaning- posted on Facebook Page](https://fiftyflowers.com/blogs/flowers/rose-color-meanings)
- [Home Decor with flowers- posted on Facebook Page](https://www.ftd.com/blog/five-ways-interior-designers-use-flowers)
- [description product rose](https://www.euroflorist.pl/bukiet-rozana-dama)
- [sunflowers description](https://www.bloomandwild.com/meaning-and-symbolism-of-sunflowers)
- [inpiration flower description](https://laflora.pl/)
- [Take care roses](https://www.floom.com/pages/how-to-care-for-cut-roses)
- [How flowers have a positive effect on our mood](https://unlimitedgreens.com/blogs/blog/how-do-flowers-have-a-positive-impact-on-our-mood)
- [Decorate with flowers- blog post](https://www.thespruce.com/how-to-decorate-with-flowers-5207816)

### Images:
All pictures on this site are taken from [Freepik](https://www.freepik.com/)

# Acknowledgements:

- Thank you to my mentor Elaine Broche for useful feedback and guidance in my project. I received a lot of help and a very detailed explanation.

- Thank you to tutor assistance Oisin and Ed for explanation of the issues related to checkout confirmation email and  Rebecca for great help with the issue that was in file signals.py related to the final price displayed in the confirmation e-mail.

 

