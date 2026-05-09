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
+ Show as busy
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
+ [Name go here] - A library for reporting to Factor DB is going to be used as a basis for this project (provide relevant links and info here)
---
## Design Explanation:
+ Why Python: Libraries already exist and the integer limit in python is dynamically accomadated for. This allows for easy and accurate computation
