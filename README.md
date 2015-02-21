# South Bend Tree Hugger Server

This project uses the [Django framework](https://www.djangoproject.com/) and requires the following to be installed.

* Python
* SQLite3

It is highly recommended to run this (and all Python apps) under [virualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/) to avoid polluting the global Python environment. Install globally at your peril, you have been warned.

```
git clone git@github.com:HackMichiana/tree-hugger-server.git
cd tree-hugger-server
pip install -r requirements.txt
./manage.py migrate
./manage.py loaddata tree_hugger/fixtures/admin.json
./manage.py runserver
```

Browse to http://localhost:8000 to see the site. There may not be anything there yet however.
To view the admin navigate to http://localhost:8000/admin and log in with

* username: `admin`
* password: `admin`

The `admin` user was loaded in the `loaddata` step and should only be created for development instances. The admin user should not exist for production deployments!
