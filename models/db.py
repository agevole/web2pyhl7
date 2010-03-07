# coding: utf8

#########################################################################
## This scaffolding model makes your app work on Google App Engine too
#########################################################################

if request.env.web2py_runtime_gae:            # if running on Google App Engine
    db = DAL('gae')                           # connect to Google BigTable
    session.connect(request, response, db=db) # and store sessions and tickets there
    ### or use the following lines to store sessions in Memcache
    # from gluon.contrib.memdb import MEMDB
    # from google.appengine.api.memcache import Client
    # session.connect(request, response, db=MEMDB(Client())
else:                                         # else use a normal relational database
    db = DAL('sqlite://storage.sqlite')      # if not, use SQLite or other DB
    # if no need for session
    # session.forget()
    #dh = DAL("mysql://root@localhost/disease")  # if not, use MYSQL or other DB
    #session.connect(request, response, db=dh)  # and store sessions there
    # or use the following lines to store sessions in Memcache
    #from gluon.contrib.memdb import MEMDB
    #from google.appengine.api.memcache import Client
    #session.connect(request, response, db=MEMDB(Client()))
    



#########################################################################
## Here is sample code if you need for 
## - email capabilities
## - authentication (registration, login, logout, ... )
## - authorization (role based authorization)
## - services (xml, csv, json, xmlrpc, jsonrpc, amf, rss)
## - crud actions
## comment/uncomment as needed
import time; now=time.time()
from gluon.tools import *
from gluon.tools import Auth
from uuid import uuid4
auth=Auth(globals(),db)   # authentication/authorization

#################################################################
#from gluon.tools import Recaptcha 
#auth.settings.captcha = Recaptcha(request,'PUBLIC_KEY', 'PRIVATE_KEY')
#from gluon.contrib.login_methods.email_auth import email_auth 
#auth.settings.login_methods.append(email_auth("smtp.bizmail.yahoo.com:995", "@hcass.org"))
auth.settings.hmac_key='0d8d755a-646b-4499-821a-9be99e832e6f'


auth.settings.table_user = db.define_table(
    auth.settings.table_user_name,
    Field('first_name', length=512,default=''),
    Field('last_name', length=512,default=''),
    Field('email', length=512,default='',
          requires = [IS_EMAIL(),
                      IS_NOT_IN_DB(db,'auth_user.email')]),
    Field('password', 'password', readable=False,
          label='Password', requires=CRYPT(auth.settings.hmac_key)),
    Field('status',requires=IS_IN_SET(('Doctor','Nurse','Administrator'),zero=None)),
    Field('phone_number_home',default=''),
    Field('phone_number_office',default=''),
    Field('phone_number_cell',default=''),
    Field('address'),    
    Field('office_address'),
    Field('other_contact_info','text'),
    Field('preferred_contact',requires=IS_IN_SET(('email','phone call','sms'),zero=None)),
    Field('web_site_url',requires=IS_NULL_OR(IS_URL())),
    Field('specializations'),
    Field('affiliations'),
    Field('education','text'),
    Field('other_info','text'),
    Field('picture','upload'),
    Field('last_login',default=request.now,readable=False,writable=False),
    Field('last_notification',default=request.now,readable=False,writable=False),
    Field('registration_key', length=512,
          writable=False, readable=False,default=''),
    Field('reset_password_key', length=512,
          writable=False, readable=False, default='',
          label=auth.messages.label_reset_password_key),
    format='%(status)s %(first_name)s %(last_name)s'
    )


auth.define_tables()                         # creates all needed tables
crud=Crud(globals(),db)                      # for CRUD helpers using auth
service=Service(globals())                   # for json, xml, jsonrpc, xmlrpc, amfrpc
if auth.is_logged_in():
 user_id = auth.user .id
else:
 user_id = None

mail=Mail()
mail.settings.server = 'localhost:25'
mail.settings.sender = 'mdipierro@cs.depaul.edu'
mail.settings.login = None
auth.settings.mailer=mail
auth.settings.registration_requires_verification = True
auth.messages.verify_email = 'Click on the link http://web2py.com'+URL(r=request,c='default',f='user',args=['verify_email'])+'/%(key)s to verify your email' 
auth.settings.reset_password_requires_verification = True
auth.messages.reset_password = 'Click on the link http://web2py.com'+URL(r=request,c='default',f='user',args=['reset_password'])+'/%(key)s to reset your password'
