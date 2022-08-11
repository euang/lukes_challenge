# service_name (read-only)
 The master.cf service name of a Postfix daemon process. This
can be used to distinguish the logging from different services that
use the same program name. 


 Example master.cf entries: 



```

# Distinguish inbound MTA logging from submission and smtps logging.
smtp      inet  n       -       n       -       -       smtpd
submission inet n       -       n       -       -       smtpd
    -o syslog\_name=postfix/$service\_name
smtps     inet  n       -       n       -       -       smtpd
    -o syslog\_name=postfix/$service\_name

```


```

# Distinguish outbound MTA logging from inbound relay logging.
smtp      unix  -       -       n       -       -       smtp
relay     unix  -       -       n       -       -       smtp
    -o syslog\_name=postfix/$service\_name

```

