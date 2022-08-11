# smtp_sasl_password_maps (default: empty)

Optional Postfix SMTP client lookup tables with one username:password
entry per sender, remote hostname or next-hop domain. Per-sender
lookup is done only when sender-dependent authentication is enabled.
If no username:password entry is found, then the Postfix SMTP client
will not attempt to authenticate to the remote host.




The Postfix SMTP client opens the lookup table before going to
chroot jail, so you can leave the password file in /etc/postfix.




Specify zero or more "type:name" lookup tables, separated by
whitespace or comma. Tables will be searched in the specified order
until a match is found.



