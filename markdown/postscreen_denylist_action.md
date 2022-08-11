# postscreen_denylist_action (default: ignore)
 The action that postscreen(8) takes when a remote SMTP client is
permanently denylisted with the postscreen\_access\_list parameter.
Specify one of the following: 



 **ignore** (default) 
 Ignore this result. Allow other tests to complete. Repeat
this test the next time the client connects.
This option is useful for testing and collecting statistics
without blocking mail. 
 **enforce** 
 Allow other tests to complete. Reject attempts to deliver mail
with a 550 SMTP reply, and log the helo/sender/recipient information.
Repeat this test the next time the client connects. 
 **drop** 
 Drop the connection immediately with a 521 SMTP reply. Repeat
this test the next time the client connects. 

 This feature is available in Postfix 3.6 and later. 


 Available as postscreen\_blacklist\_action in Postfix 2.8 - 3.5. 


