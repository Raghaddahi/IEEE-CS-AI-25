n = int(input())
scores = list(map(int, input().split()))
unique_scores = sorted(set(scores), reverse=True)
runner_up = unique_scores[1]
print(runner_up)
