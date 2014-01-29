from random import randint


def solver(ar):
    return sum(ar[::2]) * ar[-1] if ar else 0

print(solver([0, 1, 2, 3, 4, 5]) == 30)
print(solver([1, 3, 5]) == 30)
print(solver([6]) == 36)
print(solver([]) == 0)

tests = []

for _ in range(20):
    t = [randint(-99, 99) for _ in range(randint(1, 20))]
    ans = solver(t)
    print('{{"input": {0},\n"answer": {1}\n}},\n'.format(t, ans))