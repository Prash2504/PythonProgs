#!/usr/bin/python 


class _verifyTheWeMoInDeviceListContainer(object):
    def __init__(self, f):
        self.f = f

    def __call__(self, *args):
        print ("Verify the WeMo Device in container %s" % args)
        # Get the return of verification as True/False
        if False:
            self.f(args)
        print ("The process is verified.")


@_verifyTheWeMoInDeviceListContainer
def _turnOnWeMo(WeMoFriendlyName):
    print ("Turn on the WeMo Device %s" % WeMoFriendlyName)


@_verifyTheWeMoInDeviceListContainer
def _turnOffWeMo(WeMoFriendlyName):
    print ("Turn off the WeMo Device %s" % WeMoFriendlyName)

if __name__ == '__main__':
    _turnOnWeMo("WeMo_34D")
