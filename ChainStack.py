# -*- coding: UTF-8

class Node(object):
	def __init__(self, data):
		self.data = data
		self.next = None

class Stack(object):#链式栈
	def __init__(self):
		self.top = None

	def is_empty(self):
		if self.top is None:
			print('This is an empty stack')


	def push(self,value):
		node = Node(value)
		node.next = self.top
		self.top = node

	def pop(self):
		node = self.top
		if node is None:
			print('This is an empty stack')
			return
		self.top = node.next
		return node.data

	def peek(self):
		node = self.top
		if node is None:
			print('This is an empty stack')
			return
		return node.value		

    def size(self):
        node = self.top
        count = 0
        if node is None:
            raise Exception('This is an empty stack')
        while node is not None:
            count += 1
            node = node.next
        return count
        

if __name__ == '__main__':
	stack = Stack()
	stack.push(1)
	print(stack.pop())
	stack.push(2)
	print(stack.pop())
