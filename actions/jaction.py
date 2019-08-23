import sys

from st2common.runners.base_action import Action

class J1Action(Action):
    def run(self, message):
        print(message)

        if message == 'working':
            return (True, message)
        return (False, message)
