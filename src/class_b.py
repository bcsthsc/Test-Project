'''
Created on Jan 21, 2012

@author: thos
'''

class B(object):
    '''
    classdocs
    '''

    
    def __init__(self):
        '''
        Constructor
        '''
        print "Initialized B object"
        self.__status = None

    def getStatus(self):
        return self.__status