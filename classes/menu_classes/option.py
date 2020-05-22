class Option:

    def __init__(self,description,action):
        self.description = description
        self.action = action

    def get_description(self):
        return self.description

    def get_action(self):
        return self.action
    
    