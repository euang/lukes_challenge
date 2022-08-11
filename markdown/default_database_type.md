# default_database_type (default: see "postconf -d" output)

The default database type for use in newaliases(1), postalias(1)
and postmap(1) commands. On many UNIX systems the default type is
either **dbm** or **hash**. The default setting is frozen
when the Postfix system is built.




Examples:




```

default\_database\_type = hash
default\_database\_type = dbm

```

