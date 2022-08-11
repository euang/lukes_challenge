# relay_destination_recipient_limit (default: $default_destination_recipient_limit)
 The maximal number of recipients per message for the relay
message delivery transport. This limit is enforced by the queue
manager. The message delivery transport name is the first field in
the entry in the master.cf file. 


 Setting this parameter to a value of 1 changes the meaning of
relay\_destination\_concurrency\_limit from concurrency per domain
into concurrency per recipient. 


 This feature is available in Postfix 2.0 and later. 


