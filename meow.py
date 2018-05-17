from boa.blockchain.vm.Neo.Runtime import Notify, GetTrigger, CheckWitness
from boa.blockchain.vm.Neo.Action import RegisterAction
from boa.blockchain.vm.Neo.TriggerType import Application, Verification

from boa.blockchain.vm.Neo.TransactionType import InvocationTransaction
from boa.blockchain.vm.Neo.Transaction import *

from boa.blockchain.vm.System.ExecutionEngine import GetScriptContainer, GetExecutingScriptHash
from boa.blockchain.vm.Neo.TriggerType import Application, Verification
from boa.blockchain.vm.Neo.Output import GetScriptHash, GetValue, GetAssetId
from boa.blockchain.vm.Neo.Storage import GetContext, Get, Put, Delete






def Main():
    OWNER = b'027e63b2a9efc22e36bca7303337f4c6e0c0728e8bb28de37e7f12bb785515e9e3'

    result = CheckWitness(OWNER)

    if result:
        print("Access Granted")
        return True

    return False

