# strict_8bitmime_body (default: no)

Reject 8-bit message body text without 8-bit MIME content encoding
information. This blocks mail from poorly written applications.




Unfortunately, this also rejects majordomo approval requests when
the included request contains valid 8-bit MIME mail, and it rejects
bounces from mailers that do not MIME encapsulate 8-bit content
(for example, bounces from qmail or from old versions of Postfix).




This feature should not be enabled on a general purpose mail server,
because it is likely to reject legitimate email.




This feature is available in Postfix 2.0 and later.



