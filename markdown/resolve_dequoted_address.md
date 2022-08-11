# resolve_dequoted_address (default: yes)
 Resolve a recipient address safely instead of correctly, by
looking inside quotes. 


 By default, the Postfix address resolver does not quote the
address localpart as per RFC 822, so that additional @ or % or !
operators remain visible. This behavior is safe but it is also
technically incorrect. 


 If you specify "resolve\_dequoted\_address = no", then
the Postfix
resolver will not know about additional @ etc. operators in the
address localpart. This opens opportunities for obscure mail relay
attacks with user@domain@domain addresses when Postfix provides
backup MX service for Sendmail systems. 


