# -*- coding: UTF-8

class Node(object):
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList(object):#链表
	def __init__(self):
		self.head = None
		self.tail = None

	def is_empty(self):
		if self.head is None:
			print('The linkedlist is empty')
		else:
			print('The linkedlist is not empty')

	def append(self, data): #在末插入节点
		node = Node(data)
		if self.head is None:
			self.head = node
			self.tail = node
		else:
			self.tail.next = node
			self.tail = node

	def iter(self): #遍历
		if self.head is None:
			print('The linkedlist is empty')
		else:
			cur = self.head
			while cur is not None:
				print(cur.data)
				cur = cur.next

	def insert(self, index, value): #在第n的位置插入节点
		cur = self.head
		cur_index = 0
		# 空链表时
		if cur is None:
			print('List is empty')
			return
		while cur_index < index-1:
			cur = cur.next
			# 插入位置超出链表节点的长度时
			if cur is None:
				print('list length less than index')
				return
			cur_index += 1
		node = Node(value)
		node.next = cur.next
		cur.next = node
		# 插入位置是链表的最后一个节点时，需要移动tail
		if node.next is None:
			self.tail = node

	def remove(self, index): #移除第n个节点
		cur = self.head
		cur_index = 0
		if cur is None: # 空链表时
			print('List is empty')
			return
		while cur_index < index-1:
			cur = cur.next
			if cur is None:
				print('list length less than index')
			cur_index += 1
		if index == 0: # 当删除第一个节点时
			self.head = cur.next
			cur = cur.next
			return
		if self.head is self.tail: # 当只有一个节点的链表时
			self.head = None
			self.tail = None
			return
		cur.next = cur.next.next
		if cur.next is None:   # 当删除的节点是链表最后一个节点时
			self.tail = cur
	

	def search(self,item): #查找节点位置
		cur = self.head
		cur_index = 0
		if cur is None: # 空链表时
			print('List is empty')
			return
		while cur.data != item:
			cur = cur.next
			cur_index += 1
		print("iterm index :" + str(cur_index))



if __name__ == '__main__':
	linkedList = LinkedList()
	linkedList.is_empty()
	linkedList.append(1)
	linkedList.append(2)
	linkedList.is_empty()
	linkedList.iter()
	linkedList.insert(2,3)
	linkedList.iter()
	linkedList.remove(2)
	linkedList.iter()
	linkedList.search(2)



