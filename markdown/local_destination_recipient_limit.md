# local_destination_recipient_limit (default: 1)
 The maximal number of recipients per message delivery via the
local mail delivery transport. This limit is enforced by the queue
manager. The message delivery transport name is the first field in
the entry in the master.cf file. 


 Setting this parameter to a value > 1 changes the meaning of
local\_destination\_concurrency\_limit from concurrency per recipient
into concurrency per domain. 


