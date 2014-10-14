sr-2014-match-munging
=====================

Some scripts for generating statistics about the Student Robotics 2014 competition.

Usage
-----

First, clone the results repository into an `sr2014-comp` subdirectory, and aggregate the data:

    $ git clone git://srobo.org/comp/sr2014-comp.git
    $ ./aggregate.py

You can then run any of the analysis scripts (`robot_moved.py`, `token_fiddled.py`, or `two_tokens_fiddled.py`).
