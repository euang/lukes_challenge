# mail_spool_directory (default: see "postconf -d" output)

The directory where local(8) UNIX-style mailboxes are kept. The
default setting depends on the system type. Specify a name ending
in / for maildir-style delivery.




Note: maildir delivery is done with the privileges of the recipient.
If you use the mail\_spool\_directory setting for maildir style
delivery, then you must create the top-level maildir directory in
advance. Postfix will not create it.




Examples:




```

mail\_spool\_directory = /var/mail
mail\_spool\_directory = /var/spool/mail

```

