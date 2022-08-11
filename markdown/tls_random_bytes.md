# tls_random_bytes (default: 32)
 The number of bytes that tlsmgr(8) reads from $tls\_random\_source
when (re)seeding the in-memory pseudo random number generator (PRNG)
pool. The default of 32 bytes (256 bits) is good enough for 128bit
symmetric keys. If using EGD or a device file, a maximum of 255
bytes is read. 


 This feature is available in Postfix 2.2 and later. 


