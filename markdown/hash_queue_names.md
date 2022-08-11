# hash_queue_names (default: deferred, defer)

The names of queue directories that are split across multiple
subdirectory levels.



 Before Postfix version 2.2, the default list of hashed queues
was significantly larger. Claims about improvements in file system
technology suggest that hashing of the incoming and active queues
is no longer needed. Fewer hashed directories speed up the time
needed to restart Postfix. 



After changing the hash\_queue\_names or hash\_queue\_depth parameter,
execute the command "**postfix reload**".



