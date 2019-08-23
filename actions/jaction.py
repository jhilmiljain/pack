import sys

from st2common.runners.base_action import Action

class MyJAction(Action):
    def run(self, message):
        if message == 'working':
            return (True, message)
        else:
            print("Wrong parameters")
