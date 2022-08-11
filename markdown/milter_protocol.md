# milter_protocol (default: 6)
 The mail filter protocol version and optional protocol extensions
for communication with a Milter application; prior to Postfix 2.6
the default protocol is 2. Postfix
sends this version number during the initial protocol handshake.
It should match the version number that is expected by the mail
filter application (or by its Milter library). 


Protocol versions: 



2 Use Sendmail 8 mail filter protocol version 2 (default
with Sendmail version 8.11 .. 8.13 and Postfix version 2.3 ..
2.5).
3 Use Sendmail 8 mail filter protocol version 3.
4 Use Sendmail 8 mail filter protocol version 4.
6 Use Sendmail 8 mail filter protocol version 6 (default
with Sendmail version 8.14 and Postfix version 2.6).

Protocol extensions: 



no\_header\_reply  Specify this when the Milter application
will not reply for each individual message header.

 This feature is available in Postfix 2.3 and later. 


