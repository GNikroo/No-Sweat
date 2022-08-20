Readme
# No Sweat!
No Sweat! is a forum for fitness enthusiasts--from beginner to expert and casual to committed—to get together to share experiences and support. This project has been a labor of love which I have developed for Code Institute as my milestone project, showcasing my skills as a full stack developer. 
![Responsivity](static/images/nosweat-responsive.png) 
The live website can be found on [Heroku](https://no-sweat-fitforum.herokuapp.com/) 
To open links in a new browser tab, press CTRL + Click.  
## Table of Contents
* [User Experience Design (UX)](#ux)
    * [Strategy](#strategy)
        * [Site Functionality](#site-functionality)
    * [Scope](#scope)
        * [Features](#features)
    * [Structure](#structure)
    * [Skeleton](#skeleton)
    * [Surface](#surface)
* [Testing Strategy](#testing-strategy)
    * [Validator Testing](#validator-testing)
    * [Bugs](#bugs)
* [Deployment](#deployment)
* [Credits](#credits)
* [Media](#media)
    * [Content](#content)
    * [Acknowledgements](#acknowledgements) 
 

## UX 
### Strategy 
* As a **Site User** I can **view posts in a list** so that **I can easily see what other users have shared / posted**. 

* As a **Site User** I can **see how many likes the post has** so that **I can decide if the post has valuable information**. 

* As a **Site User** I can **see comments** so that **I can read the discussion about the post**. 

* As a **Site User** I can **view a particular post** so that **I can read it in its entirety**. 

* As a **Site User** I can **search the website** so that **I can find relevant posts**. 

* As a **Site User** I can **create an account** so that **I can post my own content as well as comment and like others**. 

* As a **Site User** I can **create a post** so that **I can share my experiences and receive feedback from others**. 

* As a **Site User** I can **comment on posts** so that **I can be a part of the discussions**. 

* As a **Site User** I can **like and unlike posts and comments** so that **I can show support for other users**. 

* As a **Site User** I can **update and delete my own posts** so that **I can manage my content** 

* As a **Site User** I can **update and delete my own comments** so that **I can manage my content** 

* As a **Site Admin** I can **remove comments and posts** so that **I can filter out objectionable content**. 

#### Site Functionality 
The goal of this app is to provide a judgement free space place for those interested in fitness to connect with others who have similar goals, interest, and/or experience. Unauthorized users can choose to simply observe with access to read posts and comments. Users can create an account to create their own posts or comment on posts. Users can also edit or delete either posts or comments they’ve made. 

### Scope 
#### Features  
* Responsive Design across the range of devices available.  
* Easy to navigate post list makes it obvious to find which posts might interest a user. 
* User profiles allow for easy access to a creator’s posts. 
* All buttons are easy to find and indicate their purpose through color and labels 
* Users can edit and delete their own posts and comments in order to manage their own content. 
* Site visitors and registered users have access to search keywords in both post titles and content to find entries that match their interest. 

### Structure 
User Stories: Acceptance Criteria: Implementation

> As a Site User I can view posts in a list so that I can easily see what other users have shared / posted. 
* **Acceptance Criteria:**
* The post list layout should be presented with a uniform look to each post and in a clear grid. 
* **Implementation:**
* Using Bootstrap 5 the post list layout is in a fixed grid that shows 6 posts per page giving the user a clear visual of each post. 

> As a Site User I can see how many likes the post has so that I can decide if the post has valuable information. 
* **Acceptance Criteria:** 
* Post should show how many people have taken the time to like a post in order to visually boost its importance to users. 
* **Implementation:**
* Each post has a “likes” counter which is represented by a pink heart. The number increases by one with each like the post receives. The count is visible in the post’s detail and in the post list views. 

> As a Site User I can see comments so that I can read the discussion about the post. 
* **Acceptance Criteria:**
* Comments should be visible to all users regardless of registration status. 
* **Implementation:**
* Users can view all comments on individual posts as well as a comment counter from the list view. 

> As a Site User I can view a particular post so that I can read it in its entirety. 
* **Acceptance Criteria:**
* Posts should provide links from the list view that allow users to read it in its entirety. 
* **Implementation:**
* From the list view, a user can click on the image, title, author, or date of a given post to follow a link which then displays the corresponding post’s details. 

> As a Site User I can search the website so that I can find relevant posts. 
* **Acceptance Criteria:**
* A search bar should be provided for all users. 
* **Implementation:**
* Users can easily find the search bar located next to the site logo. Post titles and content can be search with one or more words regardless of capitalization. 

> As a Site User I can create an account so that I can post my own content as well as comment and like others. 
* **Acceptance Criteria:**
* A link should be provided for users to create an account. 
* **Implementation:**
* A link is provided for users to sign up. Once an account is created, they are able to interact with content. 

> As a Site User I can create a post so that I can share my experiences and receive feedback from others. 
* **Acceptance Criteria:**
* Registered users should be able to add individual posts. 
* **Implementation:**
* Once a user has been evaluated to be authorized by django’s allauth, a button to add a post is clearly visible below the site’s banner. 

> As a Site User I can comment on posts so that I can be a part of the discussions. 
* **Acceptance Criteria:**
* Registered users should be able to add comments to posts. 
* **Implementation:**
* Once a user has been evaluated to be authorized by django’s allauth, a form to add a comment is clearly visible at the bottom of each post’s detail. 

> As a Site User I can like and unlike posts and comments so that I can show support for other users. 
* **Acceptance Criteria:**
* Registered users should be able to like posts. 
* **Implementation:**
* Once a user has been evaluated to be authorized by django’s allauth, users can toggle the like button below each post’s content to ‘liked’ or not. 

> As a Site User I can update and delete my own posts so that I can manage my content.
* **Acceptance Criteria:** 
* A post creator should be able to edit and delete said post. 
* **Implementation:**
* Once a user has been verified to be the original creator of a post via if statements in the corresponding html, buttons will become visible to edit or delete posts they’ve created previously. 

> As a Site User I can update and delete my own comments so that I can manage my content. 
* **Acceptance Criteria:**
* A comment creator should be able to edit and delete said comment. 
* **Implementation:**
* Once a user has been verified to be the original creator of a comment via if statements in the corresponding html, buttons will become visible to edit or delete comments they’ve added previously. 

> As a Site Admin I can remove comments and posts so that I can filter out objectionable content. 
* **Acceptance Criteria:**
* Site administrators should have access to delete comments and posts. 
* **Implementation:**
* Admin’s have access to the admin portal where all posts are visible and editable. From there, an admin can delete offensive or inappropriate comments and posts.

## Future Functionality
* User stories to build future functionality:
    * As a **Site User** I can **choose to follow topics** so that **I can read content that might interest me**. 
    * As a **Site User** I can **search for and view other creator's profiles** so that **I can determine whether to follow them or not**. 
    * As a **Site User** I can **follow chosen posters** so that **I can read content that interests me**. 
    * As a **Site User** I can **view a list of suggested posters** so that **I can view a post list relevant to my interests**.
    * As a **Site User** I can **tag my post** so that **users who follow those topics will see my post**. 
    * As a **Site User** I can **click on tag links** so that **I can quickly choose which posts suit my interest in the moment**.
    * As a **Site User** I can **create draft posts** so that **I can finish writing the content later**. 
    * As a **Site User** I can **search by user profile** so that **I can connect to users I am interested in**. 
    * As a **Site User** I can **share a post** so that **others can access a post**.
    * As a **Site User** I can **register and login with a social media account** so that **I don't have to keep track of multiple plasswords or worry about account security**.

### Skeleton
* Wireframes
    * Homepage
    * ![Homepage](static/images/nosweat-wireframe-home.png)
    * Post detail
    * ![Post detail](static/images/nosweat-wireframe-post.png)
    * User profile
    * ![User profile](static/images/nosweat-wireframe-profile.png)

### Surface 
When first accessing No Sweat, all users regardless of registration status can see a list of posts filtered by most recently created. 
![Homepage](static/images/nosweat-home.png) 

From there, each post is accessible to read. 
![Post Detail](static/images/nosweat-post-detail.png) 

To interact with posts, users can sign up to the site by following the link and fill out the form. 
![Sign Up](static/images/nosweat-signup.png) 
![Log In](static/images/nosweat-login.png) 

Once finished, a registered user can: 
* Create a post 
![Add a post](static/images/nosweat-addpost.png) 
![Fill in form](static/images/nosweat-addpost-form.png) 

* Edit and/or delete the post 
![Editable post](static/images/nosweat-posttoedit.png) 
![Edited post](static/images/nosweat-editedpost.png) 
![Delete](static/images/nosweat-justchecking.png) 
![Deleted post](static/images/nosweat-deletedpost.png) 

* Add a comment 
![Leave a comment form](static/images/nosweat-leavecomment.png) 
![Comment added](static/images/nosweat-commentadded.jpeg) 

* Edit and/or delete the comment 
![Edited comment](static/images/nosweat-updatedcomment.png) 
![Deleted comment](static/images/nosweat-commentdeleted.jpeg)  

* Toggle the like button for a given post 
![Toggle like](static/images/nosweat-like.png)  

* View their own posts in their profile 
![Profile view](static/images/nosweat-profile.png) 

## Testing Strategy  
### Manual Testing during development 
* During the development and deployment stage, I ensured that:
    * Initial launch was successful
    * Rigorous testing of posting capabilities for a variety of users: All users have successfully added posts
    * Rigorous testing of commenting capabilities for a variety of users: All users have successfully added comments
    * Only authorized users can add posts and leave comments
    * Only users verified to have created posts and comments are able to delete or edit
    * Fields to edit comments and posts are prepopulated with initial data
    * Only verified users can like posts
    * Users who have signed up have access to their user profile
    * Alert messages display accurately
    * Users were authorized through CSRF-tokens and if statements that restrict visibility based on requirements being met
    * User uploaded images display correctly and can be updated using the proper form
    * Bootstrap delivers a visually appealing and user-friendly app across all screen sizes
    * Site users cannot access admin portal.

* Unittest 
    * Due to time constraints, tests were not built for this project. 

### Validator Testing
* HTML - W3C Validator
    * After removing django tags, no errors were found.

* CSS - W3C CSS Validation Service - Jigsaw
    * No errors were found.

* PEP8 – Python Validation Service
    * Small errors found with white space. Fixed and rechecked to find no errors.

* Lighthouse
    * Mobile: 97, 94, 92, 100
    ![Mobile](static/images/lighthouse-mobile.png)
    * Desktop: 100, 86, 100, 100
    ![Desktop](static/images/lighthouse-dektop.png)

### Bugs
* A number of bugs were found during production and resolved before deployment.
* Following deployment:
    * A bug has been found when attempting to retrieve a forgotten password. Removed the broken link and will include it in future additional functionality.
    * CSS failed to load and produced error: MIME type ('text/html') is not a supported stylesheet MIME type. After some research I had turned debug on while fixing some CSS and redirects. I pushed the app without changing debug back to False. Once I did so, the CSS loaded as expected.

## Deployment  
* My site was deployed to [Heroku](https://no-sweat-fitforum.herokuapp.com/). After creating a secure environment, I created an app on Heroku.
    * Create new app
    * Attach Heroku Postgres as Database in resources
    * Configured variables by matching keys and values both on heroku and in my secure environment
    * Connected the appropriate repository
* After building the app in my IDE, I made a final deployment.
    * Changed debug to false in settings
    * Added X-Frame-Options: SAMEORIGIN to settings
    * Navigated to the deploy option in my app on heroku
    * Deployed branch

## Credits  
### Media 
* All images were downloaded and used with permission from [Pexels](https://www.pexels.com/). 
* Favicon was created and downloaded with permission from [freefavicon](https://freefavicon.com/).  

### Content  
* The core html is from Code Institute’s I Think Therefore I Blog walkthrough. I have added, removed, and altered what was necessary to create a unique forum that fits my purpose. 
* The search bar was created with assistance from Code with Stein found [here](https://codewithstein.com/adding-a-simple-search-30-days-of-django/) 

### Acknowledgements
* The logic behind this website required help from those on the Code Institute slack workspace as well as the Code Institute tutor team for me to understand. My mentor Rahul helped me to understand the logic behind my views in creating CRUD functionality. I now feel confident in python and django to build user-friendly and functional apps. Thank you all!