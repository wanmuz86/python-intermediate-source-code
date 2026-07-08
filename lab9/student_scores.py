from score_list import ScoreList

#Sepcial container class that save score of a student
class StudentScores:

    def __init__(self, name, scores):
        self.name = name
        self.scores = ScoreList(scores)

    def average(self):
        if len(self.scores) == 0:
            return 0.0
        # Double check with slide we can use sum? - __iter__
        return sum(self.scores) / len(self.scores)

#eq and lt will later unlock sorting and searching
# rosScores =. [80,90,100]
# alysiousScore = [90,100,80]
    def __eq__(self, other): # to use ==
        if not isinstance(other, StudentScores):
            return NotImplemented # cannot use to compare with the instance
        return self.average() == other.average()
    
    def __lt__(self, other):
        if not isinstance(other, StudentScores):
            return NotImplemented
        return self.average() < other.average() 
        # TRUE if my average is smaller than the other average

    # :.2f -> 2 decimal point
    def __repr__(self): #Developer debugging
        return f"StudentScores(name='{self.name}',avg={self.average():.2f} )"

    
    def __contains__(self,value):
        return value in self.scores

    def top(self, n=1):
        if (n<= 0):
            raise ValueError("n must be positive")
        return f"{self.name}, Top scores :{sorted(self.scores, reverse=True)[:n]}"