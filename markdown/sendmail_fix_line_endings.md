# sendmail_fix_line_endings (default: always)
 Controls how the Postfix sendmail command converts email message
line endings from <CR><LF> into UNIX format (<LF>).




 **always**   Always convert message lines ending
in <CR><LF>. This setting is the default with Postfix
2.9 and later. 
 **strict**   Convert message lines ending in
<CR><LF> only if the first input line ends in
<CR><LF>. This setting is backwards-compatible with
Postfix 2.8 and earlier. 
 **never**   Never convert message lines ending in
<CR><LF>. This setting exists for completeness only.


 This feature is available in Postfix 2.9 and later. 


