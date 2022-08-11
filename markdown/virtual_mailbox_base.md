# virtual_mailbox_base (default: empty)

A prefix that the virtual(8) delivery agent prepends to all pathname
results from $virtual\_mailbox\_maps table lookups. This is a safety
measure to ensure that an out of control map doesn't litter the
file system with mailboxes. While virtual\_mailbox\_base could be
set to "/", this setting isn't recommended.



 This parameter is specific to the virtual(8) delivery agent.
It does not apply when mail is delivered with a different mail
delivery program. 



Example:




```

virtual\_mailbox\_base = /var/mail

```

