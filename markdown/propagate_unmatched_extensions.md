# propagate_unmatched_extensions (default: canonical, virtual)

What address lookup tables copy an address extension from the lookup
key to the lookup result.




For example, with a virtual(5) mapping of "*joe@example.com =>
joe.user@example.net*", the address "*joe+foo@example.com*"
would rewrite to "*joe.user+foo@example.net*".




Specify zero or more of **canonical**, **virtual**, **alias**,
**forward**, **include** or **generic**. These cause
address extension
propagation with canonical(5), virtual(5), and aliases(5) maps,
with local(8) .forward and :include: file lookups, and with smtp(8)
generic maps, respectively. 



Note: enabling this feature for types other than **canonical**
and **virtual** is likely to cause problems when mail is forwarded
to other sites, especially with mail that is sent to a mailing list
exploder address.




Examples:




```

propagate\_unmatched\_extensions = canonical, virtual, alias,
        forward, include
propagate\_unmatched\_extensions = canonical, virtual

```

