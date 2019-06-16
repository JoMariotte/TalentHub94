# Max 100000 boxes containing max 100000 numbered marbles, find the probability that two marbles chosen from each box
# have different numbers.
# For the test, there was no need to check if each input was valid

numBoxes = int(input())
mod = 1000000007
boxes = []
for i in range(numBoxes):
    boxes.append(int(input()))
boxes.sort()
proba = 1
for i in range(numBoxes):
    if boxes[i] - i <= 0:
        proba = 0
        break
    proba = proba * (boxes[i] - i) % mod
print(proba)