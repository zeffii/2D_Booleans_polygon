"""
30 Dec 2015.

code interpretation by Dealga McArdle of this paper.

  http://www.cc.gatech.edu/~jarek/graphics/papers/04PolygonBooleansMargalit.pdf

It's the first thing that came up after a 'polygon unions' Google search. This repo
is an attempt at getting that psuedo code into a working state. It might be over my
head but won't know until attempted.

"""


''' Table 1 '''

# 1 = island
# 0 = hole
SM = "same"
OP = "opposite"
polygonorientation = {
    (1, 1): {'AnB': SM, 'AuB': SM, 'A-B': OP, 'B-A': OP},
    (1, 0): {'AnB': OP, 'AuB': OP, 'A-B': SM, 'B-A': SM},
    (0, 1): {'AnB': OP, 'AuB': OP, 'A-B': SM, 'B-A': SM},
    (0, 0): {'AnB': SM, 'AuB': SM, 'A-B': OP, 'B-A': OP}
}


def polygon_operation(Oper, Reg, A, B, Atype, Btype, Out):

    def find_intersection(segment_one, segment_two, point):
        """
        original:
          return True if the two line segments intersect
          False otherwise. If intersection then point is given
          the coordinate
        interpretation:
          return [] if no intersection and [x, y] if there is one.
        """
        ...

    def inside_polygon(v, polygon):
        """
        finds and returns the following
        - whether the v is inside or outside the boundary of polygon
        - check for every edge of polygon if point on the edge
        - 1] and if not, whether the edge intersects with a ray that
          -  begins at the point v and is directed in the X-axis direction
        - 2] if point v is on the edge, the function returns 'boundary'
             If the edge intersects with the raw, except at the edge's
             lower endpoint, a counter is incremented.
        When all edges are checked, the procedure returns 'inside' if
        the counter is an odd number or 'outside' if the counter is even.

        """
        ...

    def change_orientation(polygon):
        ...

    def find_orientation(polygon):
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
        insertV(AV, v, inside_polyon(v, B))

    for v in B:
        insertV(BV, v, inside_polyon(v, A))

    ''' Find intersections '''
