# postscreen_greet_action (default: ignore)
The action that postscreen(8) takes when a remote SMTP client speaks
before its turn within the time specified with the postscreen\_greet\_wait
parameter. Specify one of the following: 



 **ignore** (default) 
 Ignore the failure of this test. Allow other tests to complete.
Repeat this test the next time the client connects.
This option is useful for testing and collecting statistics
without blocking mail. 
 **enforce** 
 Allow other tests to complete. Reject attempts to deliver mail
with a 550 SMTP reply, and log the helo/sender/recipient information.
Repeat this test the next time the client connects. 
 **drop** 
 Drop the connection immediately with a 521 SMTP reply. Repeat
this test the next time the client connects. 

 In either case, postscreen(8) will not allowlist the remote SMTP client
IP address. 


 This feature is available in Postfix 2.8. 


