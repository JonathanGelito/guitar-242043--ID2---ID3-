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
        self.buffer = list(range(0, capacity))


    def size(self) -> int:
        '''
        Return number of items currently in the buffer
        '''
        # TO-DO: implement this

        return self._rear

    def is_empty(self) -> bool:
        '''
        Is the buffer empty (size equals zero)?
        '''
        # TO-DO: implement this
        if self._rear==0:
            return True
        
    def is_full(self) -> bool:
        '''
        Is the buffer full (size equals capacity)?
        '''
        # TO-DO: implement this
        if  self._rear==self.MAX_CAP:
            return True
        else:
            raise RingBufferFull

    def enqueue(self, x: float):
        '''
        Add item `x` to the end
        '''
        # TO-DO: implement this
        if(self._rear!=self.MAX_CAP):
            self.buffer[self._rear]=x
            self._rear+=1
        else:
            raise RingBufferFull

    def dequeue(self) -> float:
        '''
        Return and remove item from the front
        '''
        # TO-DO: implement this
        if(self._rear!=0):
            self._rear-=1   
            return self.buffer.pop(0)
        else:
            raise RingBufferEmpty
        


    def peek(self) -> float:
        '''
        Return (but do not delete) item from the front
        '''
        # TO-DO: implement this
        if(self._rear!=0):
            return self.buffer[0]
        else:
            raise RingBufferEmpty
        
    def printlist(self) -> list:
        '''
        Return (but do not delete) the list
        '''

        return self.buffer
    

    def getrear(self) -> int:
        '''
        Returns the rear
        '''

        return self._rear

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