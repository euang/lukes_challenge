# lmtp_assume_final (default: no)
 When a remote LMTP server announces no DSN support, assume that
the
server performs final delivery, and send "delivered" delivery status
notifications instead of "relayed". The default setting is backwards
compatible to avoid the infinitesimal possibility of breaking
existing LMTP-based content filters. 


