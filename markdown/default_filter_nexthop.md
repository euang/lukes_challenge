# default_filter_nexthop (default: empty)
 When a content\_filter or FILTER request specifies no explicit
next-hop destination, use $default\_filter\_nexthop instead; when
that value is empty, use the domain in the recipient address.
Specify "default\_filter\_nexthop = $myhostname" for compatibility
with Postfix version 2.6 and earlier, or specify an explicit next-hop
destination with each content\_filter value or FILTER action. 


 This feature is available in Postfix 2.7 and later. 


