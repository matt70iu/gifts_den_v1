# Gifts Den

Gits den aims to be the one stop shop for all the gifts you need, for those special people in your life!

The wide scope name of the store was very much deliberate, in the sense that it gives potentially limitless rooms for expansion in the future, both in terms of prodct range and store size.

When building the store, I started off with some clothing, electrical and living style products, with the intension of expanding this in the future.

Please see the wireframes shots below to give you an idea of the general site layout and structure.

## Site Design (Wireframes) 

![wireframes-homepage](media/screenshots/wireframes/homepage-wireframes.png)

- Homepage

![filtered-products-page](media/screenshots/wireframes/filtered-products-page-wireframes.png)

- Products page

![products-detail-page](media/screenshots/wireframes/products-detail-page-wireframe.png)

- Products Detail Page

![shopping-bag-page-1](media/screenshots/wireframes/shopping-bag-page-wireframes-1.png)

![shopping-bag-page-2](media/screenshots/wireframes/shopping-bag-page-wareframes-2.png)

- Shopping bag page

![checkout-page-1](media/screenshots/wireframes/checkout-page-wireframes-1.png)

![check-out-page-2](media/screenshots/wireframes/checkout-page-warefrmaes-2.png)

- Checkout Page

![order-success-page-1](media/screenshots/wireframes/order-success-page-wireframes-1.png)

![order-success-page-2](media/screenshots/wireframes/order-success-page-wireframes-2.png)

- Order success page

![product-management-page-1](media/screenshots/wireframes/product-management-page-wireframes-1.png)

![product-management-page-2](media/screenshots/wireframes/product-management-page-wirefrmaes-2.png)

- Product management page

![profile-page](media/screenshots/wireframes/profile-page-wireframes.png)

- Profile Page

![password-reset-screen](media/screenshots/wireframes/password-reset-screen-wireframes.png)

- Password reset screen

![sign-in-form](media/screenshots/wireframes/sign-in-form-wireframes.png)

- Sign in form

![sign-out-screen](media/screenshots/wireframes/log-out-screen-wireframes.png)

- Sign Out form

## User stories/planning

I used Github's storyboard feature to assist me with the planning of this project, although, as with previous projects, I did need to add some stories while building the project to cater for additional features such as reviews, that I decieded to add after commencing work.

![gift-den-user-stories](media/screenshots/gift-den-user-stories.png)

## Models

The project includes all Crud functionality as per requirements.

The main models within the project are:

Products consisting of:
- Category
- Product
- Review 
- Userprofile

- The Review model is an addition to the Code Institute Boutique Ado walkthrough project, which I used to help me build this project.

- I will also be ammending or possibly removing the rating field from the product model, as a user is unable to rate a project in it's current form and believe that the review model is more useful in this regard.

- I also added a date of birth field to the Userprofile model as I believe this will be useful in terms of any age restricted products that may be sold on the store in the future.

## Gifts Den Marketing Strategy

### PPC Advertising

On launch, our new Ecommerce store is not likely to get a lot of organic search engine trafic due to the fact that it is a new site, and could take several weeks or even months to gain any sort of position in relevent meaningful search terns.

To that end, I would like to target some longer tail, less competative keywords using PPC advertising.

### Long Tail Keywords

These long tail keywords would be product focused and I would like to bring the user directly to the page that their search is targeting.

Take a product we currently sell such as headphones.

If we were to target a keyword such as "buy headphones", this currently has search results in google ranging into the hundreds of millions, however, if we were to target a keyword such as "buy headphones with better battery life", this has search results in the 10 of millions, which would be much easier and cheaper to target using PPC.

### Organic SEO optimisation

I will be putting descriptive metatags and keywords into my base template in order to improve our organic search engine rankings, as per project requirements.

Once I have all final sample products in place, I will also be creating sitemap, and robots.txt from it for the search engines and submitting as needed.

### Newsletter

We already have a newsletter sign up form set up on our store's homepage. As we drive traffic to our site, initially through our budgeted PPC campagn and later, through our growing organic search results, we can send out a monthly or as the store gorws, even a weekty newsletter to let our subscribers know about any special offers and seals, and drive even more traffic to the site.

## Features

### Homepage

On the home page the user can:

![Home-page](media/screenshots/home-page.png)

- Search the site
- Login/out or register
- Select some products to view from the the top navbar or from the shop now button

Assuming our user is a new customer

![select-register](media/screenshots/click-register.png)

- We will click on register.

![registration-screen](media/screenshots/sign-up-corrected.png)

- We are then brought to the resigistration screen to fill out our details.

![registration-2](media/screenshots/registration-screen-2png.png)

- Once the user has filled out their details, they will click on the sign up button.

![registration-success](media/screenshots/register-success.png)

- They will then be brought back to the homepage and presented with a success message confirming successful registration.

- They will then need to confirm their email address via the email sent to the email address they registered.

### Purchasing a product

![login-in-page](media/screenshots/login-page-crednetials-entered.png)

- Our newly created user, having confirmed their email address, will now be able to log into the store to make a purchase.

![log-in-success-message](media/screenshots/login-success-new-registration.png)

![select-headphones](media/screenshots/select-electrical.png)

- Assuming our new user wanted to purchase some headphones, they would select electrical from the top nav bar and then select headphones.

![headphones-filtered](media/screenshots/headphones-filtered.png)

- The user is then presented with a filtered list of all headphones available.

![headphones-product-detail](media/screenshots/headphones-product-detail.png)

- Our user wishes to purchase the first set of headphones, selects them and is then presented with the product detail page.

![headphones-added-to-bag](media/screenshots/headphones-add-to-bag-success.png)

- Once the user has selected the correct quantity and clicked add to bag, they will be greeted with a confirmation message confirming the headphones have been added to their shopping bag successfully.

![headphones-checkout-prepopulated](media/screenshots/headphones-checkout-prepopulated.png)

- Asuming this is the only item they wish to purchase, they will then click on go to checkout and be presented with the checkout screen, with the majaority of their registeration information already filled out on the page.

![tick-profile-box](media/screenshots/profile-tick-box.png)

- They will also have the option to select a tick box in case they wish to change any of their user profile information.

- They will then add their payment information and click on complete order.

![order-success-page](media/screenshots/order-success-headphones.png)

![confirmation-email](media/screenshots/confirmation-email-gmailpng.png)

- They will then be presented with an order success page and sent a confirmation email to confirm their order was processed successfully.

- The order process will differ slightly depending on weather the user is registered.

![register-or-login](media/screenshots/create-account-or-login.png)

- If the user is not registered, they will need to fill out all their information in the checkout page, and if they they wish to register, they can simply select, create account, or login and will be brought to the registeration or login page and can then continue with their purchase. 















