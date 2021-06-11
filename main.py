from information_unit import TransmissionEnvelope
from data_dictionary import EDI810

if __name__ == '__main__':
    file = "tests/test_data/EDI-810.txt"
    te = TransmissionEnvelope(file)

    print(te)
    for fg in te.functional_groups:
        print(fg)
        for ts in fg.transaction_sets:
            print(ts)
            for segment in ts.segments:
                if segment.id not in EDI810.segments:
                    print(f'BAAAAAAAD Segment: {segment.id}')