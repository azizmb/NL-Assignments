Instructions
============

To run unittests:
-----------------

    python test.py


To use function:
----------------

    >>> import combinations
    >>> c = [combo for combo in combinations.generate_combinations("ASDF", 2)]
    >>> print c
    [['A', 'S'], ['A', 'D'], ['A', 'F'], ['S', 'D'], ['S', 'F'], ['D', 'F']]
    >>>