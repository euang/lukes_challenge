# mail_owner (default: postfix)

The UNIX system account that owns the Postfix queue and most Postfix
daemon processes. Specify the name of an unprivileged user account
that does not share a user or group ID with other accounts, and that
owns no other files
or processes on the system. In particular, don't specify nobody
or daemon. PLEASE USE A DEDICATED USER ID AND GROUP ID.




When this parameter value is changed you need to re-run "**postfix
set-permissions**" (with Postfix version 2.0 and earlier:
"**/etc/postfix/post-install set-permissions**".



