# ElectronicDataInterchange

# Transmission Structure

```
[ISA]-- Interchange ----------------------
:  [GS]-- Functional Group ---------------
:  :  [ST]-- Transaction Set -------------
:  :  :   ,-- Detail Segment------------.
:  :  :  |                               |
:  :  :  |    DataElement*DataElement    |
:  :  :  |                               |
:  :  :   `-- Detail Segment------------`
:  :  [SE]-- Transaction Set -------------
:  [GE]-- Functional Group ---------------
[IEA]-- Transmission Envelope ------------
 ```
