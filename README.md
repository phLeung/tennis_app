Author: Philip Leung


This is a personal learning project for web app development. The program is a web interface that
runs in a development environment.  This program is meant to run on development environment as I have not
had enough time to deploy it to a production environment. I used jquery for developing the user interface since I am more familiar with this framework than React (which I am currently learning). I used Flask and
Postgres for the backend development of the web interface. Although I have developed the backend with Flask,Postgres, and Flask SQLAlchemy, I have not had the time to implement all the backend features
of the application such as adding a player to the database or displaying the results of the two players
and the associated match after the end of the match. However, I have successfully tested the data models
I have developed via unit testing. Since this app is meant to run on a development server, you must
create the Postgres database in order to run the tests for the data models as I will go over in the setup
instructions. I used the flask python framework for developing the backend because
it is the python web framework that I more familiar with. I chose Postgres because it would best suited
for potential scalability capabilities. On the other hand, I used sqlite3 instead of Postgres for testing the data models that I have developed via flask SQLAlchemy because it was easier to setup. Because it
is easier to setup, I will document setting up sqlite and configuring it with flask sqlalchemy. I will
also document setting up the Postgres sql server and configuring it with flask sqlalchemy, though
this is optional and not required for the setup instructions. Overall, I think it makes sense to configure
sqlite3 with flask_sqlalchemy for testing the data models and for potential implementation. On the other hand,
if the data for this application were to grow to a size that can't be handled with sqlite3, then it would be
best to consider using Postgres.


As the flask server is running, the web interface will initially take you to a web page where a user must fill out a form. The user must enter two names of the players. These two fields are required and can't be left empty. The user can choose between 3 set matches and 5 set matches. The user can also choose which tiebreak
formats to use. Once the user hits the submit button after filling out the form, the user will be
able to keep track of the tennis score between two players.  The blue colored indicator is used
to denote which player is serving. The User can control which player serves. The tennis scoring mechanism
handles events such as deuce and tiebreaks.

Setup Instructions:

Please look at the requirements text to check for python dependencies that
must be installed via pip

Before setting up this program on your environment, you must do the following:
(Using Sqlite3)
You must install the python dependencies via pip3
To run the tests on the sqlite3 database, you must set the environment variable to the URI of sqlite
when creating the database.
This can be done by adding the following to the configuration file .bash_profile (OS X) or .profile (Linux).
For example, in the configuration file for .bash_profile (OS X) or .profile for (Linux) you should the
following line:
export TENNIS_URI="sqlite:///tennis_scores.sqlite3"
Once you do that, save and exit the configuration file and execute with the following command:
source ~/.bash_profile (OS) or
source ~/.profile (Linux)

With the setup of the sqlite database completed, you must configure the environment variables for the
flask framework before starting the application.
go to the file path of the directory for application:
~/flashpoint_test/tennis_score_app/
When you get to this directory set the following flask environment variables on the command line:
export FLASK_CONFIG=config.py
export FLASK_ENV=development

Once that is done, run the python program run.py to run the flask server and access application.
As the flask server is running, type localhost:5000 on your web browser's url to access the web interface.
The home page will ask you to fill out a form before interacting with the tennis scoring mechanism.




Optional database setup for Postgres on Mac:
If you don't have Postgres installed on the Mac, then go to this link https://postgresapp.com
to download it.
Once downloaded, install the python driver for postgres with the following command:
pip3 install psycopg2
Execute the command psql to access the CLI for postgres.
create the database using the following command:
CREATE DATABASE tennis_scores;
The database name tennis_scores is arbitrary. With that done, you will have created a database for
the tennis scoring application.
You can open and edit the configuration files using nano or another text editor.
After that, set the environment variable to URI (Uniform Resource Identifier) of postgres in the configuration
file for .bash_profile (OS X) or .profile for (Linux) with the following line:
export TENNIS_URI="postgresql://postgres:postgres@localhost:5432/tennis_scores"
Once you do that, save and exit the configuration file and execute with the following command:
source ~/.bash_profile (OS) or
source ~/.profile (Linux)

TODO:
create web page for displaying database information such as scores.
create sign in page.
redesign the score board layout.
