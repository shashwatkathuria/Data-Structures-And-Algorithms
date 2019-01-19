# JOBS MINIMUM TIME COMPLETION ALGORITHM - GREEDY ALGORITHM
------------------------------------------------
INSTRUCTONS TO RUN THE PROGRAM
------------------------------------------------

The following command must be executed to run the program:

          python JOBS.py

------------------------------------------------
ALGORITHM
------------------------------------------------

In Jobs Minimum Completion Time Algorithm, a greedy based approach
is used to get the correct answer. The jobs are executed in the order of
weight to length ratio. In the wrong version, the jobs are executed in the
order of weight - length as is proved by the program (conflicts are solved
by executing the job with more weight first). The run time complexity of
both the algorithms are mainly governed by sorting which is O(nlogn) where
n is the number of jobs.

------------------------------------------------
