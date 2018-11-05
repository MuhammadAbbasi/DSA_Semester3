
class Progression:
    def __init__(self,start=0):
        self._current=start
    def advance(self):
        self._current+=1
    def __next__ (self):
        if self._current is None:
            raise StopIteration
        else:
            answer=self._current
            self.advance()
            return answer
    def __iter__(self):
        return self
    def print_progression(self,n):
         print(" ".join(str(next(self)) for i in range (n)))
class Fibonacci(Progression):
      def __init__(self,first=0,second=1):
            super().__init__(first)
            self.prev=second-first
    def advance(self):
          self._current,self.prev=self.prev,self._current+self.prev
if __name__== '__main__':
    Fibonacci(2,4).print_progression(8)          
