# Copyright 2013, Michael H. Goldwasser
#
# Developed for use with the book:
#
#    Data Structures and Algorithms in Python
#    Michael T. Goodrich, Roberto Tamassia, and Michael H. Goldwasser
#    John Wiley & Sons, 2013
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import math

def merge(src, result, start, inc):
  """Merge src[start:start+inc] and src[start+inc:start+2*inc] into result."""
  end1 = start+inc                        # boundary for run 1
  end2 = min(start+2*inc, len(src))       # boundary for run 2
  x, y, z = start, start+inc, start       # index into run 1, run 2, result
  while x < end1 and y < end2:
    if src[x] < src[y]:
      result[z] = src[x]
      x += 1
    else:
      result[z] = src[y]
      y += 1
    z += 1                                # increment z to reflect new result
  if x < end1:
    result[z:end2] = src[x:end1]          # copy remainder of run 1 to output
  elif y < end2:
    result[z:end2] = src[y:end2]          # copy remainder of run 2 to output

def merge_sort(S):
  """Sort the elements of Python list S using the merge-sort algorithm."""
  n = len(S)
  logn = math.ceil(math.log(n,2))
  src, dest = S, [None] * n               # make temporary storage for dest
  for i in (2**k for k in range(logn)):   # pass i creates all runs of length 2i
    for j in range(0, n, 2*i):            # each pass merges two length i runs
      merge(src, dest, j, i)
    src, dest = dest, src                 # reverse roles of lists
  if S is not src:
    S[0:n] = src[0:n]                     # additional copy to get results to S
