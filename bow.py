from boa.interop.Neo.Runtime import GetTrigger, CheckWitness

from boa.interop.Neo.TriggerType import Application, Verification

def Main(password):

    trigger = GetTrigger()

    if trigger == Verification:
        return handleVerification()

    elif trigger == Application:
        return handleApplication(password)

    return False

def handleVerification():

    owner = 'AK2nJJpJr6o664CWJKi1QRXjqeic2zRp8y'

    is_owner = CheckWitness(owner)

    if is_owner:
        return True

    return False

def handleApplication(password):

    if password == 'shadow':
        return 'ACCESS_GRANTED'

    return 'ACCESS_DENIED'



