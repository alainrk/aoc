from collections import defaultdict, Counter, deque, OrderedDict
from heapq import heappush, heappop, heapify, nlargest, nsmallest
from bisect import bisect_left, bisect_right, insort
from itertools import permutations, combinations, combinations_with_replacement, accumulate, product, groupby, count
from functools import lru_cache, reduce
from math import gcd, lcm, sqrt, ceil, floor, factorial
import math
from copy import deepcopy
import re
import sys
import typing
import string

# https://regex101.com/
# result = re.search(r"(\b[A-Z]+\b).+(\b\d+)", "this MATCH with 123")
# print(result.groups()) # ('MATCH', '123')

sys.setrecursionlimit(100000)

def lmap(func, *iterables):
  return list(map(func, *iterables))
def flatten(l):
  return [i for x in l for i in x]
def ints(s: str) -> typing.List[int]:
  return lmap(int, re.findall(r"-?\d+", s))
def positive_ints(s: str) -> typing.List[int]:
  return lmap(int, re.findall(r"\d+", s))
def floats(s: str) -> typing.List[float]:
  return lmap(float, re.findall(r"-?\d+(?:\.\d+)?", s))
def positive_floats(s: str) -> typing.List[float]:
  return lmap(float, re.findall(r"\d+(?:\.\d+)?", s))
def words(s: str) -> typing.List[str]:
  return re.findall(r"[a-zA-Z]+", s)
def alphabetLower():
  return list(string.ascii_letters[:26])
def alphabetUpper():
  return list(string.ascii_letters[26:])
def alphabet():
  return list(string.ascii_letters)

'''p and q are points with arbitrary dimensions (e.g. [2, 3, 1], [5, 6, 4])'''
def manhattan_distance(p, q):
  distance = 0
  for p_i,q_i in zip(p,q):
    distance += abs(p_i - q_i)
  return distance

class UnionFind:
  # n: int
  # parents: List[Optional[int]]
  # ranks: List[int]
  # num_sets: int

  def __init__(self, n: int) -> None:
    self.n = n
    self.parents = [None] * n
    self.ranks = [1] * n
    self.num_sets = n

  def find(self, i: int) -> int:
    p = self.parents[i]
    if p is None:
      return i
    p = self.find(p)
    self.parents[i] = p
    return p

  def in_same_set(self, i: int, j: int) -> bool:
    return self.find(i) == self.find(j)

  def merge(self, i: int, j: int) -> None:
    i = self.find(i)
    j = self.find(j)

    if i == j:
      return

    i_rank = self.ranks[i]
    j_rank = self.ranks[j]

    if i_rank < j_rank:
      self.parents[i] = j
    elif i_rank > j_rank:
      self.parents[j] = i
    else:
      self.parents[j] = i
      self.ranks[i] += 1
    self.num_sets -= 1
