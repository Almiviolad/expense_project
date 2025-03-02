import cmd, sys
import models
from models import storage
from models.base import BaseCls
from models.user import User
from models.expense import Expense



classes = {'User': User, 'Expense': Expense}
class Cli(cmd.Cmd):
    """command line interpreter to easily operations with models"""
    def __init__(self, completekey = "tab", stdin = None, stdout = None):
        super().__init__(completekey, stdin, stdout)
    intro = 'Welcome to expensetrack console'
    prompt = '<trackxpense>'
    

    def do_EOF(self, arg):
        """exits the console"""
        return True
    
    def do_quit(self, arg):
        """Also exits the console"""
        return True
    
    def _kv_parser(self, args):
        """create anew dict fromyhelist of string on cli"""
        new_dict ={}
        for arg in args:
            if '=' in arg:
                kv = arg.split('=')
                key = kv[0]
                value =kv[1]
                if value[0] == value[-1] == '"' or "'":
                    value = value.strip('"\'').replace('_', ' ')
                    new_dict[key] = value
                else:
                    try:
                        new_dict[key] =int(value)
                    except:
                        try:
                            new_dict[key] = float(key)
                        except:
                            continue
        return new_dict

    def do_create(self, arg):
        """creates a new model"""
        args = arg.split()
        if len(args) < 1:
            print('???class name  missing???')
            return False
        
        cls = args[0]
        if cls in classes:
            if len(args) < 2:
                print('You did not add {} details'.format(cls) )
                return False
            new_dict = self._kv_parser(args[1:])
            print(new_dict, cls)
            ins = classes[cls](**new_dict)
            ins.save()
            print('{} created successfully'.format(ins.id ))
        else:    
            print('???Class does not exist???')
            return False
        
    
    def do_all(self, arg):
        """return all instance of a class or all instances"""
        print(storage.all(arg))
        return False
    
    def do_delete(self, arg):
        """delete an instance"""
        storage.delete(arg)
if __name__ == '__main__':
    Cli().cmdloop()