# authorized_flush_users (default: static:anyone)

List of users who are authorized to flush the queue.




By default, all users are allowed to flush the queue. Access is
always granted if the invoking user is the super-user or the
$mail\_owner user. Otherwise, the real UID of the process is looked
up in the system password file, and access is granted only if the
corresponding login name is on the access list. The username
"unknown" is used for processes whose real UID is not found in the
password file. 



Specify a list of user names, "/file/name" or "type:table" patterns,
separated by commas and/or whitespace. The list is matched left to
right, and the search stops on the first match. A "/file/name"
pattern is replaced
by its contents; a "type:table" lookup table is matched when a name
matches a lookup key (the lookup result is ignored). Continue long
lines by starting the next line with whitespace. Specify "!pattern"
to exclude a name from the list. The form "!/file/name" is supported
only in Postfix version 2.4 and later. 



This feature is available in Postfix 2.2 and later.



