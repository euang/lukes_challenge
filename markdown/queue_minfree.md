# queue_minfree (default: 0)

The minimal amount of free space in bytes in the queue file system
that is needed to receive mail. This is currently used by the
Postfix SMTP server to decide if it will accept any mail at all.




By default, the Postfix SMTP server rejects MAIL FROM commands when
the amount of free space is less than 1.5\*$message\_size\_limit
(Postfix version 2.1 and later).
To specify a higher minimum free space limit, specify a queue\_minfree
value that is at least 1.5\*$message\_size\_limit.




With Postfix versions 2.0 and earlier, a queue\_minfree value of
zero means there is no minimum required amount of free space.



