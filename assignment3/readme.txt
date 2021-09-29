The timing results for A* search show how it is just phenomonally faster than
iterative deepening. At a solution depth of 16, A* search found a solution in 
1/120th and 1/30th the time of iterative deepening for Manhattan distance and
Number of wrong tiles respectively. These times also conform to our expections
about how Manhattan and number of wrong tiles perform relative to each other.
Since the Manhattan distance dominates the number of wrong tiles as a search
heuristic, we expect it to find a solution much faster.

As an aside, my heuristic functions were not the best code I've written. If my
times are slower than others despite my A* function looking good, that is
probably why.

-------------------------------------------------------------------------------

A* Manhattan distance

Trying to find a solution for puzzle with solution of depth 2
Starting puzzle:
1 2 .
8 4 3
7 6 5
0.0003867149353027344
Found a solution, of depth 2
Solution path: [5, 4]

Trying to find a solution for puzzle with solution of depth 4
Starting puzzle:
1 2 3
6 . 4
8 7 5
0.0025510787963867188
Found a solution, of depth 4
Solution path: [3, 6, 7, 4]

Trying to find a solution for puzzle with solution of depth 8
Starting puzzle:
2 6 3
1 7 4
. 8 5
0.026015043258666992
Found a solution, of depth 8
Solution path: [7, 4, 1, 0, 3, 6, 7, 4]

Trying to find a solution for puzzle with solution of depth 10
Starting puzzle:
1 6 2
8 . 5
7 4 3
0.4718360900878906
Found a solution, of depth 10
Solution path: [5, 8, 7, 4, 1, 2, 5, 8, 7, 4]

Trying to find a solution for puzzle with solution of depth 12
Starting puzzle:
2 5 3
1 . 4
7 8 6
4.078825950622559
Found a solution, of depth 12
Solution path: [1, 2, 5, 4, 7, 8, 5, 2, 1, 0, 3, 4]

Trying to find a solution for puzzle with solution of depth 16
Starting puzzle:
8 3 .
6 1 7
5 4 2
5.804782867431641
Found a solution, of depth 16
Solution path: [1, 4, 5, 8, 7, 6, 3, 4, 5, 8, 7, 6, 3, 0, 1, 4]
A* Manhattan time 10.391018867492676


.A* num wrong tiles

Trying to find a solution for puzzle with solution of depth 2
Starting puzzle:
1 2 .
8 4 3
7 6 5
0.00017905235290527344
Found a solution, of depth 2
Solution path: [5, 4]

Trying to find a solution for puzzle with solution of depth 4
Starting puzzle:
1 2 3
6 . 4
8 7 5
0.0010001659393310547
Found a solution, of depth 4
Solution path: [3, 6, 7, 4]

Trying to find a solution for puzzle with solution of depth 8
Starting puzzle:
2 6 3
1 7 4
. 8 5
0.015770673751831055
Found a solution, of depth 8
Solution path: [7, 4, 1, 0, 3, 6, 7, 4]

Trying to find a solution for puzzle with solution of depth 10
Starting puzzle:
1 6 2
8 . 5
7 4 3
0.2618858814239502
Found a solution, of depth 10
Solution path: [5, 8, 7, 4, 1, 2, 5, 8, 7, 4]

Trying to find a solution for puzzle with solution of depth 12
Starting puzzle:
2 5 3
1 . 4
7 8 6
13.211047172546387
Found a solution, of depth 12
Solution path: [1, 2, 5, 4, 7, 8, 5, 2, 1, 0, 3, 4]

Trying to find a solution for puzzle with solution of depth 16
Starting puzzle:
8 3 .
6 1 7
5 4 2
21.791930198669434
Found a solution, of depth 16
Solution path: [1, 4, 5, 8, 7, 6, 3, 4, 5, 8, 7, 6, 3, 0, 1, 4]
A* num time 35.49337387084961