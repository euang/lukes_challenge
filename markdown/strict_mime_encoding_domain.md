# strict_mime_encoding_domain (default: no)

Reject mail with invalid Content-Transfer-Encoding: information
for the message/\* or multipart/\* MIME content types. This blocks
mail from poorly written software.




This feature should not be enabled on a general purpose mail server,
because it will reject mail after a single violation.




This feature is available in Postfix 2.0 and later.



