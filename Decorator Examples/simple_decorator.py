from datetime import datetime
import time

# Simple performance effeciency check

def perfcheck(func):
    def func_wrapper(name):
        start_time = datetime.now()
        func(name)
        end_time = datetime.now()
        time_delta = end_time - start_time
        print time_delta
    return func_wrapper

@perfcheck
def get_text(name):
    time.sleep(5)
    return "I am %s" % name

if __name__ == '__main__':
        print "Check the decorator : Performance using function decorators:"
        get_text('Varadarajan')
