# All business logic associated with adding users, user login, registration, and display of user info etc should be handled here

from .models.UserModule import User
from . import DataBaseLayer
from datetime import datetime, timedelta
import datetime
import string
import random

class UserRegistry:
    active_user_list = []

    #use default values for all the fields excluding email and password
    def __init__(self):
        pass

    def sign_in(user_form):
        print("sign in!")
        return UserRegistry.authenticate(user_form.cleaned_data['email'], user_form.cleaned_data['password'])

    def authenticate(email=None, password=None):
        print("AUTH  CALLED")
        conn = DataBaseLayer.connectDb()
        sql_select = "SELECT * FROM User WHERE email = '" + email+ "' AND password = '" + password + "';"
        user = UserRegistry.formatUserTableObject(DataBaseLayer.selectCommand(conn, sql_select)[0])
  
        session_expire = (datetime.datetime.today()+timedelta(days=30))
        session_key = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
        sql_insert = "UPDATE user SET session_expire = '"+str(session_expire)+"',session_key = '"+session_key+"'  WHERE id = '" + "1"+"';"
        DataBaseLayer.insertCommand(conn, sql_insert)
        #need to get the user again after update
        user = UserRegistry.formatUserTableObject(DataBaseLayer.selectCommand(conn, sql_select)[0])
        print("$$$$")
        print(user)  
        return user

    #not ideal
    def formatUserTableObject(bad_user_format):
        f_user = {};
        f_user['id'] = bad_user_format[0];
        f_user['first_name'] = bad_user_format[1];
        f_user['last_name'] = bad_user_format[2];
        f_user['address'] = bad_user_format[3];
        f_user['phone_number'] = bad_user_format[4];
        f_user['is_admin'] = bad_user_format[5];
        f_user['password'] = bad_user_format[6];
        f_user['email'] = bad_user_format[7];
        f_user['session_expire'] = str(bad_user_format[8]);
        f_user['session_key'] = bad_user_format[9];
        return f_user


    def get_active_users():
        #session_key exists 
        #session_expire > today's date
        today = datetime.datetime.today()
        #return User.objects.filter(session_expire__range=[today, "3020-01-31"]).exclude(session_key="")
        print("today")
        print(today)
        sql = "SELECT * FROM user WHERE NOT session_key = '' AND session_expire >= '"+str(today)+"';"
        conn = DataBaseLayer.connectDb()
        bad_format_users = DataBaseLayer.selectCommand(conn, sql)
        users = []
        for bad_format_user in bad_format_users:
            users.append(UserRegistry.formatUserTableObject(bad_format_user))
        print("SUCCESS!")
        print(users)
        return users
