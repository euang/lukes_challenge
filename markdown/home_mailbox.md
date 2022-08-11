# home_mailbox (default: empty)

Optional pathname of a mailbox file relative to a local(8) user's
home directory.




Specify a pathname ending in "/" for qmail-style delivery.



 The precedence of local(8) delivery features from high to low
is: aliases, .forward files, mailbox\_transport\_maps, mailbox\_transport,
mailbox\_command\_maps, mailbox\_command, home\_mailbox, mail\_spool\_directory,
fallback\_transport\_maps, fallback\_transport and luser\_relay. 



Examples:




```

home\_mailbox = Mailbox
home\_mailbox = Maildir/

```

