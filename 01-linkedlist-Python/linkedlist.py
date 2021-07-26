"""The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value.
Then, use "Test Run" and "Submit" to run the test cases
at the bottom."""

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        # Your code goes here
        n = self.head
        if self.head:
            while n.next:
                n = n.next
            n.next = new_element
        else:
            self.head = new_element
            
    def get_position(self, position):
        if position < 1:
            return None
        count=1
        n=self.head
        while n and count<=position:
            if count==position:
                return n
            count=count+1
            n=n.next
        return None

        # counter = 1
        # current = self.head
        # if position < 1:
        #     return None
        # while current and counter <= position:
        #     if counter == position:
        #         return current
        #     current = current.next
        #     counter += 1
        # return None
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        # Your code goes here
        pass
    
    def insert(self, new_element, position):
        count=1
        n=self.head

        if position>1:
            while n and count < position:
                if count == position-1:
                    new_element.next = n.next
                    n.next = new_element
                n = n.next
                count += 1   
        elif position==1:
            new_element.next=self.head
            self.head=new_element
        # count=0
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
    
    
    def delete(self, value):
        """Delete the first node with a given value."""
        # Your code goes her
        n = self.head
        previous = None
        while n.value != value and n.next:
            previous = n
            n = n.next

        if n.value == value:
            if previous:
                previous.next = n.next
            else:
                self.head = n.next



