from datetime import datetime
import time

class Performance_Check(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start_time = datetime.now()
        self.func(*args, **kwargs)
        end_time = datetime.now()
        time_delta = end_time - start_time
        print time_delta

@Performance_Check
def get_class_text(name):
    time.sleep(5)
    return "I am %s" % name

if __name__ == '__main__':
    print "Check the decorator : Performance using class decorators:"
    get_class_text('Varadarajan')
