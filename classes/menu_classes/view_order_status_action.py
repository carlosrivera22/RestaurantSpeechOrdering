from interfaces.menu_interfaces.abstract_action import AbstractAction
class ViewOrderStatusAction(AbstractAction):

    def execute(self,arg):
        dm = arg
        dm.display_order()
