# postscreen_non_smtp_command_action (default: drop)
 The action that postscreen(8) takes when a remote SMTP client sends
non-SMTP commands as specified with the postscreen\_forbidden\_commands
parameter. Specify one of the following: 



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
this test the next time the client connects. This action is the
same as with the Postfix SMTP server's smtpd\_forbidden\_commands
feature. 

 This feature is available in Postfix 2.8. 


