# message_strip_characters (default: empty)
 The set of characters that Postfix will remove from message
content. The usual C-like escape sequences are recognized: \a
\b \f \n \r \t \v \*ddd* (up to three octal digits) and
\\. 


 Note 1: this feature does not recognize text that requires MIME
decoding. It inspects raw message content, just like header\_checks
and body\_checks. 


 Note 2: this feature is disabled with "receive\_override\_options
= no\_header\_body\_checks". 


 Example: 



```

message\_strip\_characters = \0

```

 This feature is available in Postfix 2.3 and later. 


