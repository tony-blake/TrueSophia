#!/usr/bin/env python
"""Main Python script that starts the catalog app.

It checks to see if the database file exists and if not it creates the database
and populates it with some sample content, for demonstration purposes.
"""
import os.path

from catalog import app
from catalog.database_setup import create_db
from catalog.populate_database import populate_database

if __name__ == '__main__':
    # App configuration
    app.config['DATABASE_URL'] = 'sqlite:///itemcatalog.db'
    #app.config['DATABASE_URL'] = 'postgresql://catalog:PASSWORD@localhost/catalog'
    app.config['UPLOAD_FOLDER'] = '/vagrant/catalog/item_images'
    app.config['OAUTH_SECRETS_LOCATION'] = ''
    app.config['ALLOWED_EXTENSIONS'] = set(['pdf','jpg', 'jpeg', 'png', 'gif'])
    app.config['MAX_CONTENT_LENGTH'] = 200 * 1024 * 1024  # 200 MB
    app.secret_key = 'super_secret_key'  # This needs changing in production env

    if app.config['DATABASE_URL'] == 'sqlite:///itemcatalog.db':
        if os.path.isfile('itemcatalog.db') is False:
            create_db(app.config['DATABASE_URL'])
            populate_database()
    else:  # for postgresql
        create_db(app.config['DATABASE_URL'])
        populate_database()

    app.debug = True
    app.run(host='0.0.0.0', port=8000)
