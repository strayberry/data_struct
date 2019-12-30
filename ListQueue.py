# -*- coding: UTF-8

class Queue:#数组队列
    def __init__(self):#初始化
        self.__queue=[]
        self.__size=0
    def __str__(self):
        return ''.join([str(i) for i in self.__queue])
    def size(self):
        return self.__size
    def is_empty(self):
        return self.__size<=0
    def enqueue(self,data):#入队
        self.__queue.append(data)
        self.__size+=1
    def dequeue(self):#出队
        if self.is_empty():
            return -1
        else:
            self.__size-=1
            return self.__queue.pop(0)
 
class Deque:#双向队列
    def _init_(self):
        self.__queue=[]
        self.__size=0
    def __str__(self):
        return ''.join([str(i) for i in self._queue])
    def is_empty(self):
        return self.__size==0
    def insert_front(self,data):#相当于单向队列的入队
        self.__queue.append(data)
        self.__size+=1
    def insert_rear(self,data):
        self.__queue.insert(0,data)
        self.__size+=1
    def delete_rear(self):
        if self.is_empty():
            return -1
        self.__size-=1
        return self.__queue.pop(0)
    
    def delet_front(self):
        if self.is_empty():
            return -1
        self.__size-=1
        return self.__queue.pop()
    def size(self):
        return self.__size
