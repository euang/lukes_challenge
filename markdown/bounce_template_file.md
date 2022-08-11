# bounce_template_file (default: empty)
 Pathname of a configuration file with bounce message templates.
These override the built-in templates of delivery status notification
(DSN) messages for undeliverable mail, delayed mail, successful
delivery, or delivery verification. The bounce(5) manual page
describes how to edit and test template files. 


 Template message body text may contain $name references to
Postfix configuration parameters. The result of $name expansion can
be previewed with "**postconf -b *file\_name***" before the file
is placed into the Postfix configuration directory. 


 This feature is available in Postfix 2.3 and later. 


