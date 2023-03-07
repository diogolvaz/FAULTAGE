#
#   This file represents the SEND() action

##################################################################################################################################
#
#   IMPORTS
#
##################################################################################################################################

#
from services.ActionsSpace.Actions.Logic.Send import SEND
#
import inputs.GenerationInputs as GenerationInputs
import utils.GlobalVariables.TextVariables as Vars

##################################################################################################################################
#
#   CLASS
#
##################################################################################################################################


class SEND_M(SEND):

    ##################################################################################################################################
    #
    #   VARIABLES
    #
    ##################################################################################################################################

    ##################################################################################################################################
    #
    #   CONSTRUCTOR
    #
    ##################################################################################################################################

    def __init__(self, type):
        super().__init__(Vars.SEND_MYSELF, type, "SEND to myself",
                         GenerationInputs.getLogicReward(Vars.SEND_MYSELF))

    ##################################################################################################################################
    #
    #   GET
    #
    ##################################################################################################################################

    def getNumberOfSends(self, N):
        return 1

    ##################################################################################################################################
    #
    #   LOGIC
    #
    ##################################################################################################################################

    def __eq__(self, logic):
        return super().__eq__(logic) and (type(logic) is SEND_M)
