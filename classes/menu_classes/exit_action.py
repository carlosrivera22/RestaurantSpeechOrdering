from interfaces.menu_interfaces.abstract_action import AbstractAction
from ..data_manager.dm_component import DataManager

class ExitAction(AbstractAction):

    def execute(self,arg):
        dm = arg
        dm.get_menu_stack().pop()
    