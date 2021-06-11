from information_unit import TransactionSet
from data_dictionary import EDI810

if __name__ == '__main__':
    file = "tests/test_data/EDI-810.txt"
    ts = TransactionSet(file)

    print(f'The Transaction Set contains {len(ts)} segments')
    for segment in ts.segments:
        if segment.id not in EDI810.segments:
            raise Exception(f'BAAAAAAAD Segment: {segment.id}')

        if len(segment) > 2:
            print(f'Segment(id={segment.id}, DataElements={len(segment)})')
        else:
            print(f'Segment(id={segment.id}, DataElements={segment.data_elements})')
