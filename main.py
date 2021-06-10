from information_unit import TransactionSet

if __name__ == '__main__':
    file = "tests/test_data/EDI-810.txt"
    ts = TransactionSet(file)

    print(f'The Transaction Set contains {len(ts)} segments')
    for segment in ts.segments:
        print(segment)






