from interfaces.menu_interfaces.abstract_action import AbstractAction
from ..data_manager.dm_component import DataManager

class SubmitAction(AbstractAction):

    def execute(self,arg):
        dm = arg
        print("Your order is:")
        dm.display_order()
        print("Thanks for submitting your order!")
        while not dm.get_menu_stack().isEmpty():
            dm.get_menu_stack().pop()
        