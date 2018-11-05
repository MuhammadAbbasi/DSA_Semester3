from collections import *


class S(object):
    def __getitem__(self, item):
        raise IndexError

    def __len__(self):
        return 0

    def __contains__(self, item):
        return False

    def __iter__(self):
        return iter(())

    def __reversed__(self):
        return self

    def index(self, item):
        raise IndexError

    def count(self, item):
        return 0
    def __eq__(self,other):
        if len(self)!=len(other):
            return False
        for j in range(len(self)):
            if self[j]!=other[j]:
                return False
        return True
    def __lt__(self,other):
        if len(self)!=len(other):
            return False
        for j in range(len(self)):
            if self[j]>=other[j]:
                return False
        return True
    