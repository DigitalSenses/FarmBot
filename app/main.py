import telepot
import time
from database import controls
from database.db import db_session
import random

UserID = ''

def handle(msg):
    print('')
    print('Incomming message')

    message = extract(msg)

    for key, value in message.items():
        print(key, value)

    global UserID
    UserID = message['UserID']

    if message['Text'].lower() == '/start':
        print('/start')
        bot_cmd_start(message)

    if message['Text'].startswith('/user'):
        print('/user')
        arguments = message['Text'].replace('/user ', '')
        arguments = arguments.split(' ')
        bot_cmd_user(arguments)

    if message['Text'].startswith('/change'):
        print('/change')
        arguments = message['Text'].replace('/change ', '')
        arguments = arguments.split(' ')
        bot_cmd_change(arguments)

    if message['Text'].startswith('/help'):
        print('/help')
        bot_cmd_help()

    if message['Text'].startswith('/list_commands'):
        print('/list_commands')
        bot_cmd_list_commands()

    if message['Text'].startswith('/roll'):
        print('/roll')
        arguments = message['Text'].replace('/roll ', '')
        arguments = arguments.split(' ')
        bot_cmd_roll(arguments)

    UserID = ''

def extract(msg):
    print(msg)

    message = {}
    message['UserID']    = msg['chat']['id']
    message['Username']  = msg['from']['username']
    message['FirstName'] = msg['from']['first_name']
    message['Text']      = msg['text'].lower()
    message['Date']      = msg['date']

    return message

def bot_send_message(message):
    print('Sending message : "%s"' % (message))

    global UserID
    bot.sendMessage(UserID, "%s" % message)

def bot_cmd_start(message):
    print('Confirm Start')

    bot.sendMessage(message['UserID'], 'Welcome to the farm %s. If you need help, use the command /help' % message['FirstName'])

def bot_cmd_user(args):
    print('Confirm User')

    if   args[0].lower() == 'add':
        print("add")
        del args[0]

        if len(args) != 4:
            print(args)
            bot_send_message('Incorrect Arguments - Command Format "/user add {Username} {Name} {Permission} {Role}"')
            raise(Exception('Incorrect Arguments'))

        print(args)
        result = controls.AddUser(args[0], args[1], args[2], args[3])
        bot_send_message(result)
    elif args[0].lower() == 'remove':
        print('remove')

        result = controls.RemoveUser(args[1])
        bot_send_message(result)

def bot_cmd_change(args):
    print('Confirm Change')

    if   args[0].lower() == 'name':
        result = controls.ChangeName(args[1], args[2])
        bot_send_message(result)
    elif args[0].lower() == 'species':
        result = controls.ChangeSpecies(args[1], args[2])
        bot_send_message(result)
    elif args[0].lower() == 'bodytype':
        result = controls.ChangeBodyType(args[1], args[2])
        bot_send_message(result)
    elif args[0].lower() == 'height':
        if args[1] == '+':
            controls.AddHeight(args[2], int(args[3]))
        elif args[1] == '-':
            controls.SubHeight(args[2], int(args[3]))
        elif isinstance(args[1], str):
            controls.ChangeHeight(args[1], int(args[2]))
    elif args[0].lower() == 'weight':
        if args[1] == '+':
            controls.AddWeight(args[2], args[3])
        elif args[1] == '-':
            controls.SubWeight(args[2], args[3])
        elif isinstance(args[2], str):
            controls.ChangeWeight(args[1], args[2])
    elif args[0].lower() == 'cocktype':
        controls.ChangeCockType(args[1], args[2])
    elif args[0].lower() == 'numberofcocks':
        if args[1] == '+':
            controls.AddCockNumber(args[1], args[3])
        elif args[1] == '-':
            controls.SubCockNumber(args[1], args[3])
        elif isinstance(args[1], str):
            controls.ChangeCockNumber(args[1], args[2])
    elif args[0].lower() == 'cocksizelength':
        if args[1] == '+':
            controls.AddCockSizeLength(args[1], args[3])
        elif args[1] == '-':
            controls.SubCockSizeLength(args[1], args[3])
        elif isinstance(args[1], str):
            controls.ChangeCockSizeLength(args[1], args[2])
    elif args[0].lower() == 'cocksizethickness':
        if args[1] == '+':
            controls.AddCockSizeThickness(args[1], args[3])
        elif args[1] == '-':
            controls.SubCockSizeThickness(args[1], args[3])
        elif isinstance(args[1], str):
            controls.ChangeCockSizeThickness(args[1], args[2])
    elif args[0].lower() == 'numberofballs':
        if args[1] == '+':
            controls.AddBallNumber(args[1], args[3])
        elif args[1] == '-':
            controls.SubBallNumber(args[1], args[3])
        elif isinstance(args[1], str):
            controls.ChangeBallNumber(args[1], args[2])
    elif args[0].lower() == 'ballsize':
        if args[1] == '+':
            controls.AddBallSize(args[1], args[3])
        elif args[1] == '-':
            controls.SubBallSize(args[1], args[3])
        elif isinstance(args[1], str):
            controls.ChangeBallSize(args[1], args[2])
    elif args[0].lower() == 'position':
        controls.ChangePosition(args[1], args[2])
    elif args[0].lower() == 'role':
        controls.ChangeRole(args[1], args[2])

    db_session.close()

def bot_cmd_roll(args):
    min_value = args[0]
    max_value = args[1]

    if min_value > max_value:
        a = min_value
        b = max_value

        min_value = b
        max_value = a

    r = random.randint(int(min_value), int(max_value))

    r = str(r)
    bot_send_message(r)

def bot_cmd_list_commands():
    bot_send_message('Command List \n\n/start\n\n/user add {Username} {Name} {Permission} {Role}\n\n/user remove {Username}\n\n/change name {Username} {Name}\n\n/change species {Name} {Species}\n\n/change bodytype {Name} {BodyType}\n\n/change height {Name} -{HeightToSubtract}\n/change height {Name} +{HeightToAdd}\n/change height {Name} {Height}\n\n/change weight {Name} -{WeightToSubtract}\n/change weight {Name} +{WeightToAdd}\n/change weight {Name} {Weight}\n\n/change cocktype {Name} cocktype\n\n/change numberofcocks {Name} -{CocksToSubtract}\n/change numberofcocks {Name} +{CocksToAdd}\n/change numberofcocks {Name} {Cocks}\n\n/change cocksizelength {Name} -{CockLengthToSubtract}\n/change cocksizelength {Name} +{CockLengthToAdd}\n/change cocksizelength {Name} {CockLength}\n\n/change cocksizethickness {Name} -{CockThicknessToSubtract}\n/change cocksizethickness {Name} +{CockThicknessToAdd}\n/change cocksizethickness {Name} {CockThickness}\n\n/change numberofballs {Name} -{NumberOfBallsToSubtract}\n/change numberofballs {Name} +{NumberOfBallsToAdd}\n/change numberofballs {Name} {NumberOfBalls}\n\n/change ballsize {Name} -{BallSizeToSubtract}\n/change ballsize {Name} +{BallSizeToAdd}\n/change ballsize {Name} {BallSize}\n\n/change position {Name} {position}\n\n/change role {Name} {role}')

def bot_cmd_help():
    bot_send_message('You must use commands to interact with this bot. Use /list_commands to get a full list.')

# Create a bot object with API key
bot = telepot.Bot('379955406:AAHhnAdnFJnLk0v5hVGLYMl6t9Rg9cj1PIw')

# Attach a function to notifyOnMessage call back
bot.message_loop(handle)

# Listen to the messages
while 1:
    time.sleep(10)
    #TODO Return list of all users
    #TODO Setup permissions