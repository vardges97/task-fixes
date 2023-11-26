import re

def validate_username(username):
    if len(username) < 5 or len(username) > 20:
        return False
    if not username.isalnum():
        return False
    reserved_names = ['admin', 'root','boss','chief']
    if username.lower() in reserved_names:
        return False
    return True

def validate_email(email):
    email_pattern = r'^[\w\.-]+@[\w\.-]+$'
    return re.match(email_pattern, email) is not None


def validate_phone(phone):
    phone_pattern = r'^(\+\d{12}|\d{9})$'
    return re.match(phone_pattern, phone) is not None

def validate_password(password):
    if len(password) < 8:
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char in ".!@#$%^&*" for char in password):
        return False
    return True

def validate_password_repeat(password, password_repeat):
    return password == password_repeat


def validate_username_decorator(func):
    def wrapper(*args, **kwargs):
        if not validate_username(args[0]):
            print("Invalid username")
            return
        return func(*args, **kwargs)
    return wrapper


def validate_email_decorator(func):
    def wrapper(*args, **kwargs):
        if not validate_email(args[1]):
            print("Invalid email")
            return
        return func(*args, **kwargs)
    return wrapper


def validate_phone_decorator(func):
    def wrapper(*args, **kwargs):
        if not validate_phone(args[2]):
            print("Invalid phone number")
            return
        return func(*args, **kwargs)
    return wrapper


def validate_password_decorator(func):
    def wrapper(*args, **kwargs):
        if not validate_password(args[3]):
            print("Invalid password. must contain at least one lowercase,uppercase,special char\n"
                  "one number and be at least 8 characters long")
            return
        return func(*args, **kwargs)
    return wrapper


def validate_password_repeat_decorator(func):
    def wrapper(*args, **kwargs):
        if not validate_password_repeat(args[3], args[4]):
            print("Passwords do not match")
            return
        return func(*args, **kwargs)
    return wrapper


@validate_username_decorator
@validate_email_decorator
@validate_phone_decorator
@validate_password_decorator
@validate_password_repeat_decorator
def register_user(username, email, phone, password, password_repeat):

    print("Registration successful!")


username1=input('Enter username: ')
email1=input('Enter email: ')
phone1=input('Enter phone number: ')
password1=input('Enter your password: ')
password_repeat1=input('Repeat your password: ')

register_user(username1,email1,phone1,password1,password_repeat1)