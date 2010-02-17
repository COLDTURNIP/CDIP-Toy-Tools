#!/usr/bin/python
# -*- coding: utf-8 -*-

import telnetlib

DEBUG = True

if DEBUG == True:
    def printlog(str):
        print ' [DBG]', str
        return

else:
    def printlog(str):
        pass

if __name__ == '__main__':
    print '''
        ****************************
        *  COLDTURNIP's BBS Mover  *
        ****************************
    '''
    if DEBUG:
        printlog('DEBUG = True')

    print 'Moving finished.'

