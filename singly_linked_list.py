class Node:
	def __init__(self, value):
		self.next = None
		self.value = value

class LinkedList:
	def __init__(self):
		self.head = None

	def get_head(self):
		return self.head

	def insert_node(self, value):
		if self.head is None:
			self.head = Node(value)
		else:
			temp = self.head
			while temp.next:
				temp = temp.next
			temp.next = Node(value)

def print_list(node):
	print(node.value)
	while node.next:
		node = node.next
		print(node.value)

list_1 = LinkedList()
arr = [1,2,3,4,4,6,7,4,2,8]
for i in arr:
	list_1.insert_node(i)
print_list(list_1.get_head())