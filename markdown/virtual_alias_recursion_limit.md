# virtual_alias_recursion_limit (default: 1000)

The maximal nesting depth of virtual alias expansion. Currently
the recursion limit is applied only to the left branch of the
expansion graph, so the depth of the tree can in the worst case
reach the sum of the expansion and recursion limits. This may
change in the future.




This feature is available in Postfix 2.1 and later.



