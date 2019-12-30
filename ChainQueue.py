# -*- coding: UTF-8

class Node(object):
	def __init__(self, data):
		self.data = data
		self.next = None

class Queue(object):#链式队列
	def __init__(self):
		self.head = None
		self.tail = None
	
	def is_empty(self):
		if self.head is None:
			print('This is an empty queue')
		else:
			print('This is not an empty queue')

	def enqueue(self, data):
		node = Node(data)
		if self.head is None:
			self.head = node
			self.tail = node
		else:
			self.tail.next = node
			self.tail = node

	def dequeue(self):
		if self.head is None:
			print('This is an empty queue')
			return
		cur = self.head
		self.head = cur.next
		return cur.data

	def iter(self):
		if self.head is None:
			print('This is an empty queue')
			return
		while self.head is not None:
			print(self.dequeue())




if __name__ == '__main__':
	queue = Queue()
	queue.is_empty()
	queue.enqueue(1)
	queue.is_empty()
	print(queue.dequeue())
	queue.is_empty()
	queue.enqueue(1)
	queue.enqueue(2)
	queue.enqueue(3)
	queue.iter()





