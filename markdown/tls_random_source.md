# tls_random_source (default: see "postconf -d" output)
 The external entropy source for the in-memory tlsmgr(8) pseudo
random number generator (PRNG) pool. Be sure to specify a non-blocking
source. If this source is not a regular file, the entropy source
type must be prepended: egd:/path/to/egd\_socket for a source with
EGD compatible socket interface, or dev:/path/to/device for a
device file. 


 Note: on OpenBSD systems specify dev:/dev/arandom when dev:/dev/urandom
gives timeout errors. 


 This feature is available in Postfix 2.2 and later. 


