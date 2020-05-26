# Triangle of pascal


def pascal(n):
    ancien_liste = [1]
    for j in range(n):
        # 6->5
        # col.     0,1
        # [1].    # pa=[1,1]
        for z in range(0, int(n - j)):
            print('  ', end='')
        print(ancien_liste, end='')
        print()
        print(' ', end='')  # .     colon .    0,1,2
        nouvelle_liste = ancien_liste + [1]  # nouvelle_liste=[1,1,1]
        for col in range(0, len(ancien_liste) - 1):  # 0->1
            nouvelle_liste[col + 1] = ancien_liste[col] + ancien_liste[col + 1]
        ancien_liste = nouvelle_liste


pascal(10)
