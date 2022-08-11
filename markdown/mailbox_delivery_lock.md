# mailbox_delivery_lock (default: see "postconf -d" output)

How to lock a UNIX-style local(8) mailbox before attempting delivery.
For a list of available file locking methods, use the "**postconf
-l**" command.




This setting is ignored with **maildir** style delivery,
because such deliveries are safe without explicit locks.




Note: The **dotlock** method requires that the recipient UID or
GID has write access to the parent directory of the mailbox file.




Note: the default setting of this parameter is system dependent.



