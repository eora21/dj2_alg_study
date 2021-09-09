def BFS(repeat=0, total_energy=0):
    if repeat == N - 2:
        global highest_energy
        if highest_energy < total_energy:
            highest_energy = total_energy
        return

    for i in range(1, len(marbles)-1):
        energy = marbles[i-1] * marbles[i+1]
        marble = marbles[i]
        del(marbles[i])
        BFS(repeat+1, total_energy+energy)
        marbles.insert(i, marble)

    return highest_energy


N = int(input())

marbles = list(map(int, input().split()))

highest_energy = 0
print(BFS())