from rest_framework.response import Response

import ezdxf
from ezdxf import units

# Create your views here.
# @api_view(['POST'])


def exportToDxfFile(request):

    model = []
    #
    nodeArr = model.getNodes()
    shapeArr = model.getShapes().shapes

    # Create a new DXF document.
    doc = ezdxf.new(dxfversion='R2010')
    doc = ezdxf.new()
    # Set millimeter as document/modelspace units
    doc.units = units.MM
    # which is a shortcut (including validation) for
    doc.header['$INSUNITS'] = units.MM
    # Create new table entries (layers, linetypes, text styles, ...).
    doc.layers.new('2', dxfattribs={'color': 2})
    doc.layers.new('1', dxfattribs={'color': 5})
    # DXF entities (LINE, TEXT, ...) reside in a layout (modelspace,
    # paperspace layout or block definition).
    msp = doc.modelspace()
    # Add entities to a layout by factory methods: layout.add_...()
    for attr, circleVertex in nodeArr.items():
        if not attr == "_n":
            msp.add_circle((circleVertex[0], circleVertex[1]), 1.5, dxfattribs={
                           'color': 4, 'layer': '2', 'thickness': 2})

    for attr, shapes in shapeArr.items():
        points = []
        for nodeKey in shapes:
            nodePoint = nodeArr[nodeKey]
            points.append((nodePoint[0], nodePoint[1]))
            print(model.getNodes().getNode(nodeKey))
        msp.add_polyline2d(points, close={bool: True}, dxfattribs={
                           'color': 20, 'layer': '1', 'thickness': 2})
        # msp.add_lwpolyline(points,close={bool:True},dxfattribs={'color': 20,'layer':'1','thickness':2})

    # Save DXF document.
    doc.saveas(request.data["path"])

    return Response({"msg": "success"})