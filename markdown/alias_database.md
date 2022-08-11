# alias_database (default: see "postconf -d" output)

The alias databases for local(8) delivery that are updated with
"**newaliases**" or with "**sendmail -bi**".




This is a separate configuration parameter because not all the
tables specified with $alias\_maps have to be local files.




Examples:




```

alias\_database = hash:/etc/aliases
alias\_database = hash:/etc/mail/aliases

```

