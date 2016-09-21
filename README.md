#Tournament Results Database
###(In fullfillment of Udacity's Full Stack Developer Program)

The Tournament Results Database was developed part of Udacity's Full Stack Developer Nanodegree. It contains the backend code for a [Swiss-System Tournament](https://en.wikipedia.org/wiki/Swiss-system_tournament). The purpose of this project was to develop a database and functions that would pass all tests when run using the *tournament_test.py* file. There is no end user interface (UI) for the software for entering data or generating reports.

##Table of Contents
 * [Functionality](#functionality)
 * [Structure Overview](#structure-overview)
 * [Technologies](#technologies)
 * [Folders & Files](#folders-files)
 * [Libraries & Modules](#libraries-modules)
 * [Using the Software](#using-software)

<a id="functionality"></a>
##Functionality
The *Tournament Results Database* contains functionality for adding tournaments, participants, and match data (rounds). Match data contains information about who is matched with whom and the outcome of the match. There are functions for querying the data for comparison and output. Functions are commented as to their purpose along with the code within the *tournament.py* file.
<a id="structure-overview"></a>
##Structure Overview

| Table         | Description                           | Key(s)                           |
| ------------- | ------------------------------------- | -------------------------------- |
| tournaments   | Supports multiple tournaments         | t_id                             |
| participants  | Contains participant name and hometown| p_id                             |
| rounds        | Data for registration & matches       | t_id (foreign), player (foreign) |

##Technologies <a id="technologies"></a>

| Tool Used  | Purpose                                   | Notes                                       | About         |
| ---------- | ----------------------------------------- | ------------------------------------------- | ------------- |
| Windows OS | developer platform                        | Virtual Machine (VM) used to simulate Linux | [More info](https://www.virtualbox.org/wiki/VirtualBox) |
| VirtualBox | software to run virtual machine           | Configured to run Linux server              | [More info](https://www.virtualbox.org/wiki/VirtualBox) |
| Vagrant    | software to configure/manage VM           | Shares files between host computer & VM     | [More info](https://www.vagrantup.com/about.html) |
| GitHub     | provide configuration instructions for VM | Fork & clone Udacity repo (link below)      | [More info](https://en.wikipedia.org/wiki/GitHub) |
| Git Bash   | run commands from VM                      | Provides Unix-Style terminal                | [More info](https://en.wikipedia.org/wiki/Bash_(Unix_shell)) |
| PostgreSQL | database for persistant data storage      | Runs on Virtual Machine (VM)                | [More info](https://www.postgresql.org/about/) |
| psql       | allows interaction with the PostgreSQL db | Run commands through Git Bash               | [More info](https://www.postgresql.org/about/) |
| Python     | language used to program functions        | Python files detailed below                 | [More info](https://www.python.org/about/) |
<a id="folders-files"></a>
##Folders & Files

| File               | Purpose                                | Notes                                       |
| ------------------ | -------------------------------------- | ------------------------------------------- |
| tournament.sql     | db schema                              | May be used to create schema with psql (see below) |
| tournament.py      | core code for application              | Functions are accessed by running *tournament_test.py* |
| tournament_test.py | file to test *tournament.py* functions | Provided by [Udacity](http://www.udacity.com) |
<a id="libraries-modules"></a>
##Libraries & Modules
| Library or Module | Purpose                                  |
| ----------------- | ---------------------------------------- |
| psycopg2          | API for PostgreSQL db use                |
| bleach            | used to clean input of malicious scripts |
<a id="using-software"></a>
##Using the Software
**To run the site**
1. Install [Git](https://git-scm.com/downloads) in order to use Git Bash Unix-Style terminal.
2. Install [VirtualBox](https://www.virtualbox.org/wiki/Downloads). No need for the extension pack or SDK. Do not launch after install.
3. Install [Vagrant](https://www.vagrantup.com/downloads.html).
4. Fetch the [GitHub repository](https://github.com/udacity/fullstack-nanodegree-vm) created for the project by first Forking, and then getting the URL from GitHub for cloning (use HTTPS).
5. Open **Git Bash** and cd to the desired directory for the application.
6. Run "git clone PASTE_CLONED_PATH_FROM_GITHUB_HERE fullstack". This creates a directory called "fullstack" within your selected folder as well as the vagrant configuration.
7. Replace the stock *tournament.py* and *tournament.sql* files with the two files in the "vagrant/tournament" folder of the same name from this repository. (The files provided by Udacity are blank, pre-project completion files.) These files may reside directly in the vagrant directory, depending upon how you've set it up.
8. Launch the Virtual Machine by running "vagrant up" in the vagrant directory ("vagrant halt" stops the VM).
9. Run "vagrant ssh" to log into the virtual machine ("exit" will log you off).
10. Run "cd /vagrant/tournament" if necessary to switch to the tournament directory.
11. Run "psql" to run the querying software.
12. At "vagrant=>", run "\i tournament.sql" to create the database and tables.
13. You can connect to the tournament database by running "\c tournament". If you would like to see a list of the tables, run "\dt". For other commands you can use in psql, check [here](http://postgresguide.com/utilities/psql.html).
12. Quit psql with "\q" and run "tournament_test.py" to see the tests run on the *tournament.py* file.

Refer to [this page](https://udacity.atlassian.net/wiki/display/BENDH/Vagrant+VM+Installation) from Udacity for additional install details and screen shots.

**To customize the files**
Feel free to modify your copy of *tournament.py* and run *tournament_test.py* to see how this affects the outcomes of the test. You can use print statements within *tournament.py* to troubleshoot your code.

Stubs and test file were provided by [Udacity](http://www.Udacity.com). Additional instruction on Back End Development is available by signing up for a class on their site. Additional enhancements by Marija Robinson.

The implemented project can be accessed at [http://animal-stories.appspot.com/blog](animal-stories.appspot.com).

I welcome any feedback on this project at marija@springmail.com.