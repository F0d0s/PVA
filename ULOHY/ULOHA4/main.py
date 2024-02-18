import math

def find_equal_sums_intervals(sequence):
    if not sequence or len(sequence) > 2000:
        raise ValueError("Nespravny vstup.")

    intervals = []
    equal_sums_count = 0

    for i in range(len(sequence)):
        for j in range(i + 1, len(sequence) + 1):
            interval = sequence[i:j]
            if len(interval) >= 2:
                interval_sum = sum(interval)
                intervals.append((i, j - 1, interval_sum))

    for i in range(len(intervals)):
        for j in range(i + 1, len(intervals)):
            if intervals[i][2] == intervals[j][2]:
                equal_sums_count += 1

    return equal_sums_count

def main():
    try:
        sequence = list(map(int, input("Posloupnost: ").split()))
        result = find_equal_sums_intervals(sequence)
        print("Pocet dvojic:", result)
    except ValueError as e:
        print("Nespravny vstup.")

main()
