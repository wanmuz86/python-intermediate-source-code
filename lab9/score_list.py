# Special collection that is used to score student marks
class ScoreList:

    def __init__(self, scores=None):
        # Initialize a list with the given scores or empty []
        self._scores = list(scores or [])

    # Add the score in the list
    def add(self, score):
        self._scores.append(score)

    # return how many scores are there
    def __len__(self):
        return len(self._scores)

    def __getitem__(self, index):
        return self._scores[index] # support indexing and slice

    def __iter__(self):
        return iter(self._scores) # to support for loop