# tls_daemon_random_bytes (default: 32)
 The number of pseudo-random bytes that an smtp(8) or smtpd(8)
process requests from the tlsmgr(8) server in order to seed its
internal pseudo random number generator (PRNG). The default of 32
bytes (equivalent to 256 bits) is sufficient to generate a 128bit
(or 168bit) session key. 


 This feature is available in Postfix 2.2 and later. 


