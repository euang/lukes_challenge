# disable_mime_input_processing (default: no)

Turn off MIME processing while receiving mail. This means that no
special treatment is given to Content-Type: message headers, and
that all text after the initial message headers is considered to
be part of the message body.




This feature is available in Postfix 2.0 and later.




Mime input processing is enabled by default, and is needed in order
to recognize MIME headers in message content.



