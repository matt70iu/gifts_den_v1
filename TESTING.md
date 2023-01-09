# Gifts Den Testing

## Login/Logout

The expected result of this test is that, when the user attempts to log into the application using their username and password, they will be logged in and presented with an on screen message confirming a successful login, with their my account dropdown menu, displaying the option to view their profile, logout and in the case of a superuser, go to the product management page.

When testing this featue I did the following:

![my-account-menu](media/screenshots/my-account-menu.png)

- Click on my account at the top right of the screen and select login.

![sign-in-screen](media/screenshots/sign-in-screen.png)

- When presented with the sign in screen, the Sign up/login screen text between the horizontal rule was missing.

- This was because of a previous change to the logo class to white to make the offer banner text visable.

- To rectify this, I added an id to override the class and changed the colour to suit.

![sign-in-screen-correction](media/screenshots/sign-in-screen-correction.png)

- The sign in screen now displays as expected.

- I entered my credentials and was able to log in successfully.

![sign-in-success](media/screenshots/sign-in-success.png)

- I next attempted to log out by selecting the my account menu again and selecting logout.

![sign-out-screen](media/screenshots/sign-out-screen.png)

- I encountered the same issue with the h2 text between the horizontal rule as on the sign in page.

- Again I corrected this by adding an id to the h2 to pair it with the previous css for the sign in page.

![sign-out-screen-corrected](media/screenshots/sign-out-screen-corrected.png)

- I was then able to sign out successfully.

![sign-out-success](media/screenshots/sign-out-success.png)

## Register New Account

The expected result of this test is that the user will be able to register a new account and that within this process, they be sent an email verification in order to confirm their email address. Once the user confirms their email, they should be able to log in with their newly created credentials.

When testing this feature, I did the following:

![my-account-menu](media/screenshots/my-account-menu.png)

- Click on the my account menu at the top right of the screen and select register.

![registration-page-1](media/screenshots/registration-screen-1.png)
![registration-page-2](media/screenshots/registration-screen-2png.png)

- Again, I encountered the same issue as with the previous log in/out pages, so I added the same id to this template to correct also.

![sign-up-corrected](media/screenshots/sign-up-corrected.png)

- I was then greeted with the confirm email screen, to which I again added the applicable id to correct the missing h2 text.

![confirm-email](media/screenshots/confirm-email-page.png)

- The verification email was then sent to a temp email address as expected.

![verification-email](media/screenshots/verification-email.png)

- Upon using the link, provided in this page, I was then greeted with a the next confirmation page with a button, asking me to click to confirm my email address. Again, I corrected the issue with the h2 by adding the correct id to the template.

![confirm-email-2](media/screenshots/confirm-email-page-2.png)

- The I was then brought back to the login screen with an email confirmation success message.

![registration-success](media/screenshots/register-success.png)

- I was then able to log in using this email address without issue.

![registration-success-new-user](media/screenshots/login-success-new-registration.png)









