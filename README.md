#Tournament Results Database
###(In fullfillment of Udacity's Full Stack Developer Program)

The Tournament Results Database was developed part of Udacity's Full Stack Developer Nanodegree. It contains the backend code for a [Swiss-System Tournament](https://en.wikipedia.org/wiki/Swiss-system_tournament). The purpose of this project was to develop a database and functions that would pass all tests when run using the *tournament_test.py* file. There is no end user interface (UI) for the software for entering data or generating reports.

##Table of Contents



##Functionality
------------------------
The *Tournament Results Database* contains functionality for adding tournaments, participants, and match data (rounds). Match data contains information about who is matched with whom and the outcome of the match. There are functions for querying the data for comparison and output. Functions are commented as to their purpose along with the code within the *tournament.py* file.

##Structure Overview
------------------------

| Table         | Description                           | Key(s)                           |
| ------------- |:-------------------------------------:| --------------------------------:|
| tournaments   | Supports multiple tournaments         | t_id                             |
| participants  | Contains participant name and hometown| p_id                             |
| rounds        | Data for registration & matches       | t_id (foreign), player (foreign) |

##Technologies
------------------------

| Tool Used  | Purpose                                   | Notes                                       | About         |
| ---------- |:-----------------------------------------:|--------------------------------------------:| --------------:|
| Windows OS | developer platform                        | Virtual Machine (VM) used to simulate Linux | [More info](https://www.virtualbox.org/wiki/VirtualBox) |
| VirtualBox | software to run virtual machine           | Configured to run Linux server              | [More info](https://www.virtualbox.org/wiki/VirtualBox) |
| Vagrant    | software to configure/manage VM           | Shares files between host computer & VM     | [More info](https://www.vagrantup.com/about.html) |
| GitHub     | provide configuration instructions for VM | Fork & clone Udacity repo (link below)      | [More info](https://en.wikipedia.org/wiki/GitHub) |
| Git Bash   | run commands from VM                      | Provides Unix-Style terminal                | [More info](https://en.wikipedia.org/wiki/Bash_(Unix_shell)) |
| PostgreSQL | database for persistant data storage      | Runs on Virtual Machine (VM)                | [More info](https://www.postgresql.org/about/) |
| psql       | allows interaction with the PostgreSQL db | Run commands through Git Bash               | [More info](https://www.postgresql.org/about/) |
| Python     | language used to program functions        | Python files detailed below                 | [More info](https://www.python.org/about/) |

##Folders & Files
------------------------
| File               | Purpose                                | Notes                                       |
| ------------------ |:--------------------------------------:|--------------------------------------------:|
| tournament.sql     | db schema                              | May be used to create schema with psql (see below) |
| tournament.py      | core code for application              | Functions are accessed by running *tournament_test.py* |
| tournament_test.py | file to test *tournament.py* functions | Provided by [Udacity](http://www.udacity.com) |

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