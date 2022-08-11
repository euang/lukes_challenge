# smtp_destination_concurrency_limit (default: $default_destination_concurrency_limit)
 The maximal number of parallel deliveries to the same destination
via the smtp message delivery transport. This limit is enforced by
the queue manager. The message delivery transport name is the first
field in the entry in the master.cf file. 


