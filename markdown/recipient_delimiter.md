# recipient_delimiter (default: empty)
 The set of characters that can separate an email address
localpart, user name, or a .forward file name from its extension.
For example, with "recipient\_delimiter = +", the software tries
user+foo@example.com before trying user@example.com, user+foo before
trying user, and .forward+foo before trying .forward. 


 More formally, an email address localpart or user name is
separated from its extension by the first character that matches
the recipient\_delimiter set. The delimiter character and extension
may then be used to generate an extended .forward file name. This
implementation recognizes one delimiter character and one extension
per email address localpart or email address. With Postfix 2.10 and
earlier, the recipient\_delimiter specifies a single character. 


 See canonical(5), local(8), relocated(5) and virtual(5) for the
effects of recipient\_delimiter on lookups in aliases, canonical,
virtual, and relocated maps, and see the propagate\_unmatched\_extensions
parameter for propagating an extension from one email address to
another. 


 When used in command\_execution\_directory, forward\_path, or
luser\_relay, ${recipient\_delimiter} is replaced with the actual
recipient delimiter that was found in the recipient email address
(Postfix 2.11 and later), or it is replaced with the main.cf
recipient\_delimiter parameter value (Postfix 2.10 and earlier).



 The recipient\_delimiter is not applied to the mailer-daemon
address, the postmaster address, or the double-bounce address. With
the default "owner\_request\_special = yes" setting, the recipient\_delimiter
is also not applied to addresses with the special "owner-" prefix
or the special "-request" suffix. 



Examples:




```

# Handle Postfix-style extensions.
recipient\_delimiter = +

```


```

# Handle both Postfix and qmail extensions (Postfix 2.11 and later).
recipient\_delimiter = +-

```


```

# Use .forward for mail without address extension, and for mail with
# an unrecognized address extension.
forward\_path = $home/.forward${recipient\_delimiter}${extension},
    $home/.forward

```

