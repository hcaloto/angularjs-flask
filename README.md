# AngularJS and Flask #
-------------

Example of an application with Flask, AngularJS and Bootstrap. This also uses MYSQL as database.

## Installation and setup of MySQL ##
### Install MySQL Server ###
##### Mac OS #####
```
$ brew install mysql
$ mysql.server restart
```
##### Ubuntu #####
```
$ apt-get install mysql-server
$ apt-get install libmysqlclient-dev python-dev
$ service mysql restart
```
### Setup a MySQL database ###
##### Connect to mysql server #####
```
$ mysql -u root -p
```
##### Create a MySQL user #####
```
# Create the user
mysql> CREATE USER 'developer'@'localhost' IDENTIFIED BY 'default';

# Allow the user to read, edit and execute any task over any database
GRANT ALL PRIVILEGES ON * . * TO 'developer'@'localhost';

# Refresh privileges
FLUSH PRIVILEGES;
```
##### Create a database #####
```
mysql> CREATE DATABASE test;
```
##### Create a table #####
```
mysql> USE test;
mysql> CREATE TABLE user (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, username VARCHAR(100), password VARCHAR(100), token VARCHAR(250));
```
##### Add an user #####
```
mysql> INSERT INTO user (username, password) VALUES ("hcaloto", "mypass");
mysql> exit
```
-------------
## Install Python requirements ##
##### Create virtualenv #####
```
$ pip install virtualenv
$ virtualenv angularflask
```
##### Install specific requirements #####
```
$ source angularflask/bin/activate
$ pip install -r requirements.txt
```
-------------
## Running ##
```
$ source angularflask/bin/activate
$ python manage.py
```
--------------------
## Testing ##
```
$ make
```
--------------------
## Links ##
> **MySQL:**
> - [Installation on Mac OS](http://blog.joefallon.net/2013/10/install-mysql-on-mac-osx-using-homebrew/)
> - [Installation on Ubuntu 16.04](https://help.ubuntu.com/16.04/serverguide/mysql.html)
> - [MySQL tutorial](https://www.digitalocean.com/community/tutorials/a-basic-mysql-tutorial)
> - [Cursor Documentation](http://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlcursor.html<U+200B>)
> - [MySQL & Flask](http://www.halfcooked.com/mt/archives/000969.html)

> **Markdown:**
> - Editor: [Dillinger](http://dillinger.io/)