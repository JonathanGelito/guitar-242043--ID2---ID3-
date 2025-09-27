from guitarstring import GuitarString
from stdaudio import play_sample
import stdkeys

if __name__ == '__main__':
    # initialize window
    stdkeys.create_window()

    keyboard = "q2we4r5ty7u8i9op-[=]"

    string_keys = [] #Equivalent to string_LETTER variables
    for i in range(20):
        string_keys.append(GuitarString(440 * 1.059463 ** (i-12)))

    n_iters = 0
    currently_playing = [] #For the note currently playing
    
    while True:
        # it turns out that the bottleneck is in polling for key events
        # for every iteration, so we'll do it less often, say every 
        # 1000 or so iterations
        if n_iters == 1000:
            stdkeys.poll()
            n_iters = 0     
        n_iters += 1

        # check if the user has typed a key; if so, process it
        if stdkeys.has_next_key_typed():
            #To prevent crashing from integer overflow
            #currently_playing.clear() 
            #sample = 0.0
            #Assign a key variable
            key = stdkeys.next_key_typed()
            #Make it so that it gets the index of the key, and plucks the correct
            #string_keys item based on the index given.
            if key in list(keyboard): #Prevents crashing if another key is pressed
                if string_keys[list(keyboard).index(key)] in currently_playing:
                    currently_playing.remove(string_keys[list(keyboard).index(key)])
                string_keys[list(keyboard).index(key)].pluck()
                currently_playing.append(string_keys[list(keyboard).index(key)])
        

        
        

        # compute the superposition of samples
        sample=0.0
        for c in currently_playing:
            # determine whether or not the sample should be cleared  based on time
            if c.time()<65336:
                if -1<sample+c.sample()<1:
                    sample += c.sample()
            else:
                currently_playing.remove(c)


        # play the sample on standard audio
        play_sample(sample)

        # advance the simulation of each guitar string by one step
        for c in currently_playing:
            c.tick()

        