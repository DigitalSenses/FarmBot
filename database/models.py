from sqlalchemy import Column, Integer, String
from database.db import Base

class User(Base):
    __tablename__ = 'user'
    ID                  = Column(Integer()   , nullable=False, primary_key=True)
    Username            = Column(String(32)  , nullable=False, unique=True)
    Name                = Column(String(50)  , nullable=True)
    Species             = Column(String(50)  , nullable=True)
    Body_Type           = Column(String(50)  , nullable=True)
    Height              = Column(Integer()   , nullable=True)
    Weight              = Column(String(50)  , nullable=True)
    Cock_Type           = Column(String(50)  , nullable=True)
    Cock_Number         = Column(Integer()   , nullable=True)
    Cock_Size_Length    = Column(Integer()   , nullable=True)
    Cock_Size_Thickness = Column(Integer()   , nullable=True)
    Ball_Number         = Column(Integer()   , nullable=True)
    Ball_Size           = Column(Integer()   , nullable=True)
    #Dom_Sub             = Column(String(50)  , nullable=True)
    Position            = Column(String(50)  , nullable=True)
    #Owner               = Column(String(250) , nullable=True)
    #Pet                 = Column(String(250) , nullable=True)
    #Marking             = Column(String(1024), nullable=True)
    #Body_Modification   = Column(String(1024), nullable=True)
    Role                = Column(String(30)  , nullable=True)
    #Permission          = Column(String(20)  , nullable=False)

    def __init__(self, username, name, Permission, Role):
        self.Username   = username
        self.Name       = name
        self.Permission = Permission

    def __repr__(self):
        message = (
                'ID - "%s" \n'
                'Username - "%s" \n'
                'Name - "%s" \n'
                'Species - "%s" \n'
                'Body_Type - "%s" \n'
                'Height - "%s" \n'
                'Weight - "%s" \n'
                'Cock_Type - "%s" \n'
                'Cock_Number - "%s" \n'
                'Cock_Size_Length - "%s" \n'
                'Cock_Size_Thickness - "%s" \n'
                'Ball_Number - "%s" \n'
                'Ball_Size - "%s" \n'
                #'Dom_Sub - "%s" \n'
                'Position - "%s" \n'
                #'Owner - "%s" \n'
                #'Pet - "%s" \n'
                #'Marking - "%s" \n'
                #'Body_Modification - "%s" \n'
                'Role - "%s \n'
                #'Permission - "%s'

                % (
                    self.ID,
                    self.Username,
                    self.Name,
                    self.Species,
                    self.Body_Type,
                    self.Height,
                    self.Weight,
                    self.Cock_Type,
                    self.Cock_Number,
                    self.Cock_Size_Length,
                    self.Cock_Size_Thickness,
                    self.Ball_Number,
                    self.Ball_Size,
                    #self.Dom_Sub,
                    self.Position,
                    #self.Owner,
                    #self.Pet,
                    #self.Marking,
                    #self.Body_Modification,
                    self.Role,
                    #self.Permission
                   )
                )
        message = message.replace('None', '')
        message = message.replace('_', ' ')
        return message