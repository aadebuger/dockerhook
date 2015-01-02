'''
Created on Jan 2, 2015

@author: aadebuger
'''
from docker import Client

def events():
    cli = Client(base_url='tcp://127.0.0.1:4243')
    eventiter = cli.events
    for event in eventiter:
        print 'event',event
        
if __name__ == '__main__':
    events();