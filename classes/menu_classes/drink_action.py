from interfaces.menu_interfaces.abstract_action import AbstractAction
from ..data_manager.dm_component import DataManager
from classes.menu_classes.drink_menu import DrinkMenu

class DrinkAction(AbstractAction):

    def execute(self,arg):
        dm = arg
        dm.get_menu_stack().push(DrinkMenu())
