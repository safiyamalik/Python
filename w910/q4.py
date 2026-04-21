votes = {}
n = int(input("Enter number of candidates: "))
for i in range(n):
    name = input("Enter candidate name: ")
    vote = int(input("Enter votes: "))
    votes[name] = vote
fewest_person = min(votes, key=votes.get)
print("Person with fewest votes:", fewest_person)
print("Votes:", votes[fewest_person])
