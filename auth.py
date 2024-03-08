from flask import Blueprint , render_template , request , flash
import re

auth = Blueprint('auth' , __name__)

@auth.route('/sign-up-parents' , methods=['GET','POST'])
def sign_up_parents():
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('name')
        password = request.form.get('password')
        id = request.form.get('ID') 
        if(check_email(email) == False):
            flash('Email must be as the regular format', category='error')

        elif(check_name(name) == False):
            flash('name must be longer than 3 chars , without numbers and speical chars', category='error')

        elif(check_pass(password) == False):
            flash('password must be longer than 7 chars without spaces, must contain at least one: [a-z],[A-Z],[0-9]' , category='error')
        
        elif(check_id(id) == False):
            flash("ID must be exactly 9 numbers , and only numbers!" , category='error')

        else:
            flash('Account created!' , category='success')
            

    return render_template("sign_up_parents.html")


def check_email(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    #check if the email is like the format that given above
    if (re.fullmatch(regex , email)):
        return True
    return False

def check_name(name):
    special_characters = "!@#$%^&*()-+?_=,<>/"
    #check if name length is bigger than 3 chars
    if len(name) > 3:
       #check if there some numbers in the name 
       if bool(re.search(r'\d', name)) == False:
           #check if there is some special chars in the name
           if not any(c in special_characters for c in name):
               return True
    return False

def check_pass(password):
    flag = True
    #check the length of the password
    if (len(password)<=8):
        flag = False
    #check if [a-z] in the password
    elif not re.search("[a-z]", password):
        flag = False
    #check if [A-Z] in the password
    elif not re.search("[A-Z]", password):
        flag = False
    #check if [0-9] in the password
    elif not re.search("[0-9]", password):
        flag = False
    elif re.search(" ", password):
        flag = False

    return flag
        


def check_id(id):
    flag = True
    special_characters = "!@#$%^&*()-+?_=,<>/"
    if len(id) != 9:
        flag = False
    elif re.search("[a-z]", id) and re.search("[A-Z]", id) and re.search(" ", id):
            flag = False

    return flag