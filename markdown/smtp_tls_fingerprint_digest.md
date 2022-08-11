# smtp_tls_fingerprint_digest (default: see "postconf -d" output)
 The message digest algorithm used to construct remote SMTP server
certificate fingerprints. At the "fingerprint" TLS security level
(**smtp\_tls\_security\_level** = fingerprint), the server certificate is
verified by directly matching its certificate fingerprint or its public
key fingerprint (Postfix 2.9 and later). The fingerprint is the
message digest of the server certificate (or its public key)
using the selected
algorithm. With a digest algorithm resistant to "second pre-image"
attacks, it is not feasible to create a new public key and a matching
certificate (or public/private key-pair) that has the same fingerprint. 


 The default algorithm is **sha256** with Postfix ≥ 3.6
and the **compatibility\_level** set to 3.6 or higher. With Postfix
≤ 3.5, the default algorithm is **md5**. 


 The best-practice algorithm is now **sha256**. Recent advances in hash
function cryptanalysis have led to md5 and sha1 being deprecated in favor of
sha256. However, as long as there are no known "second pre-image" attacks
against the older algorithms, their use in this context, though not
recommended, is still likely safe. 


 While additional digest algorithms are often available with OpenSSL's
libcrypto, only those used by libssl in SSL cipher suites are available to
Postfix. You'll likely find support for md5, sha1, sha256 and sha512. 


 To find the fingerprint of a specific certificate file, with a
specific digest algorithm, run:




> 
> 
> ```
> 
> $ openssl x509 -noout -fingerprint -*digest* -in *certfile*.pem
> 
> ```
> 
> 


 The text to the right of the "=" sign is the desired fingerprint.
For example: 



> 
> 
> ```
> 
> $ openssl x509 -noout -fingerprint -sha256 -in cert.pem
> SHA256 Fingerprint=D4:6A:AB:19:24:...:BB:A6:CB:66:82:C0:8E:9B:EE:29:A8:1A
> 
> ```
> 
> 


 To extract the public key fingerprint from an X.509 certificate,
you need to extract the public key from the certificate and compute
the appropriate digest of its DER (ASN.1) encoding. With OpenSSL
the "-pubkey" option of the "x509" command extracts the public
key always in "PEM" format. We pipe the result to another OpenSSL
command that converts the key to DER and then to the "dgst" command
to compute the fingerprint. 


 The actual command to transform the key to DER format depends on the
version of OpenSSL used. As of OpenSSL 1.0.0, the "pkey" command supports
all key types. 



> 
> 
> ```
> 
> # OpenSSL ≥ 1.0 with SHA-256 fingerprints.
> $ openssl x509 -in cert.pem -noout -pubkey |
>     openssl pkey -pubin -outform DER |
>     openssl dgst -sha256 -c
> (stdin)= 64:3f:1f:f6:e5:1e:d4:2a:56:...:fc:09:1a:61:98:b5:bc:7c:60:58
> 
> ```
> 
> 


 The Postfix SMTP server and client log the peer (leaf) certificate
fingerprint and the public key fingerprint when the TLS loglevel is 2 or
higher. 


 This feature is available in Postfix 2.5 and later. 


