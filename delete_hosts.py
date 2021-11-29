import os
import subprocess
import requests
import sys
import getpass

username = input('Username : ')
password = getpass.getpass(prompt='Password : ')

class Satellite:
    def __init__(self,servlist):
	self.servlist = servlist
	self.sat_server = "wppladm006.supervalu.com"
		
    def delete_host(self):
	if svr and len(self.servlist) == 3:
            for server in self.servlist:
	        Server_ID = os.popen('curl -s -u %s'%username + ':%s'%password + ' -L http://%s'%self.sat_server +'/api/v2/hosts/%s'%server + ' | json_reformat|grep -m20 \"id\"|grep -w id').read()
		integer = -1
		try :
                    ID = Server_ID.split(':')[1].split(',')[0]
		    integer = int(ID)
		except ValueError:
		    print("WARNING!!! - Host Not found : %s"%server)
		
	        str_int = str(integer)
		if integer > 0 :
		    #delete the host
		    print('Deleting server subscriptions : %s'%server)
		    os.popen('curl -X DELETE -s -k -u migration:%s'%password + ' -L https://%s'%self.sat_server +'/api/v2/hosts/%s'%str_int + '/subscriptions').read()
		    print('Disassociating Client Host : %s'%server)
		    os.popen('curl -X PUT -s -k -u migration:%s'%password + ' -L https://%s'%self.sat_server +'/api/v2/hosts/%s'%str_int + '/disassociate').read()
		    print('Deleting the host from Satellite server : %s'%server)
		    resp = os.popen('curl -X DELETE -s -k -u  migration:%s'%password + ' -L http://%s'%self.sat_server +'/api/v2/hosts/%s'%str_int + ' |json_reformat').read()
		    return resp
		else:
		    #print response
		    return ID

if __name__ == '__main__':
    svr = sys.argv[1:]
    if svr:
        FQDN1 = svr[0]+'.supervalu.com'
	FQDN2 = svr[0]+'.unfi.com'
	FQDN3 = svr[0]+'.albertsons.com'
	servlist = [FQDN1,FQDN2,FQDN3]
	S = Satellite(servlist)
	print(S.delete_host())

    else:
	print('please enter server name to delete from satellite : example - eplnx421')
	sys.exit(0)
