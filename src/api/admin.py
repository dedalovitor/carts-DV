import os
from flask_admin import Admin
from .models import db, User, User_region, Region, Restoration, Accommodation, Experience, Patrimony, Favorites, Comments, Pet
from flask_admin.contrib.sqla import ModelView

def setup_admin(app):
    app.secret_key = os.environ.get('FLASK_APP_KEY', 'sample key')
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
    admin = Admin(app, name='4Geeks Admin', template_mode='bootstrap3')

    class MyModel(ModelView):
        column_display_pk = True

    # Add your models here, for example this is how we add a the User model to the admin
    admin.add_view(MyModel(User, db.session))
    admin.add_view(MyModel(User_region, db.session))
    admin.add_view(MyModel(Region, db.session))
    admin.add_view(MyModel(Restoration, db.session))
    admin.add_view(MyModel(Accommodation, db.session))
    admin.add_view(MyModel(Experience, db.session))
    admin.add_view(MyModel(Patrimony, db.session))
    admin.add_view(MyModel(Favorites, db.session))
    admin.add_view(MyModel(Comments, db.session))
    admin.add_view(MyModel(Pet, db.session))
 