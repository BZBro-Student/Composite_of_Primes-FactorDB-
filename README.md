# Semi-Prime Generator Distributed Project
## Project Overview:
    The goal of this project is to learn how to distribute computations amongst a small computer system in a master/minion configuration. For my purposes I will be using 1 rpi3 as the master and 3 rpi1 as the minions. Minions will be given a batch of primes of n digit length in pairs (over ssh, possibly all in memory to avoid card wear). Minions will multiply the prime pairs together and send the batch result back to the master, master will then check for redundant (already factored) results before sending the result to the database (FactorDB).

---
 ## Project Specs:
### - Master:
+ Generates batches of primes (ideally enough to run in memory)
+ Uses SSH to send primes (probably to standin)
+ Receives completed batches (possibly in seperate process)
+ Reports semiprimes
### - Minion:
+ Receive prime pairs
+ Find product of prime pairs
+ Send result to master (maybe master reads standout)
+ Show as ready for new batch.
---
## OOP objectives:
+ Logic for generation handled in it's own class
+ Checking and receiving results in it's own class (possibly seperate process entirely)
+ Logic for multiplication kept to itself
+ Logic for reporting kept to itself
---
## Libraries:
+ Factor-DB - A library for reporting to Factor DB is going to be used as a basis for this project (provide relevant links and info here)
+ SymPy - Symbolic math library used to run prime generation
---
## Design Explanation:
+ Why Python: Libraries already exist and the integer limit in python is dynamically accomadated for. This allows for easy and accurate computation at any level
---
## Results:
After running this program for about 24 hours the program had managed to report 16460 new entries to the database, that is about 686 succesful submissions per hour or 11 succesful submissions a minute. 
The biggest time lost is the time needed by each device to do an SSH handshake which can take a long time especially on older hardware such as the three pi1's being used which are limited to 10 mbs read and write
speeds. On top of this the pi3s generation of primes is a polynomial runtime task, if everything was being run on the same machine this would likely be what overtakes the rest of runtime assuming no overhead while 
reporting to the actual database. Probable improvements to be made would be to see about sending a batch payload to the DB if possible. SSH could probably be kept open between batches to lower the cost of handshake.
