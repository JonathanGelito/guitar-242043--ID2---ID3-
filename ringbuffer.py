#!/usr/bin/env python3


class RingBuffer:
    def __init__(self, capacity: int):
        '''
        Create an empty ring buffer, with given max capacity
        '''


        # TO-DO: implement this
        self.MAX_CAP = capacity
        self._front = 0
        self._rear =  0
        self.buffer = [None]*capacity


    def size(self) -> int:
        '''
        Return number of items currently in the buffer
        '''
        # TO-DO: implement this
        if self._front>=self.MAX_CAP:
                self._front=0  
        if self._rear>=self.MAX_CAP:
                self._rear=0  
        if abs(self._rear-self._front)!=0:
            return abs(self._rear-self._front)
        else:
            if self.buffer[self._rear]!=None:
                return self.MAX_CAP
            else: return 0

        

    def is_empty(self) -> bool:
        '''
        Is the buffer empty (size equals zero)?
        '''
        # TO-DO: implement this
        if self._rear==self._front and self.buffer[self._front]==None:
            return True
        
    def is_full(self) -> bool:
        '''
        Is the buffer full (size equals capacity)?
        '''
        # TO-DO: implement this
        if  self.size()==self.MAX_CAP:
            return True

    def enqueue(self, x: float):
        '''
        Add item `x` to the end
        '''
        # TO-DO: implement this
        
        if(not (self.is_full())):
            if self._rear>=self.MAX_CAP:
                self._rear=0 
            self.buffer[self._rear]=x
            self._rear+=1       
        else:
            raise RingBufferFull

    def dequeue(self) -> float:
        '''
        Return and remove item from the front
        '''
        # TO-DO: implement this
        if(not (self.is_empty())):
            if self._front>=self.MAX_CAP:
                self._front=0  
            x=self.buffer[self._front]
            self.buffer[self._front]=None
            self._front+=1
            return x         
        else:
            raise RingBufferEmpty
        


    def peek(self) -> float:
        '''
        Return (but do not delete) item from the front
        '''
        # TO-DO: implement this
        if self._front>=self.MAX_CAP:
                self._front=0           
        if(self.buffer[self._front]!=None):
            return self.buffer[self._front]
        else:
            raise RingBufferEmpty
        
class RingBufferFull(Exception):
    '''
    The exception raised when the ring buffer is full when attempting to
    enqueue.
    '''
    pass

class RingBufferEmpty(Exception):
    '''
    The exception raised when the ring buffer is empty when attempting to
    dequeue or peek.
    '''
    pass