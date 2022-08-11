# mydomain (default: see "postconf -d" output)

The internet domain name of this mail system. The default is to
use $myhostname minus the first component, or "localdomain" (Postfix
2.3 and later). $mydomain is used as
a default value for many other configuration parameters.




Example:




```

mydomain = domain.tld

```

