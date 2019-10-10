"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!
def main():
    MIN_SCORE = 0
    MAX_SCORE = 100
    score = float(input("Enter score > "))
    while score < MIN_SCORE or score > MAX_SCORE:
        print("invalid score, please enter inbetween range, ({} - {})".format(MIN_SCORE, MAX_SCORE))
        score = float(input("Enter score > "))
    score_determine = score_calc(score)
    print(score_determine)

def score_calc(score):
    if score >= 90:
        message = "Excellent score"
    elif score >= 50:
        message = "Passable score"
    elif score < 50:
        message = "bad score"
    return message

main()


