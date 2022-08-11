# milter_default_action (default: tempfail)
 The default action when a Milter (mail filter) response is
unavailable (for example, bad Postfix configuration or Milter
failure). Specify one of the following: 



accept Proceed as if the mail filter was not present.

reject Reject all further commands in this session
with a permanent status code.
tempfail Reject all further commands in this session
with a temporary status code. 
quarantine Like "accept", but freeze the message in
the "hold" queue. Available with Postfix 2.6 and later. 

 This feature is available in Postfix 2.3 and later. 


