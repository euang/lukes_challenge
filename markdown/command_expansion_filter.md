# command_expansion_filter (default: see "postconf -d" output)

Restrict the characters that the local(8) delivery agent allows in
$name expansions of $mailbox\_command and $command\_execution\_directory.
Characters outside the
allowed set are replaced by underscores.



