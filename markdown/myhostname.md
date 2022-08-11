# myhostname (default: see "postconf -d" output)

The internet hostname of this mail system. The default is to use
the fully-qualified domain name (FQDN) from gethostname(), or to
use the non-FQDN result from gethostname() and append ".$mydomain".
$myhostname is used as a default value for many other configuration
parameters. 



Example:




```

myhostname = host.example.com

```

