TrueSophia
===========================================

Description
-----------

**TrueSophia** is a website that stores scientific journal articles and scientific papers. It has several categories of subjects (Physics, Maths, etc). The user can log in with their Google or Facebook account and add their favourite scientific papers to the various categories. Users can also download previously added papers by right clicking on the pdf image of the scientific paper.

## Required Libraries and Dependencies
The project code requires the following software:

* Python 2.7.x
* [SQLAlchemy](http://www.sqlalchemy.org/) 0.8.4 or higher (a Python SQL toolkit)
* [Flask](http://flask.pocoo.org/) 0.10.1 or higher (a web development microframework)
* The following Python packages:
    * oauth2client
    * requests
    * httplib2
    * flask-seasurf (a CSRF defence)


You can run the project in a Vagrant managed virtual machine (VM) which includes all the
required dependencies (see below for how to run the VM). For this you will need
[Vagrant](https://www.vagrantup.com/downloads) and
[VirtualBox](https://www.virtualbox.org/wiki/Downloads) software installed on your
system.

## Project contents
This project consists for the following files in the `catalog` directory:

* `application.py` - The main Python script that serves the website. If no database
    is found, one is created and populated by `populate_database.py`.
* `fb_client_secrets.json` - Client secrets for Facebook OAuth login.
* `g_client_secrets.json` - Client secrets for Google OAuth login.
* `README.md` - This read me file.
* `/catalog` - Directory containing the `catalog` package.
    * `/static` - Directory containing CSS and Javascript for the website.
        Includes a copy of the [Material Design Lite](http://www.getmdl.io/)
        web framework by Google and
        [JavaScript Cookie](https://github.com/js-cookie/js-cookie/), a JavaScript
        API for handling cookies.
    * `/templates` - Directory containing the HTML templates for the website, using
        the [Jinja 2](http://jinja.pocoo.org/docs/dev/) templating language for Python.
        See next section for more details on contents.
    * `__init__.py` - Initialises the Flask app and imports the URL routes.
    * `auth.py` - Handles the login and logout of users using OAuth.
    * `connect_to_database.py` - Function for connecting to the database.
    * `database_setup.py` - Defines the database classes and creates an empty database.
    * `file_management.py` - Functions for handling user uploaded image files.
    * `json_endpoint.py` - Returns the data in JSON format.
    * `populate_database.py` - Inserts a selection of animals into the database.
    * `views.py` - Provides backend code to produce web page views of the data and forms
        for creating, editing and deleting animals. It also ensures that only the user
        that added an animal can edit or delete it.
    * `xml_generator.py` - Returns the data in XML format.

### Templates
The `/templates` directory contains the following files, written in HTML and the Jinja2
templating language:

* `add_item_button.html` - Renders a MDL button on a page to add a new item (paper).
* `delete_item.html` - Delete paper confirmation page.
* `edit_item.html` - Form to edit the details of a paper.
* `homepage.html` - The default page, which lists the 10 latest papers that were added.
* `item.html` - A page that displays a single paper and its details.
* `items.html` - A page that lists the papers belonging to a single category.
* `layout.html` - This defines the common layout of the website and is the parent
    for all the other template pages.
* `login.html` - A login page featuring OAuth Goolge+ and Facebook login buttons.
* `my_items.html` - A page for displaying the pages you have added to the website.
* `new_item.html` - A form for adding a new paper.

## How to Run the Project
Download the project zip file to you computer and unzip the file. Or clone this
repository to your desktop.

Open the text-based interface for your operating system (e.g. the terminal
window in Linux, the command prompt in Windows).

Navigate to the project directory and then enter the `vagrant` directory.

### Bringing the VM up
Bring up the VM with the following command:

```bash
vagrant up
```

The first time you run this command it will take awhile, as the VM image needs to
be downloaded.

You can then log into the VM with the following command:

```bash
vagrant ssh
```

More detailed instructions for installing the Vagrant VM can be found
[here](https://www.udacity.com/wiki/ud197/install-vagrant).

### Make sure you're in the right place
Once inside the VM, navigate to the tournament directory with this command:

```bash
cd /vagrant/catalog
```

### OAuth setup
In order to log in to the web app, you will need to get either a Google+ or Facebook
(or both) OAuth app ID and secret. For Google, go to the
[Google Developers Console](https://console.developers.google.com/) and for Facebook,
go to [Facebook Login](https://developers.facebook.com/products/login).

Once you have your credentials, put the IDs and secrets in the `fb_client_secrets.json`
file for Facebook and `g_client_secrets.json` for Google.

You will now be able to log in to the app.

### Run application.py
On the first run of `application.py` there will be no database present, so it creates
one and populates it with sample data. On the command line do:

```bash
python application.py
```

It then starts a web server that serves the application. To view the application,
go to the following address using a browser on the host system:

```
http://localhost:8000/
```

You should see the latest papers that were added to the database. Have a read of the papers in the different categories. You can download them by right clicking on the pdf image in the item category. To upload a document from your own device , you'll need to log in first with either a Google or Facebook account.


### Shutting the VM down
When you are finished with the VM, press `Ctrl-D` to logout of it and shut it down
with this command:

```bash
vagrant halt
```

## Extra Credit Description
The following features are present to earn an extra credit from Udacity.

### XML Endpoint
Database contents can be obtained in XML form by going to
[http://localhost:8000/catalog.xml](http://localhost:8000/catalog.xml). Depending
on your browser, you may need to view source of the page to view the XML file. You
can do this by right-clicking and selecting `View Page Source` from the menu.

### Papers
The Sophia app allows the user to add, edit and delete an image for each paper. An
image may either be uploaded to the app or specified with the URL of an image. If
a paper has an image associated with it, it is displayed to all users.

### Cross-site Request Forgery Protection
The app uses the Flask plugin [SeaSurf](https://flask-seasurf.readthedocs.org/en/latest/),
in order to protect against cross-site request forgery. An addition cookie is stored
in the client containing a nonce. When a user logs in, adds, edits or deletes an item,
the contents of this cookie is checked to make sure it matches the value on the server.
If it does not match or is missing, no change to the database will be made.

### References
I modeled the layout of my "Journal App" on the "Zoo Management App" by Steven Wooding
https://github.com/SteveWooding/fullstack-nanodegree-vm/tree/master/vagrant/catalog.
