#! /usr/local/bin/python3

"""
Created by eggwizard

v1.0    Created
"""

import time

class tictoc:
    def __init__(self):
        self.time_tic = time.perf_counter()
        self.time_toc = self.time_tic

    def tic(self):
        self.time_tic = time.perf_counter()

    def toc(self):
        self.time_toc = time.perf_counter()
        self.time_delta = self.time_toc - self.time_tic
        print("Elapsed time: %.5f sec" %self.time_delta)

    
