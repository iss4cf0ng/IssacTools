def times_table():
    for i in range(1, 10):
        for j in range(1, 10):
            print('%1s x %1s = %2s' % (i, j, i * j), end='\t')
        print('')

times_table()