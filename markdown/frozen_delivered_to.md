# frozen_delivered_to (default: yes)
 Update the local(8) delivery agent's idea of the Delivered-To:
address (see prepend\_delivered\_header) only once, at the start of
a delivery attempt; do not update the Delivered-To: address while
expanding aliases or .forward files. 


 This feature is available in Postfix 2.3 and later. With older
Postfix releases, the behavior is as if this parameter is set to
"no". The old setting can be expensive with deeply nested aliases
or .forward files. When an alias or .forward file changes the
Delivered-To: address, it ties up one queue file and one cleanup
process instance while mail is being forwarded. 


