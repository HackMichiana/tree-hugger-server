# South Bend Tree Hugger Server

# Overview

The South Bend parks department needs a way to geotag trees on public property. This information could be used for the following:

* Planning where to plant new trees
* Identifying diseased trees for maintenance
* Informing storm cleanup
* Science!

The basic collection of tree info is simple. We need a few approximate measurements, a GPS location, a picture of the tree from afar and a picture of a leaf. In addition the basic collection form we need user accounts with social authentication, data exploration tools and methods of data extraction to give to the city.


# Tech

This project uses the [Django framework](https://www.djangoproject.com/) and requires the following to be installed.

* Python
* SQLite3
* [Bower](http://bower.io/)

It is highly recommended to run this (and all Python apps) under [virualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/) to avoid polluting the global Python environment. Install globally at your peril, you have been warned.

```
git clone git@github.com:HackMichiana/tree-hugger-server.git
cd tree-hugger-server
pip install -r requirements.txt
./manage.py migrate
./manage.py loaddata tree_hugger/fixtures/admin.json
./manage.py bower install
./manage.py runserver
```

Browse to http://localhost:8000 to see the map view. http://localhost:8000/add-a-tree contains the HTML5 tree submission form.
To view the admin navigate to http://localhost:8000/admin and log in with

* username: `admin`
* password: `admin`

The `admin` user was loaded in the `loaddata` step and should only be created for development instances. The admin user should not exist for production deployments!

There is also a REST API at `/api/v1/?format=json` powered by [Tastypie](http://tastypieapi.org/).
