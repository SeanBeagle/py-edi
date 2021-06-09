class Segment:  # Information Unit
    """A segment is the intermediate unit of information in a transaction set.

    Segment consist of logically related data
    data_element in a defined sequence, with a data ele- ment separator preceding each data element and a segment terminator
    character following the last data element. segment have a predetermined segment identifier that comprises the first
    characters of the segment. When segment are combined to form a transaction set, their use in the transaction set is
    defined by a segment requirement designator and a segment sequence. Some segment may be repeated, and groups of
    segment may be repeated as loops.
    """