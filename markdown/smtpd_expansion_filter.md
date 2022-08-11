# smtpd_expansion_filter (default: see "postconf -d" output)

What characters are allowed in $name expansions of RBL reply
templates. Characters not in the allowed set are replaced by "\_".
Use C like escapes to specify special characters such as whitespace.




The smtpd\_expansion\_filter value is not subject to Postfix configuration
parameter $name expansion.




This feature is available in Postfix 2.0 and later.



