# Cleanup-hosts-redhat-satellite

This module could be used to dissociate and delete Linux servers from redhat satellite server.

Requirement - Redhat Satellite access ( username and password )

1) clone the repo
    git clone https://github.com/Venuvgp19/Cleanup-hosts-redhat-satellite.git

2) Navigate to the directory
      
       cd Cleanup-hosts-redhat-satellite

Note - if the server has any kind of duplicate entries of different domain it should also be deleted from satellite. Hence define fqdns in the below location in the code. Also enter the satellite server FQDN within the program.
        
    self.sat_server = ""  #Satellite server FQDN goes here (constructor)
        
    FQDN1 = svr[0]+'.example1.com'
    FQDN2 = svr[0]+'.example2.com'
    FQDN3 = svr[0]+'.example3.com'

3) Execute the code using command python delete_hosts.py <server_to_be_deleted>
            
	    (base) [root@server Cleanup-hosts-redhat-satellite]# python delete_hosts.py abcd
	    Username : "migration"
	    Password :
            WARNING!!! - Host Not found : abcd.supervalu.com
 	    "Resource host not found by id 'abcd.supervalu.com'"
       

            (base) [root@server Cleanup-hosts-redhat-satellite]# python delete_hosts.py serv
            Username :"migration"
            Password : **********
            Deleting server subscriptions : serv.example1.com
            Disassociating Client Host : serv.example1.com
            Deleting the host from Satellite server : serv.example1.com

