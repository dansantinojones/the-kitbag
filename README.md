# The Kitbag

## Introduction
This online store was created and developed as my final portfolio project for my Full Stack Software Development course with Code Institute. The Kitbag is an e-commerce website selling retro football shirts. Users can register an account, browse shirts on sale, purchase shirts with card payment, view order history and sell shirts.

View the live project here: [The Kitbag](https://the-kitbag.herokuapp.com/)

This is for educational purposes only, please don’t enter your card details.
If you want to test the payment system, use these test card details: <br>
Card Number: 4242 4242 4242 4242 <br>
Date: 0424 <br>
CVC: 242 <br>
Postcode: 42424

## Strategy Plane
### Business Goals
- Sales
- Repeat purchase
- Sign Ups 
### Target Audience
- 18 to 44 year olds
- Football fans
- Collectors
- High disposable income
### Competitor Review
1. [Classic Football Shirts](https://www.classicfootballshirts.co.uk/)

<details>
  <summary>Click here to view competitor analysis on Classic Football Shirts</summary>

  ![](media/cfs-overview.png)
  ![](media/cfs-location.png)
  ![](media/csf-demographic.png)
  ![](media/csf-keywords.png)
 
  </details>

2. [Retro Football Kits](https://www.retrofootballkits.co.uk/)

<details>
  <summary>Click here to view competitor analysis on Retro Football Kts</summary>

  ![](media/rfk-overview.png)
  ![](media/rfk-location.png)
  ![](media/rfk-demographic.png)
  ![](media/rfk-keywords.png)
 
  </details>

3. [Vintage Football Shirts](https://www.vintagefootballshirts.com/)

<details>
  <summary>Click here to view competitor analysis on Vintage Football Shirts </summary>

  ![](media/vfs-overview.png)
  ![](media/vfs-location.png)
  ![](media/vfs-demographic.png)
  ![](media/vfs-keywords.png)
 
  </details>


## Scope Plane
### User Stories
As a shopper:
- As a site user I can register for an account so that I can have a personal account and view my profile.
- As a site user I can login and logout of my account so that access my personal account information.
- As a site user I can have a personalised profile page so that I can view purchase history.
- As a site user I can recover my password incase I forget it so that regain access to my account
- As a site user I can receive an email confirming my account registration so that I know my account was successfully registered.
- As a shopper I can view a list of products so that select one or more to purchase.
- As a shopper I can view individual product details so that I can identify price, size, description and product image.
- As a shopper I can easily view the total of my spending so that avoid spending too much.
- As a shopper I can search products by name and description so that find a specific item to purchase.
- As a shopper I can sort the list of available products so that I can arrange the list by price.
- As a shopper I can view products from specific leagues so that choose from my favourite leagues and narrow my search.
- As a shopper I can select the size and quantity of a product so that I can choose from available sizes and purchase more than one.
- As a shopper I can view items in basket so that identify the total cost view products I've selected to purchase.
- As a shopper I can adjust the quantity of items in my basket so that I can make changes before checkout.
- As a shopper I can easily enter payment information so that I checkout quickly with no hassle.
- As a shopper I can view my order details after checkout so that I can ensure no mistakes were made.
- As a shopper I can receive an email confirmation after checkout so that keep a record of my purchases.
- As a shopper I can sign up to a mailing list so that I can be first notified of new shirts on release.
- As a shopper I can view company reviews so that I can gain trust before making a purchase.
- As a shopper I can leave the company a review so that I can express my satisfaction/dissatisfaction.
- As a shopper I can sell my shirts so that I receive money for old shirts I no longer want.
- As a shopper I can remove items from my basket so that do not have to close the browser to clear the basket.

As an admin:
- As a store owner I can add products so that add new items for sale.
- As a store owner I can edit and update products so that I can change product pricing, images and descriptions.
- As a site owner I can delete products so that I can remove items that are no longer for sale.
- As a site owner I can view orders made by customers so that I can manage the orders.
- As a site owner I can create a mailing list with registered user emails so that I can send out weekly newsletters.
- As a site owner I can manage customer reviews so that I can resolve any issues from dissatisfied customers.
- As a site owner I can see all the relevant details from shirts customers want to sell so that I can make an informed decision on making them an offer.

### Agile Methodology
The Kitbag was created using the agile approach, from the initial planning and wireframing to building the front and back-end functionalities. I used GitHub project to build a Kanban board to visualise the user stories from ‘To Do’ to ‘In Progress’ to ‘Done’. User Stories that could not be completed were put into ‘Out of Scope’. ’Important’ red tags were used on the User Stories that needed addressing first. ‘Urgent’ yellow tags were used on User Stories that must be included. ‘CRUD’ aqua tags were used to highlight the Admin Stories. 

### Milestones
- Home
- Registration
- Products
- Basket
- Checkout
- Payment 
- Profile 
- Admin
- Reviews

## Structure Plane 
The structure of the pages was carefully planned out when designing the website. I wanted to keep it similar to most e-commerce website structures ensuring that the website is familiar to the user and the content is positioned exactly where the user expects it to be.
### Consistent
### Predictable
- Clickable logo to take user back to home page
- Images open in a new window
### Content Organisation
The shirts on sale were displayed on the site using bootstrap cards which stack nicely above each other in mobile view making it easy to browse through the products.
### Information Architecture 
When planning the shirt detail page I put myself in the shoes of the user to understand what information would be most important to the user and how it will be viewed. The most important information in the buyer decision-making process is, image, name, price and size.

## Skeleton Plane 
### Wireframes
Prior to writing any code, initial wireframes were drawn with pencil and paper. Once happy with the layout and design, I used [Figma](https://www.figma.com/) to create my wireframes. It was important to plan and visualise my website across desktop and mobile to ensure I had a clear vision and the execution of writing code was successful.

<details>
  <summary>Click here to view Desktop Wireframes:</summary>

  ![](media/wf-desktop-home.png)
  ![](media/wf-desktop-shirts.png)
  ![](media/wf-desktop-shirt-detail.png)
  ![](media/wf-desktop-basket.png)
  ![](media/wf-desktop-checkout.png)
 
  </details>

<details>
  <summary>Click here to view Mobile Wireframes:</summary>

  ![](media/wf-mobile-home.png)
  ![](media/wf-mobile-shirts.png)
  ![](media/wf-mobile-shirt-detail.png)
  ![](media/wf-mobile-basket.png)
  ![](media/wf-mobile-checkout.png)
 
  </details>
<br>

### Navigation Diagram
I designed a flowchart using [Lucidchart](https://lucid.app/documents#/documents?folder_id=recent) to help visualise the user experience throughout the website. The milestones are bold to highlight their importance. 
![](media/navigation-diagram.png)

### Database Diagram
I used [DrawSQL]() to create and visualise the database diagrams for the project. 

<details>
  <summary>Click here to view product models:</summary>

  ![](/media/db-league.png)
  ![](/media/db-shirt.jpg)
  ![](/media/db-sellshirt.jpg)
 
  </details>

<details>
  <summary>Click here to view order models:</summary>

  ![](/media/db-order.png)
  ![](/media/db-orderlineitem.png)
 
  </details>


<details>
  <summary>Click here to view profile model:</summary>

  ![](/media/db-userprofile.png)
 
  </details>


<details>
  <summary>Click here to view review model:</summary>

  ![](/media/db-reviews.png)
 
  </details>


<details>
  <summary>Click here to view newsletter model:</summary>

  ![](/media/db-newsletter.png)
 
  </details>
<br>

### Sitemap

## Surface Plane 
### Colours 
### Typography 
### Icons
### Features
- Logo<br>
The logo was created using [Adobe Photoshop](https://www.adobe.com/uk/products/photoshop.html). Design inspiration was taken from popular football club badges. The logo has an imprtant role in the navigation of the website. Users can always return to the home page by clicking on the logo in the header.
- Search Bar
- Dropdowns 
- Leagues Menu<br>
All shirts on the website are categorised by the teams' leagues. The main nav menu consists of 7 leagues/categories, making it easy for users to browse their favourite leagues. 
- Mobile Header
- Alert Messages<br>
Alert messages are very important in communicating back to the user once an action is taken. This provides reassurance to the user that their action was completed successfully/uncusessfully. The alert messages are colour coded with green for success, red for error, yellow for alert and blue for info messages. These messages auto-dismiss after a few seconds. 
- Sign Up
- Shirt Cards 
- Filtering
- Back to Top Button<br>
The back to top button plays an important role in the navigation of the website. This allows users to return to the top of the page with a click of a button. This is an example good user experience as users don't have to scroll up once at the bottom of the product list. The button is placed on the right of the screen and uses the [Font Awesome](https://fontawesome.com/) arrow up icon.
- Product Count<br>
The product count notifies users how many products are available in their search or in the specific league category. A home icon is placed next to the product count for users to return to the home page. 
- Shirt Detail 
- Basket
- Checkout 
- Confirmation
- Leave a Review 
- Recent Reviews
- Update Details 
- Order History
The profile page displays the user's order history. This is important for the users to keep track of their previous orders all in one place. The cost, date, time and order number is shown under order history. The order number is a link which will take the user to their order confirmation. 

### Future Features
- Stock Tracker
- Filtering by size
- Randomizer

## Business Model

## Marketing Strategy

## SEO
### Keywords 
### Robots.txt
### Sitemap
### Privacy Policy
The [Privacy Policy Generator](https://www.privacypolicygenerator.info/) was used to create a Privacy Policy for The Kitbag. It is important to include this on the website as it tells users how and why we are collecting their personal information. From a SEO and Marketing stance, search engine algorithms will find the site trustworthy and prioritise it over websites without one.

## Technologies Used
- [HTML5](https://www.w3schools.com/html/) was used to create the structure of the website.
- [CSS3](https://www.w3schools.com/css/) was used to style the website.
- [JavaScript](https://www.javascript.com/) was used to add interactivity to the website.
- [Python](https://www.python.org/) was used to build the backend of the website.
- [Django](https://www.djangoproject.com/) was used to build the website.
- [Django Allauth](https://django-allauth.readthedocs.io/en/latest/) was used for all account management.
- [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) was used to render the website forms.
- [PostgresSQL](https://www.postgresql.org/) was used as the database during development.
- [Gunicorn](https://gunicorn.org/) was used to run the application.
- [Bootstrap](https://getbootstrap.com/docs/4.3/getting-started/introduction/) was used to style the website content.
- [Git](https://git-scm.com/) was used for version control to commit and push to GitHub.
- [GitPod](https://www.gitpod.io/) was used to 
- [GitHub](https://github.com/) was used to store the code.
- [Chrome DevTools](https://developer.chrome.com/docs/devtools/) was used to fix errors and test responsiveness.
- [Heroku](https://heroku.com/) was used to deploy the website.
- [Elephant SQL](https://www.elephantsql.com/) was used to host the database.
- [Font Awesome](https://fontawesome.com/) was used for the website icons.
- [Google Fonts](https://fonts.google.com/) was used for the website font.
- [Adobe Photoshop](https://www.adobe.com/uk/products/photoshop.html) was used to design and create the logo.
- [Figma](https://www.figma.com/) was used to design the wireframes.
- [Lucid Charts](https://lucid.app/) was used to design the navigation diagram.
- [DrawSQL](https://drawsql.app/) was used to create database diagrams.
- [Similarweb](https://www.similarweb.com/) was used for competitor analysis.
- [Stripe](https://stripe.com/gb) was used to process the card payment functionality. 
- [Amazon AWS](https://aws.amazon.com/) was used to store the static and media files.
- [Pexels](https://www.pexels.com/) was used for the image on the 'About Us' page.
- [Pixaby](https://pixabay.com/) was used for the background image.
- [Grammarly](https://www.grammarly.com/) was used to check the grammar of the website content.
- [Privacy Policy Generator](https://www.privacypolicygenerator.info/) was used to create the privacy policy.

## Testing 
### Secret Key
The Django Secret Key was accidentally exposed through GitHub. Since noticing the mistake, I have created a new secret key inside a .env file and hidden it through a gitignore file. The Secret Key exposed in the files does not work as it has since been changed.
### User Stories 
### Feature Testing 
| Feature      | Description | Result     |
| :---        |    :----:   |          ---: |
| Logo      | Click returns to home page       | ✅   |
| Search Bar   | Shows results from search term       |    ✅    |
| Alert Messages    | Display messages about users action        |        |
| Product Count   | View number of products        |   ✅    |
| Filtering    | Filter items        |   ✅    |
| Back to Top Button    | Click to go back to top        |    ✅   |
| Add to Basket   | Add itmes to basket        |       |
| Remove from Basket   | Remove itmes from basket        |       |
| Checkout   |     Use card details to checkout order    |       |
| Order Confirmation   | Display details after order        |       |
| Order Confirmation Email   | Receive an email confirmation        |       |
| Newsletter Sign Up   | Sign up using an email address        |       |
| Sell a Shirt   | Fill out a form to sell a shirt        |       |
|  Register   | User's can register for an account        |       |
| Login   | User's can login to their account        |       |
| Logout   | User's can logout of their account        |       |
| Forgot Password   | Reset password        |       |
| Add Shirt   | Add a shirt to the store        |       |
| Edit Shirt   | Edit a shirt from the store        |       |
| Delete Shirt   | Delete a shirt from the store        |       |
| Leave a Review   | Post a review        |      |
| Recent Reviews   | Display recent reviews        |      |
| Update Information   | User's can update their information        |      |
| Order History   | Display's users order history        |       |
### Terminal Errors 
### HTML Validator 
### CCS Validator 
### Python Linter
### Responsiveness
### Lighthouse
### Unfixed Bugs

## Deployment
### Code Institute Template
1. Click the 'Use This Template' button.
2. Name your repository and write a description (optional).
3. Click the 'Create Repository from Template' to create the repository.
4. Click the 'GitPod' button to create a new workspace.
5. When working on the project, ensure to open the workspace from GitPod, this will open your previous workspace ratehr than creating a new one.
6. Use the following commands to commit your work:
- 'git add' adds all the modified files to a staging area.
- 'git commit -m "Write commit message"' commits the changes to the local repository.
- 'git push' pushes all your committed changes to the GitHub repository.

### Django Setup
### ElephantSQL Setup
1. Open ElephantSQL.
2. Register or Login.
3. Click 'Create New Instance'. Create a name and select a region.
4. Confirm new instance by clicking 'Create Instance'.
5. Click the instance you created.
6. Copy the URL to the clipboard.
7. Paste it into your DATABASE_URL = "enter url here" in .env file.
### Heroku Setup
1. Open Heroku.
2. Register or Login.
3. Click 'Create New App'.
4. Enter app name and select the region.
5. Click 'Create App'.
6. Under the 'Deploy' tab, click 'Connect to GitHub'.
7. Enter your GitHub credentials.
8. Search for your repository and click 'Connect'.
9. In the 'Settings' tab, scroll to 'Reveal Config Vars' and copy the ElephantSQL URL from the .env file.
10. In config vars, set PORT to 8000 and add the SECRET_KEY from the .env file.
### Stripe Setup 
### Amazon Web Services
### Google Email

## Development
### Fork
1. Log into GitHub and click on repository to download
2. Click the 'Fork' button in the top right-hand corner
3. Select a different owner if necessary
4. Click on 'Create Fork'
5. The repository is now in your account and can be changed (Changes made to a forked repository will not affect the original).
### Clone 
1. Navigate to the main repository page.
2. Click on the 'Code' dropdown menu above the list of files.
3. Choose a method to copy the URL for the repository.
4. In the work environment, open Git Bash and change the current directory to target location for cloned repository.
5. Type 'git clone' followed by the copied URL and press 'Enter'.
### Download ZIP
1. Log into GitHub and click on the repository to download.
2. Select 'Code' and click 'Download Zip'.
3. Once the download is finished, extract ZIP file and use it in the local environment.

## Credits<br>
1. [Retro Football Shirt Store](https://www.retrofootballshirtstore.com/) for the product images. 
2. [Boutiqe Ado](https://codeinstitute.net/) walkthrough project with Code Institute for site inspiration.

## Acknowledgements
I would like to thank my mentor Chris Quinn for his advice and guidance throughout the project.






