from interfaces.menu_interfaces.abstract_action import AbstractAction
from classes.menu_classes.main_dishes_menu import MainDishesMenu
from ..data_manager.dm_component import DataManager

class MainDishesAction(AbstractAction):
    def execute(self,arg):
        dm = arg
        dm.get_menu_stack().push(MainDishesMenu())