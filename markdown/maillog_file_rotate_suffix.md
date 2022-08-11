# maillog_file_rotate_suffix (default: %Y%m%d-%H%M%S)
 The format of the suffix to append to $maillog\_file while rotating
the file with "postfix logrotate". See strftime(3) for syntax. The
default suffix, YYYYMMDD-HHMMSS, allows logs to be rotated frequently.



 This feature is available in Postfix 3.4 and later. 


