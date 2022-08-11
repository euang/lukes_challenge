# postscreen_bare_newline_action (default: ignore)
 The action that postscreen(8) takes when a remote SMTP client sends
a bare newline character, that is, a newline not preceded by carriage
return. Specify one of the following: 



 **ignore** 
 Ignore the failure of this test. Allow other tests to complete.
Do *not* repeat this test before the result from some
other test expires.
This option is useful for testing and collecting statistics
without blocking mail permanently. 
 **enforce** 
 Allow other tests to complete. Reject attempts to deliver mail
with a 550 SMTP reply, and log the helo/sender/recipient information.
Repeat this test the next time the client connects. 
 **drop** 
 Drop the connection immediately with a 521 SMTP reply. Repeat
this test the next time the client connects. 

 This feature is available in Postfix 2.8. 


