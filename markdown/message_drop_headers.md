# message_drop_headers (default: bcc, content-length, resent-bcc, return-path)
 Names of message headers that the cleanup(8) daemon will remove
after applying header\_checks(5) and before invoking Milter applications.
The default setting is compatible with Postfix < 3.0. 


 Specify a list of header names, separated by comma or space.
Names are matched in a case-insensitive manner. The list of supported
header names is limited only by available memory. 


 This feature is available in Postfix 3.0 and later. 


