import os
from flask_admin import Admin
from .models import db, User, User_region, Region, Restoration, Accommodation, Experience, Patrimony, Favorites, Comments, Pet
from flask_admin.contrib.sqla import ModelView

def setup_admin(app):
    app.secret_key = os.environ.get('FLASK_APP_KEY', 'sample key')
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
    admin = Admin(app, name='4Geeks Admin', template_mode='bootstrap3')

    
    # Add your models here, for example this is how we add a the User model to the admin
    admin.add_view(ModelView(User, db.session))
    admin.add_view(ModelView(User_region, db.session))
    admin.add_view(ModelView(Region, db.session))
    admin.add_view(ModelView(Restoration, db.session))
    admin.add_view(ModelView(Accommodation, db.session))
    admin.add_view(ModelView(Experience, db.session))
    admin.add_view(ModelView(Patrimony, db.session))
    admin.add_view(ModelView(Favorites, db.session))
    admin.add_view(ModelView(Comments, db.session))
    admin.add_view(ModelView(Pet, db.session))
    # You can duplicate that line to add mew models
    # admin.add_view(ModelView(YourModelName, db.session))