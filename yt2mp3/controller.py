import cmd

class Command(object):
    """
    Superclass for commands.
    """
    def __init__(self, arg):
        super(Command, self).__init__()
        print self
        self.arg = arg
        
        self.config = config.Config()