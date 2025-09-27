#!/usr/bin/env python3
# Jonathan "JG" Gelito, Matheus Rasay, E. "Mikey" de los Reyes
# 242043, 243780, 241438
# September 27, 2025

# I have not discussed the Python language code in my program 
# with anyone other than my instructor or the teaching assistants 
# assigned to this course.

# I have not used Python language code obtained from another student, 
# or any other unauthorized source, either modified or unmodified.

# If any Python language code or documentation used in my program 
# was obtained from another source, such as a textbook or website, 
# that has been clearly noted with a proper citation in the comments 
# of my program.

from ringbuffer import *
import math
import random
from functools import wraps


SAMP_RATE = 44100


class GuitarString:
    def __init__(self, frequency: float):
        '''
        Create a guitar string of the given frequency, using a sampling rate of 44100 Hz
        '''


        # TO-DO: implement this
        self.capacity = math.ceil(44100/frequency) # TO-DO: compute the max capacity of the ring buffer based on the frequency
        self.buffer = RingBuffer(self.capacity)  # TO-DO: construct the ring buffer object
        self.TICKs = 0
    @classmethod
    def make_from_array(cls, init: list[int]):
        '''
        Create a guitar string whose size and initial values are given by the array `init`
        '''
        # create GuitarString object with placeholder freq
        stg = cls(1000)

        stg.capacity = len(init)
        stg.buffer = RingBuffer(stg.capacity)
        for x in init:
            stg.buffer.enqueue(x)
        return stg

    def pluck(self):
        '''
        Set the buffer to white noise
        '''
        # TO-DO: implement this
        for _ in range(self.buffer.size()):
            self.buffer.dequeue()
        self.buffer._front=0
        self.buffer._rear=0
        self.TICKs=0
        for _ in range(self.capacity):
            self.buffer.enqueue(random.uniform(-0.5,0.5))


    def tick(self):
        '''
        Advance the simulation one time step by applying the Karplus--Strong update
        '''
        # TO-DO: implement this
        # Step 1: delete sample at front of ring buffer
        # Step 1: delete sample at front of ring buffer
        try:
            t0=self.buffer.dequeue()
        except RingBufferEmpty:
            t0=0
        try: 
            t1=self.buffer.peek()
        except RingBufferEmpty:
            t1=0
        self.TICKs +=1
        return self.buffer.enqueue(0.996*(t0+t1)/2)



    def sample(self) -> float:
        '''
        Return the current sample
        '''
        # TO-DO: implement this
        try: 
            x=self.buffer.peek()
        except RingBufferEmpty:
            x=0
        return x
        

    def time(self) -> int:
        '''
        Return the number of ticks so far
        '''
        # TO-DO: implement this

        # I wiil implement this later.
        return self.TICKs


        



