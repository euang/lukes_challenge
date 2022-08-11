# defer_transports (default: empty)

The names of message delivery transports that should not deliver mail
unless someone issues "**sendmail -q**" or equivalent. Specify zero
or more mail delivery transport names that appear in the
first field of master.cf.




Example:




```

defer\_transports = smtp

```

