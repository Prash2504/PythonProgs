# Class decorator using a wrapper function for decorator with arguments

class goToTabs(object):
    def __init__(self, **kwargs):
        if kwargs.pop("More", None):
            print "Click on More Tab"
        elif kwargs.pop("Rules", None):
            print "Click on Rules Tab"
        elif kwargs.pop("Devices", None):
            print "Click on Rules Tab"
        else:
            print "Invalid set of arguments."

    def __call__(self, f):
        def f_wrapper(*args):
            f(*args)
        return f_wrapper

@goToTabs(More="More")
def checkRemoteAccessEnabled():
    print("Write steps to check if remote access is enabled")

if __name__ == '__main__':
    print "Decorator with arguments:1"
    checkRemoteAccessEnabled()
