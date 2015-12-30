
# http://www.cc.gatech.edu/~jarek/graphics/papers/04PolygonBooleansMargalit.pdf

polygonorientation = [




]


def polygon_operation(Oper, Reg, A, B, Atype, Btype, Out):

    def find_orientation(polygon):
        ...

    orientationA = find_orientation(A)
    orientationB = find_orientation(B)

    if polygonorientation[Atype][Btype][Oper] == 'same':
        if not (orientationA == orientationB):
            change_orientation(B)
    elif orientationA:
        ...
