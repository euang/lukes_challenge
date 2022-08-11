# mailbox_transport (default: empty)

Optional message delivery transport that the local(8) delivery
agent should use for mailbox delivery to all local recipients,
whether or not they are found in the UNIX passwd database.



 The precedence of local(8) delivery features from high to low
is: aliases, .forward files, mailbox\_transport\_maps, mailbox\_transport,
mailbox\_command\_maps, mailbox\_command, home\_mailbox, mail\_spool\_directory,
fallback\_transport\_maps, fallback\_transport and luser\_relay. 


