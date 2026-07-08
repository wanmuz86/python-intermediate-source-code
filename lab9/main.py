from score_list import ScoreList
from student_scores import StudentScores

def main():
    scores = ScoreList([80,90,85])
    scores.add(70)

    print("Length: ",len(scores)) # 4
    print("Index 1 ", scores[1]) #90 
    print("Slide 0:2", scores[0:2]) #[80,90]

    print("Iterate")
    for s in scores:
        print("-",s)

    # Part 2: Comparison Test using StudentScores

    s1 = StudentScores("Aina", [38,85,95])
    s2 = StudentScores("Ali", [70,75,80])
    s3 = StudentScores("Mira",[95,85,90])

    print ("Equality check (Aina == Mira)", s1 == s3) # True
    print ("Less than check (Ali < Aina)", s2 < s1) # True

    students = [s1,s2,s3]
    print("Sorted students: ", sorted(students,reverse=True))
    
    print ("80 in scores? ", 80 in s1.scores) # False
    print ("80 in scores? ", 80 in s2.scores) # True
    print(any ( x < 40 for x in s1.scores)) # any is available because __iter__
    print(any ( x < 40 for x in s2.scores))

    print(s1.top(2))
    print(s2.top(2))
    print(s3.top(2))




if __name__ == "__main__":
    main()