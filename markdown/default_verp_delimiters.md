# default_verp_delimiters (default: +=)
 The two default VERP delimiter characters. These are used when
no explicit delimiters are specified with the SMTP XVERP command
or with the "**sendmail -XV**" command-line option (Postfix 2.2
and earlier: **-V**). Specify characters that are allowed by the
verp\_delimiter\_filter setting.




This feature is available in Postfix 1.1 and later.



