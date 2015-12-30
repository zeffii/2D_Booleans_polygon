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

''' Table 2 '''

# fragmenttype [ polygonAtype, polygonBtype, oper, polygon]
fragmenttype



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


    def insertV(dsv, point, io_type):
        ''' 3rd param enum [inside, outside, boundary]
        inserts into the vertex ring, DSV, the point, with the type
        io_type.
        '''
        ...

    def insertE(fragment, reg):
        """ Inserts an edge frament into the edge fragments table, EF, if
        it is not already there. If regular output result polygons are
        required and non-boundary edge fragment is to be inserted, the
        procedure checks whether the same edge fragment with the opposite
        direction is already in EF, if So. it does not insert the
        edge-fragment and it deletes the existing edge fragment with
        the opposite direction from the edge fragments table
        """
        ...

    def deleteE(fragment):
        """ Deletes an edge fragment from edge fragments table """
        ...

    def search_nextE(point):
        """ Searches and returns from the edge fragments table an edge fragment
        whose first endpoint is point
        """
        ...

    def organizeE():
        """ organizes the edge fragments table to allow fast search
        and deletion operations """
        ...

    def find_orientation(polygon):
        """ returns 'clockwise' or 'counterclockwise'. CW / CCW 
        it finds the vertex with the minimum X value and compares the slopes
        of the two edges attached to this vertex in order to find the 
        orientation
        """
        ...

    def change_orientation(polygon):
        """ self explanatory, reverses vertices """
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
