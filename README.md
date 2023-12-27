# genetic-algorithm-flow-shop-scheduling-problem

A flowshop is a common production setting in factories where products start processing at machine or stage 1 and continue processing until they are finished in the last machine m. 

A common simplification in the flowshop literature is to consider only *n!* schedules and once the production sequence of jobs for the first machine is determined, is kept unaltered for all other machines.

## Short description of the problem
The problem is the permutation flowshop sequencing problem, in which ***n*** jobs have to be processed (in the same order) on ***m*** machines.
- A job cannot be transferred to the next machine before it's processing is finished, i.e all jobs must be processed sequentially in all machines.
- A machine processes no more than one job at a time.

The objective is to find the permutation of jobs which will minimize the *makespan*

The flow shop problems are characterized by the processing times *p<sub>ij</sub>* of job *i* on machine *j*.

Having a job permutation {*J<sub>1</sub>, J<sub>2</sub>, ..., J<sub>n</sub>*}, and processing times *p(i, j)*, we can calculate the completiom times *C(J<sub>i</sub>, j)* as follows:

*C(J<sub>1</sub>, 1)* = *p(J<sub>1</sub>, 1)*  (The completion time of job 1 at machine 1 is calculated as the processing time of this first job at this machine)

*C(J<sub>i</sub>, 1)* = *C(J<sub>i-1</sub>, 1) + p(J<sub>i</sub>, 1)* for *i=2, ..., n*

