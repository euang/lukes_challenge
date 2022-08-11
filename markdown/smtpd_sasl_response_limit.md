# smtpd_sasl_response_limit (default: 12288)
 The maximum length of a SASL client's response to a server challenge.
When the client's "initial response" is longer than the normal limit for
SMTP commands, the client must omit its initial response, and wait for an
empty server challenge; it can then send what would have been its "initial
response" as a response to the empty server challenge. RFC4954 requires the
server to accept client responses up to at least 12288 octets of
base64-encoded text. The default value is therefore also the minimum value
accepted for this parameter.


 This feature is available in Postfix 3.4 and later. Prior versions use
"line\_length\_limit", which may need to be raised to accommodate larger client
responses, as may be needed with GSSAPI authentication of Windows AD users
who are members of many groups. 


