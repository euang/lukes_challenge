# known_tcp_ports (default: lmtp=24, smtp=25, smtps=submissions=465, submission=587)
 Optional setting that avoids lookups in the services(5) database.
This feature was implemented to address inconsistencies in the name
of the port "465" service. The ABNF is:




> 
> 
> known\_tcp\_ports = empty | name-to-port \*("," name-to-port)   
> 
> name-to-port = 1\*(service-name "=') port-number
> 
> 
> 
> 


 The comma is required. Whitespace is optional but it cannot appear
inside a service name or port number. 


 This feature is available in Postfix 3.6 and later. 


