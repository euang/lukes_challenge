# alias_maps (default: see "postconf -d" output)

The alias databases that are used for local(8) delivery. See
aliases(5) for syntax details.
Specify zero or more "type:name" lookup tables, separated by
whitespace or comma. Tables will be searched in the specified order
until a match is found.
Note: these lookups are recursive.




The default list is system dependent. On systems with NIS, the
default is to search the local alias database, then the NIS alias
database.




If you change the alias database, run "**postalias /etc/aliases**"
(or wherever your system stores the mail alias file), or simply
run "**newaliases**" to build the necessary DBM or DB file.




The local(8) delivery agent disallows regular expression substitution
of $1 etc. in alias\_maps, because that would open a security hole.




The local(8) delivery agent will silently ignore requests to use
the proxymap(8) server within alias\_maps. Instead it will open the
table directly. Before Postfix version 2.2, the local(8) delivery
agent will terminate with a fatal error.




Examples:




```

alias\_maps = hash:/etc/aliases, nis:mail.aliases
alias\_maps = hash:/etc/aliases

```

