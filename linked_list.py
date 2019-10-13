class Node():
    def __init__(self,val):
        self.next=None
        self.value=val


i=int(input("Enter the number of elements to be inserted : "))
head_node_value=int(input("Enter the value of head node : "))
head=Node(head_node_value)
current=head

i-=1
while(i):
    n=int(input("Enter an element to be inserted in the linked list : "))
    some=Node(n)
    current.next=some
    current=some
    i-=1

current=head

while(current):
    print(current.value,"-->",end="")
    current=current.next
print("NULL")
