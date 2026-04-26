#!/usr/bin/env python3
import sys
from pycallgraph2 import PyCallGraph
from pycallgraph2.output import GraphvizOutput

def fib0(): return 0
def fib1(): return 1
s = """def fib{}(): return fib{}() + fib{}()"""

if __name__ == '__main__':
    for n in range(2, 10):
        exec(s.format(n, n-1, n-2))
    # Descomente estas duas linhas depois para testar a melhoria:
    # from functools import lru_cache
    # for n in range(10): exec("fib{} = lru_cache(1)(fib{})".format(n, n))
    graphviz = GraphvizOutput()
    graphviz.output_file = 'pycallgraph.png'
    with PyCallGraph(output=graphviz):
        print(f"Resultado de fib9: {eval('fib9()')}")
