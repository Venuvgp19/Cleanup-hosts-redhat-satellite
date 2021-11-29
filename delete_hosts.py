import os
import subprocess
import requests
import sys
import getpass

#collect username and password from end user

username = input('Username : ')
password = getpass.getpass(prompt='Password : ')


class Satellite:
    def __init__(self,servlist):
	self.servlist = servlist #constructor
	self.sat_server = ""  #Satellite server FQDN goes here (constructor)
		
    def delete_host(self): #method of class Satellite
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
		    return ID

if __name__ == '__main__':
    svr = sys.argv[1:]
    if svr:
        FQDN1 = svr[0]+'.example1.com'
	FQDN2 = svr[0]+'.example2.com'
	FQDN3 = svr[0]+'.example3.com'
	servlist = [FQDN1,FQDN2,FQDN3]
	S = Satellite(servlist)
	print(S.delete_host())

    else:
	print('please enter server name to delete from satellite : example - <server_name>')
	sys.exit(0)
