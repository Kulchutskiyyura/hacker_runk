def findMergeNode(head1, head2):
    first_node_dict = {}
    while head1:
        first_node_dict.update({id(head1): head1.data})
        head1 = head1.next

    print(first_node_dict)

    while head2:
        if id(head2) in first_node_dict:
            return first_node_dict[id(head2)]

        head2 = head2.next
