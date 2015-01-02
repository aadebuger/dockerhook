'''
Created on Jan 2, 2015

@author: aadebuger
'''
from docker import Client
import json
def processEvent(cli,eventstr):
    event = json.loads(eventstr)
    print 'id=',event['id']
    print 'status=',event['status']
    info = cli.inspect_container(event['id'])
    print 'info=',info
    print 'name=',info['name']
    print 'HostConfig=',info['HostConfig']
    
def events():
    cli = Client(base_url='tcp://127.0.0.1:4243')
    eventiter = cli.events()
    
    while 1:
            event = eventiter.next()
            print 'event',event
            processEvent(cli,event)
        
if __name__ == '__main__':
    events();