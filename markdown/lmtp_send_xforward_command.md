# lmtp_send_xforward_command (default: no)

Send an XFORWARD command to the remote LMTP server when the LMTP LHLO
server response announces XFORWARD support. This allows an lmtp(8)
delivery agent, used for content filter message injection, to
forward the name, address, protocol and HELO name of the original
client to the content filter and downstream LMTP server.
Before you change the value to yes, it is best to make sure that
your content filter supports this command.




This feature is available in Postfix 2.1 and later.



