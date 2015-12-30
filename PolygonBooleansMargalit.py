"""
30 Dec 2015.

code interpretation by Dealga McArdle of this paper.

  http://www.cc.gatech.edu/~jarek/graphics/papers/04PolygonBooleansMargalit.pdf

It's the first thing that came up after a 'polygon unions' Google search. This repo
is an attempt at getting that psuedo code into a working state. It might be over my
head but won't know until attempted.

"""


# 1 = island
# 0 = hole
SM = "same"
OP = "opposite"
polygonorientation = {
    (1, 1): {'AnB': SM, 'AuB': SM, 'A-B': SM, 'B-A': OP},
    (1, 0): {'AnB': SM, 'AuB': OP, 'A-B': SM, 'B-A': SM},
    (0, 1): {'AnB': OP, 'AuB': SM, 'A-B': SM, 'B-A': SM},
    (0, 0): {'AnB': SM, 'AuB': SM, 'A-B': OP, 'B-A': SM}
}


def polygon_operation(Oper, Reg, A, B, Atype, Btype, Out):

    def change_orientation(polygon):
        ...

    def find_orientation(polygon):
        ...

    def insidepolygon(v, polygon):
        ...

    def insertV(v, polygon, inside_outside):
        ''' 3rd param is a bool '''
        ...

    ''' Find and set the orientations of the input polygons '''

    orientationA = find_orientation(A)
    orientationB = find_orientation(B)

    if polygonorientation[(Atype, Btype)][Oper] == 'same':
        if not (orientationA == orientationB):
            change_orientation(B)
    elif orientationA == orientationB:
        change_orientation(B)

    ''' Initiate the verts rings and classify the vertices '''

    for v in A:
        insertV(AV, v, insidepolyon(v, B))

    for v in B:
        insertV(BV, v, insidepolyon(v, A))

    ''' Find intersections '''
