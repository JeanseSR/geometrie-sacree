import FreeCAD as App
import FreeCADGui as Gui
import Part
import Sketcher

doc = App.newDocument("GeometrieSacree")

sketch = doc.addObject(
    "Sketcher::SketchObject",
    "Esquisse"
)

sketch.addGeometry(
    Part.Circle(
        App.Vector(0.0, 0.0, 0),
        App.Vector(0,0,1),
        3.1361293283571428
    ),
    False
)

sketch.addGeometry(
    Part.Circle(
        App.Vector(-2.7159676679107143, 4.704193992535713, 0),
        App.Vector(0,0,1),
        3.1361293283571428
    ),
    False
)

sketch.addGeometry(
    Part.Circle(
        App.Vector(2.7159676679107143, 4.704193992535713, 0),
        App.Vector(0,0,1),
        3.1361293283571428
    ),
    False
)

sketch.addGeometry(
    Part.Circle(
        App.Vector(5.431935335821429, 0.0, 0),
        App.Vector(0,0,1),
        3.1361293283571428
    ),
    False
)

sketch.addGeometry(
    Part.Circle(
        App.Vector(2.7159676679107143, -4.704193992535713, 0),
        App.Vector(0,0,1),
        3.1361293283571428
    ),
    False
)

sketch.addGeometry(
    Part.Circle(
        App.Vector(-2.7159676679107143, -4.704193992535713, 0),
        App.Vector(0,0,1),
        3.1361293283571428
    ),
    False
)

sketch.addGeometry(
    Part.Circle(
        App.Vector(-5.431935335821429, 0.0, 0),
        App.Vector(0,0,1),
        3.1361293283571428
    ),
    False
)

sketch.addGeometry(
    Part.Circle(
        App.Vector(-5.431935335821429, 9.408387985071426, 0),
        App.Vector(0,0,1),
        3.1361293283571428
    ),
    False
)

sketch.addGeometry(
    Part.Circle(
        App.Vector(0.0, 9.408387985071426, 0),
        App.Vector(0,0,1),
        3.1361293283571428
    ),
    False
)

sketch.addGeometry(
    Part.Circle(
        App.Vector(5.431935335821429, 9.408387985071426, 0),
        App.Vector(0,0,1),
        3.1361293283571428
    ),
    False
)

sketch.addGeometry(
    Part.Circle(
        App.Vector(8.147903003732145, 4.704193992535713, 0),
        App.Vector(0,0,1),
        3.1361293283571428
    ),
    False
)

sketch.addGeometry(
    Part.Circle(
        App.Vector(10.863870671642857, 0.0, 0),
        App.Vector(0,0,1),
        3.1361293283571428
    ),
    False
)

sketch.addGeometry(
    Part.Circle(
        App.Vector(8.147903003732145, -4.704193992535713, 0),
        App.Vector(0,0,1),
        3.1361293283571428
    ),
    False
)

sketch.addGeometry(
    Part.Circle(
        App.Vector(5.431935335821429, -9.408387985071426, 0),
        App.Vector(0,0,1),
        3.1361293283571428
    ),
    False
)

sketch.addGeometry(
    Part.Circle(
        App.Vector(0.0, -9.408387985071426, 0),
        App.Vector(0,0,1),
        3.1361293283571428
    ),
    False
)

sketch.addGeometry(
    Part.Circle(
        App.Vector(-5.431935335821429, -9.408387985071426, 0),
        App.Vector(0,0,1),
        3.1361293283571428
    ),
    False
)

sketch.addGeometry(
    Part.Circle(
        App.Vector(-8.147903003732145, -4.704193992535713, 0),
        App.Vector(0,0,1),
        3.1361293283571428
    ),
    False
)

sketch.addGeometry(
    Part.Circle(
        App.Vector(-10.863870671642857, 0.0, 0),
        App.Vector(0,0,1),
        3.1361293283571428
    ),
    False
)

sketch.addGeometry(
    Part.Circle(
        App.Vector(-8.147903003732145, 4.704193992535713, 0),
        App.Vector(0,0,1),
        3.1361293283571428
    ),
    False
)


doc.recompute()
Gui.ActiveDocument.ActiveView.fitAll()
Gui.SendMsgToActiveView("ViewFit")
