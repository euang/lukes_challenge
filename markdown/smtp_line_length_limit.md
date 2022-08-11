# smtp_line_length_limit (default: 998)

The maximal length of message header and body lines that Postfix
will send via SMTP. This limit does not include the <CR><LF>
at the end of each line. Longer lines are broken by inserting
"<CR><LF><SPACE>", to minimize the damage to MIME
formatted mail. Specify zero to disable this limit.




The Postfix limit of 998 characters not including <CR><LF>
is consistent with the SMTP limit of 1000 characters including
<CR><LF>. The Postfix limit was 990 with Postfix 2.8
and earlier.



