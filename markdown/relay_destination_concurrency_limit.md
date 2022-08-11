# relay_destination_concurrency_limit (default: $default_destination_concurrency_limit)
 The maximal number of parallel deliveries to the same destination
via the relay message delivery transport. This limit is enforced
by the queue manager. The message delivery transport name is the
first field in the entry in the master.cf file. 


 This feature is available in Postfix 2.0 and later. 


