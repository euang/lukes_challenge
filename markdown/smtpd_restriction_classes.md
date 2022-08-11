# smtpd_restriction_classes (default: empty)

User-defined aliases for groups of access restrictions. The aliases
can be specified in smtpd\_recipient\_restrictions etc., and on the
right-hand side of a Postfix access(5) table.




One major application is for implementing per-recipient UCE control.
See the RESTRICTION\_CLASS\_README document for other examples.



