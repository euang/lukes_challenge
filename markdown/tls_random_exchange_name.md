# tls_random_exchange_name (default: see "postconf -d" output)
 Name of the pseudo random number generator (PRNG) state file
that is maintained by tlsmgr(8). The file is created when it does
not exist, and its length is fixed at 1024 bytes. 


 As of version 2.5, Postfix no longer uses root privileges when
opening this file, and the default file location was changed from
${config\_directory}/prng\_exch to ${data\_directory}/prng\_exch. As
a migration aid, an attempt to open the file under a non-Postfix
directory is redirected to the Postfix-owned data\_directory, and a
warning is logged. 


 This feature is available in Postfix 2.2 and later. 


