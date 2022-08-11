# enable_original_recipient (default: yes)
 Enable support for the original recipient address after an
address is rewritten to a different address (for example with
aliasing or with canonical mapping). 


 The original recipient address is used as follows: 



 Final delivery   With "enable\_original\_recipient =
yes", the original recipient address is stored in the **X-Original-To**
message header. This header may be used to distinguish between
different recipients that share the same mailbox. 
 Recipient deduplication   With "enable\_original\_recipient
= yes", the cleanup(8) daemon performs duplicate recipient elimination
based on the content of (original recipient, maybe-rewritten
recipient) pairs. Otherwise, the cleanup(8) daemon performs duplicate
recipient elimination based only on the maybe-rewritten recipient
address. 

 Note: with Postfix ≤ 3.2 the "setting enable\_original\_recipient
= **no**" breaks address verification for addresses that are
aliased or otherwise rewritten (Postfix is unable to store the
address verification result under the original probe destination
address; instead, it can store the result only under the rewritten
address). 


 This feature is available in Postfix 2.1 and later. Postfix
version 2.0 behaves as if this parameter is always set to **yes**.
Postfix versions before 2.0 have no support for the original recipient
address. 


