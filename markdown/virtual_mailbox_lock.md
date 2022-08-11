# virtual_mailbox_lock (default: see "postconf -d" output)

How to lock a UNIX-style virtual(8) mailbox before attempting
delivery. For a list of available file locking methods, use the
"**postconf -l**" command.



 This parameter is specific to the virtual(8) delivery agent.
It does not apply when mail is delivered with a different mail
delivery program. 



This setting is ignored with **maildir** style delivery, because
such deliveries are safe without application-level locks.




Note 1: the **dotlock** method requires that the recipient UID
or GID has write access to the parent directory of the recipient's
mailbox file.




Note 2: the default setting of this parameter is system dependent.



