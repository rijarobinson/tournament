#Tournament Results Database
###(In fullfillment of Udacity's Full Stack Developer Program)

The Tournament Results Database was developed part of Udacity's Full Stack Developer Nanodegree. It contains the backend code for a [https://en.wikipedia.org/wiki/Swiss-system_tournament](Swiss-System Tournament). The purpose of this project was to develop a database and functions that would pass all tests when run using the *tournament_test.py* file.

#Features Overview
------------------------
The database contains four entites, tournaments, participants, and rounds.

| Tables        | Are           | Cool  |
| ------------- |:-------------:| -----:|
| col 3 is      | right-aligned | $1600 |
| col 2 is      | centered      |   $12 |
| zebra stripes | are neat      |    $1 |

##Technologies
------------------------
A PostgreSQL database is used to store players and the records of matches. It is developed on Virtual Box with Vagrant File (Ubuntu OS + PostgreSQL DB+ psql) provided by Udacity.

This site uses a PostgreSQL database for persistant data storage and uses Virtual Box with Vagrant Virtual Machine, Python, JavaScript, and bootstrap framework. Libraries used are described below Folders and Files section.

##Folders & Files
------------------------
* app.yaml
* blog.py
* index.yaml
* templates/base.html
* templates/editcomment.html
* templates/front.html
* templates/login.html
* templates/newpost.html
* templates/permalink.html
* templates/post.html
* templates/signup.html
* templates/welcome.html
* css/bootstrap.css
* css/style.css
* css/bootstrap.min.css
* images (folder)

**blog.py** is the main python file that contains the code for running the app.

**app.yaml and index.yaml** are used by GAE. Please refer to GAE documention regarding these files.

**templates/base.html** contains the base template for the site.

**templates/front.html** displays the main site page. The post.html is displayed within this page.

**templates/permalink.html** displays the individual post. Post.html is also used within this page. This page contains commenting functionality. It is also displayed after a new post is created.

**templates/post.html** is contained within the front and permalink html files and displays the details of an individual post.

**templates/newpost.html** is the form that allows for creating a new animal story. It is also used when a user edits their own post.

**templates/editcomment.html** is a form that is used when a user edits their own comment.

**templates/login.html** is for an existing user to login.

**templates/signup.html** is for a new user to create an account.

**templates/welcome.html** displays a welcome message to the new or existing user.

**css/bootstrap.css** contains the framework style code. This file is not directly referenced by the website. It is the full version of bootstrip.min.css for development use and has not been modified. Final version of website will not include this file.

**css/bootstrap.min.css** contains the minified version of bootstrap.css and is not modified from it's original version. Any style changes are in the style.css file.

**css/style.css** contains the modifications and additions to the style code.

**images** folder contains the images required for the site.

##Libraries & Modules
* os
* re
* webapp2
* jinja2
* random
* string
* hashlib
* time
* db (from GAE)

##Using the Site
**To run the site**, place all files in the same folder with the same structure provided. Create a new application on the GAE Cloud Platform. Rename the application from animal stories to your GAE application name in the **app.yaml** file. Use desktop GAE to Add the application and run locally or deploy. Please see GAE documentation for further information.

**To customize the files**, you can open the **base.html** file in your favorite text editor and make changes as desired. You can review the references to bootstrap using the bootstrap.css file, but good practice is to make modifications/additions in a separate css file (in this case, you can change the style.css file). Save the files and refresh the site to see your new web page.

Mockup/basic design ideas for this application were provided by [Udacity](http://www.Udacity.com). Additional instruction on Front End Development is available by signing up for a class on their site. Bootstrap provides the framework,and Google App Engine serves the content. Additional enhancements by Marija Robinson.

The implemented project can be accessed at [http://animal-stories.appspot.com/blog](animal-stories.appspot.com).

I welcome any feedback on this project at marija@springmail.com.