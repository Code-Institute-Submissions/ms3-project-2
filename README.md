# Report On Any Discrimination

![Image a website on different devices](static/files/responsive-design.jpg)

### [Live page](https://ms3-cgpalmer91.herokuapp.com/)

# Disclaimer

The statistics on this website are free to use. However, they must be reported responsibly and with context. 

Any misrepresentation of the statistics will be denounced and asked to remove them. 

Please do not use a person's name in the reports, as the report will be removed.



___

## Contents
+ <a href="#rationale">Rationale</a>
    - <a href="#inspiration">Inspiration</a>
+ <a href="#UX">UX</a> 
   - <a href="#userStories">User Stories</a>
+ <a href="#features">Features</a>
   - <a href="#existingFeatures">Existing Features</a>
   - <a href="#featuresLeftToImplement">Features left To Implement</a>
+ <a href="#defensiveFeatures">Defensive Features</a>
+ <a href="#technologiesUsed">Technologies Used</a>
+ <a href="#testing">Testing</a>
+ <a href="#responsiveDesign">Responsive design</a>
+ <a href="#deployment">Deployment</a>
   - <a href="#deploymentLive">Deployment Live</a>
   - <a href="#deploymentLive">Deployment Local</a>
+ <a href="#credit">Credit</a>
   - <a href="#tutorials">Tutorials</a>
   - <a href="#media">Media</a>
   - <a href="#acknowledgements">Acknowledgements</a>
+ <a href="#project">Project Evaluation</a>
   - <a href="#improvements">Improvements</a>






___

<span id="rationale"></span>
## Rationale

## Project proposal

The project aim to create a database of discrimination across the UK. It will allow users to take a stand and 
report any discrimination they experience, hear or see. They can categorise the discrimination and add a location.

Why collect data? Councils have made it clear that they are underfunded and that doesn't appear to be changing any
time soon. Yet, there is a rise in racist and xenophobic attacks across the country. 

This project will be open-sourced and all councils, police, charities and authories will have access to the data.
They can search by area or by discrimination to see where they can focus their efforts and funding.

___

<span id="inspiration"></span>

## Inspiration

#### Requesting information

I designed this website to be as intuative and quick as possible. A major factor for not recording events is simply 
the amount of time it can take out of the day. Therefore, I designed my web site to only request the information
it necessary. 

I read an article explaining how to create a minimalist registering page at this link:
https://www.smashingmagazine.com/2011/05/innovative-techniques-to-simplify-signups-and-logins/

Using it as inspiration, I simplified my registering form and allowed user to sign up as quickly as possible.
I also allowed them to add a preferred name once they were signed up, again speeding up the process.

I took this a step further with adding a new report or searching for a report. 

When adding a report, you are required to give information on whether the incident has been reported, 
the category of the incident and a description. As soon as that information was supplied, the incident was recorded.
After that, the user had the option to add extra details such as date and location. This offers flexibility to the
user and encourages use even if all the details aren't accessible.

When searching for a report, you only need to select the information necessary for your search. Otherwise, the Javascript
hides the extra information.

#### Design

I wanted this website to have a calm and mature theme - one that matches and reflects the sombre but important purpose.
In order to do this, I looked at two particular design websites that are linked below:
https://visme.co/blog/color-combinations/?fbclid=IwAR04pjyYtd1uGzsv9jQWIOkG3KCayjX2nGdH6xTy9WPapcLV0Xie3HKmWg0
https://visme.co/blog/website-color-schemes/?fbclid=IwAR16fr1TqIOxw-Juvp4z_FFiHoHpONwH6D6g7Eud2-aVdneS0q2DHFfTWPg

I finally decided on one that had earth tones, which promoted calm and clarity. I attempted where possible to stick 
to as few colour as possible and ensured they complimented each other. 

___

<span id="UX"></span>
## UX

<span id="userStories"></span> 
### User Stories

#### As a public user
1. 


#### As a charity or researcher

### Wireframes

Wireframes have been made using Balsamiq. 

[Wireframes](static/wireframes/wireFrames.pdf)

[Responsive images of actual site](static/wireframes/responsiveImages.pdf)
___
<span id="features"></span>
## Features

<span id="existingFeatures"></span>
### Existing Features

<ins>Navbar</ins>

1. 

<ins>Home </ins>

1. 

<ins>Dashboard </ins>

1. 

<ins>Login </ins>
<ins>Signup</ins>
<ins>Add report</ins>
<ins>Search report</ins>
<ins>Settings</ins>


<span id="featuresLeftToImplement"></span>
### Features Left to Implement

- The date will present itself the correct way round.
- Automatic email will be sent to the website managers when a report is updated/added
- Public can recommend categorise when adding a report rather than having to email separately.
- A google api will allow the locations of the features to be displayed as clusters across a map. 
- People can filter incidents just by a date frame. 
- Export data as a CSV to be used on excel.
- Councils/ other professional bodies will be able to upload reports of discrimination via their own CSV.


___
<span id="defensiveFeatures"></span>
## Defensive Features

+ I wanted to make sure that the users inputted all the information necessary for a successful search. 
  So I have used JS to disable the buttons until a criteria has been met. 
+ If you try to access any of the web pages that are reserved for account holders, it will redirect you to the login
  page. I did this to help protect people's reports so that only they could modify them. 
+ A new user cannot use the same email as a current user. This is because the functionality of the website uses the
  email address to identify which user to assign the report to. 
+ I ask the user to confirm their password before they can delete their account.
+ The passwords are hashed and a different salt is generated each time a password is made/changed. If anyone hacks into
  database they will not be able to see the passwords.

___
<span id="technologiesUsed"></span>
### Technologies Used

Languages used

1. HTML
2. CSS
3. Javascript
4. Python 

Frameworks

1. Materialize 1.0.0
2. Flask 
3. Jinja 
4. jQuery

___
<span id="testing"></span>

## Testing

I have posted a link for more detailed testing. 

Please find the link to the test document here: [Link to the testing page](assets/files/README-Testing.md)   

## Interesting bugs


1. [Dividing by 0](static/files/bug-for-dividing-by-0.pdf) 
2. [Logging in issues](static/files/Issue-with-logging-in.pdf) 
3. [Console error breaking the JS flow](static/files/js-console-error-interrupting-the-other-js.pdf) 
4. [Problems reading if the email address exists, live](static/files/Live-reading-if-the-username-exists.pdf) 
5. [Only certain elements are being searched in the array](static/files/Not-match-against-all-array-elements.pdf) 
6. [Problems with validating the password](static/files/password-validation-issue.pdf) 





___
<span id="responsiveDesign"></span>
## Responsive Design

This project has been optimised to the common devices on Google Chrome's Dev Tools.
It has been specifically designed for the following:
   + Moto G4
   + iPhone 6/7/8
   + iPad
   + iPad Pro
   + Laptop with MDPI screen
   + Laptop with HiDPI screen


The majority of the website stays consistent to an easy user experience. There are minor changes to font-sizes etc. Some 
of these can be seen in the [responsive image](static/files/responsive-design.jpg). This has been taken from the website:
http://ami.responsivedesign.is/#

There are a few major resposive choices, detailed below.

1. When viewing on a laptop the search results present their information in a different way. The incident description,
date and whether it had been reported are shown in their own colour on the right of the card.

2. The pictures of staff and descriptions shift to being alongside each other once on the laptop/ landscape iPad Pro 
screen.
___
<span id="deployment"></span>
## Deployment

<span id="deploymentLive"></span>
Deployment – Live Website  

   1.	Create repository in GitHub and give it a relevant name.
   

<span id="deploymentLocal"></span>
Deployment – Run Locally  

   1.	Again, click on the repository called The-Book-Club.
   


___
<span id="credit"></span>
## Credit

<span id="tutorials"></span>
<ins>Tutorials</ins>

For all of the following tutorials, I have edited the code necessary for my project. 

This tutorial helped me to make sure my urls were clearer.
https://restfulapi.net/resource-naming/

This tutorial helped me to alphabetise some areas of results.
https://stackoverflow.com/questions/1959386/how-do-you-sort-a-list-in-jinja2

This tutorial helped me to use the date-time function in python
https://www.dataquest.io/blog/python-datetime-tutorial/

This tutorial helped me to save the date from the input into the mongoDB.
https://stackoverflow.com/questions/58160212/how-to-save-date-from-datepicker-into-database-in-sqlalchemy-flask-application

This tutorial helped me to validate a password live for when users are deciding their first password.
https://www.w3resource.com/javascript/form/password-validation.php


This link helped to set up Flash-messages.
https://www.youtube.com/watch?v=DFCKWhoiHZ4

This tutorial helped me to store things to the Flask session.
https://pythonise.com/series/learning-flask/flask-session-object

This tutorial helped me to set up a back-end validation check which matched the live JS version.
https://www.geeksforgeeks.org/python-program-check-validity-password/


This tutorial helped me to check if there was a value in the array that matched the criteria.
https://stackoverflow.com/questions/55957237/checking-if-input-value-matches-the-array-items

This tutorial helped me to check the email live to see if there was already a user with that account.
https://stackoverflow.com/questions/14411235/while-typing-in-a-text-input-field-printing-the-content-typed-in-a-div

This link helped me to process a list of emails in python and access them in JS.
https://groups.google.com/forum/#!topic/web2py/OmwTo1ZsFN4

This link helped me to process a list from python into a json file.
https://stackoverflow.com/questions/23038710/accessing-python-list-in-javascript-as-an-array

This helped me to understand how I could get the value from a select option.
http://jsfiddle.net/YPsqQ/

Tutorial on how to hash a password
https://nitratine.net/blog/post/how-to-hash-passwords-in-python/


<span id="media"></span>
<ins>Media</ins>

To generate my favicon, I used this website: 

https://www.favicon.cc/



<span id="acknowledgements"></span>
<ins>Acknowledgements</ins>  

I used the Government's own website when choosing which categorise would be available. There are a few names I have
changed on the grounds that there are more colloquial terms available. Eg. 'Sex' has been changed to 'sexism'.
Please find the link attached below:
https://www.gov.uk/discrimination-your-rights


___
<span id="project"></span>
## Project Evaluation






<span id="improvements"></span>
### Improvements

I would like to refactor the code that chooses whether you can search by a date.
The menu could have icons on it as a visual reminder.
There could be a dashboard button like the settings button on the pages as a shortcut.
I need to use an ajax to live check the email addresses when signing up as the regex will become slow and cumbersome 
as the users grow.





___







