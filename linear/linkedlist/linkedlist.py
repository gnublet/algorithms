class node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class linked_list:
    def __init__(self):
        self.head = None
    # add a node to front
    def add_at_front(self, data):
        self.head = node(data=data, next=self.head)
    # check if linked list is empty
    def is_empty(self):
        return self.head == None
    # add node to end
    def add_at_end(self, data):
        # just in case head doesn't exist
        if not self.head:
            self.head = node(data=data)
            return
        # iterate cursor to end
        curr = self.head
        while curr.next:
            curr = curr.next
        # at new node at end
        curr.next = node(data=data)
    # delete the first node with a certain value
    def delete_node(self, key):
        curr = self.head
        prev = None
        # iterate and stop until we hit the key
        while curr and curr.data != key:
            prev = curr
            curr = curr.next
        # if first element was the element we wish to delete
        if prev is None:
            self.head = curr.next
        elif curr:
            prev.next = curr.next # make linked list skip our node to be deleted
            curr.next = None # get rid of dangling pointer
    # get the value of the last node
    def get_last_node(self):
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        return temp.data
    # print list of nodes
    def __str__(self):
        node = self.head
        pretty_string = ''
        while node != None:
            # print(node.data, end=" -> ")
            pretty_string += str(node.data) + '->'
            node = node.next
        return pretty_string
        
def main():
    ll = linked_list() # class instantiation uses function notation
    ll.add_at_front(0)
    ll.add_at_end(3)
    ll.add_at_front(1)
    ll.delete_node(3)
    print(ll)

main()