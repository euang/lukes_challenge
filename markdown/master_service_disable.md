# master_service_disable (default: empty)
 Selectively disable master(8) listener ports by service type
or by service name and type. Specify a list of service types
("inet", "unix", "fifo", or "pass") or "name/type" tuples, where
"name" is the first field of a master.cf entry and "type" is a
service type. As with other Postfix matchlists, a search stops at
the first match. Specify "!pattern" to exclude a service from the
list. By default, all master(8) listener ports are enabled. 


 Note: this feature does not support "/file/name" or "type:table"
patterns, nor does it support wildcards such as "\*" or "all". This
is intentional. 


 Examples: 



```

# With Postfix 2.6..2.10 use '.' instead of '/'.
# Turn on all master(8) listener ports (the default).
master\_service\_disable =
# Turn off only the main SMTP listener port.
master\_service\_disable = smtp/inet
# Turn off all TCP/IP listener ports.
master\_service\_disable = inet
# Turn off all TCP/IP listener ports except "foo".
master\_service\_disable = !foo/inet, inet

```

 This feature is available in Postfix 2.6 and later. 


