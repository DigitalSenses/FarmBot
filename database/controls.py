from database.models import User
from database.db import db_session

def get_user(name):
    return db_session.query(User).filter_by(Name=name).first()

def get_user_by_username(username):
    return db_session.query(User).filter_by(Username=username).first()

def AddUser(username, name, permission, role):
    try:
        if db_session.query(User).filter_by(Username=username).first() is None:

            user = User(username, name, permission, role)

            db_session.add(user)
            db_session.commit()

            message = ('User Added : "%s"' % (user))
        else:
            raise(Exception("User already exists"))
    except Exception as e:
        message = ("Error Adding User : %s" % (e))
    return message

def RemoveUser(username):
    try:
        user = get_user_by_username(username)

        db_session.delete(user)

        db_session.commit()

        message = "User Removed"
    except Exception as e:
        message = ("Error Removing User : %s" % (e))
    return message

def ChangeName(username, name):
    try:
        user = get_user_by_username(username)

        user.Name = name

        db_session.commit()

        message = ('User Name Changed : "%s"' % (user.Name))
    except Exception as e:
        message = ("Error Changing Username : %s" % (e))
    return message

def ChangeSpecies(name, species):
    try:
        user = get_user(name)

        user.Species = species

        db_session.commit()
        message = ('User species Changed : "%s"' % (user.Species))
    except Exception as e:
        message = ("Error Changing species : %s" % (e))
    return message

def ChangeBodyType(name, bodyType):
    try:
        user = get_user(name)

        user.Body_Type = bodyType

        db_session.commit()
        message = ('User Body Type Changed : "%s"' % (user.Body_Type))
    except Exception as e:
        message = ("Error Changing body type : %s" % (e))
    return message

def AddHeight(name, height):
    user = get_user(name)

    print(user)

    user.Height = user.Height + height

    db_session.commit()
def SubHeight(name, height):
    user = get_user(name)

    user.Height = user.Height - height

    db_session.commit()
def ChangeHeight(name, height):
    user = get_user(name)

    user.Height = height

    db_session.commit()

def AddWeight(name, weight):
    user = get_user(name)

    user.Weight = user.Weight + weight

    db_session.commit()
def SubWeight(name, weight):
    user = get_user(name)

    user.Weight = user.Weight - weight

    db_session.commit()
def ChangeWeight(name, weight):
    user = get_user(name)

    user.Weight = weight

    db_session.commit()

def ChangeCockType(name, cockType):
    user = get_user(name)

    user.Cock_Type = cockType

    db_session.commit()

def AddCockNumber(name, cockNumber):
    user = get_user(name)

    user.Cock_Number = user.Cock_Number + cockNumber

    db_session.commit()
def SubCockNumber(name, cockNumber):
    user = get_user(name)

    user.Cock_Number = user.Cock_Number - cockNumber

    db_session.commit()
def ChangeCockNumber(name, cockNumber):
    user = get_user(name)

    user.Cock_Number = cockNumber

    db_session.commit()

def AddCockSizeLength(name, cockSizeLength):
    user = get_user(name)

    user.Cock_Size_Length = user.Cock_Size_Length + cockSizeLength

    db_session.commit()
def SubCockSizeLength(name, cockSizeLength):
    user = get_user(name)

    user.Cock_Size_Length = user.Cock_Size_Length - cockSizeLength

    db_session.commit()
def ChangeCockSizeLength(name, cockSizeLength):
    user = get_user(name)

    user.Cock_Size_Length = cockSizeLength

    db_session.commit()

def AddCockSizeThickness(name, cockSizeThickness):
    user = get_user(name)

    user.Cock_Size_Thickness = user.Cock_Size_Thickness + cockSizeThickness

    db_session.commit()
def SubCockSizeThickness(name, cockSizeThickness):
    user = get_user(name)

    user.Cock_Size_Thickness = user.Cock_Size_Thickness - cockSizeThickness

    db_session.commit()
def ChangeCockSizeThickness(name, cockSizeThickness):
    user = get_user(name)

    user.Cock_Size_Thickness = cockSizeThickness

    db_session.commit()

def AddBallNumber(name, numberOfBalls):
    user = get_user(name)

    user.Ball_Number = user.Ball_Number + numberOfBalls

    db_session.commit()
def SubBallNumber(name, numberOfBalls):
    user = get_user(name)

    user.Ball_Number = user.Ball_Number - numberOfBalls

    db_session.commit()
def ChangeBallNumber(name, numberOfBalls):
    user = get_user(name)

    user.Ball_Number = numberOfBalls

    db_session.commit()

def AddBallSize(name, ballSize):
    user = get_user(name)

    user.Ball_Size = user.Ball_Size + ballSize

    db_session.commit()
def SubBallSize(name, ballSize):
    user = get_user(name)

    user.Ball_Size = user.Ball_Size - ballSize

    db_session.commit()
def ChangeBallSize(name, ballSize):
    user = get_user(name)

    user.Ball_Size = ballSize

    db_session.commit()

def ChangePosition(name, position):
    user = get_user(name)

    user.Position = position

    db_session.commit()

def ChangeRole(name, role):
    user = get_user(name)

    user.Role = role

    db_session.commit()