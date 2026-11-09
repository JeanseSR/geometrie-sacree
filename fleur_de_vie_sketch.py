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
        3.14
    ),
    False
)

sketch.addGeometry(
    Part.Circle(
        App.Vector(-2.719319767883137, 4.71, 0),
        App.Vector(0,0,1),
        3.14
    ),
    False
)

sketch.addGeometry(
    Part.Circle(
        App.Vector(2.719319767883137, 4.71, 0),
        App.Vector(0,0,1),
        3.14
    ),
    False
)

sketch.addGeometry(
    Part.Circle(
        App.Vector(5.438639535766274, 0.0, 0),
        App.Vector(0,0,1),
        3.14
    ),
    False
)

sketch.addGeometry(
    Part.Circle(
        App.Vector(2.719319767883137, -4.71, 0),
        App.Vector(0,0,1),
        3.14
    ),
    False
)

sketch.addGeometry(
    Part.Circle(
        App.Vector(-2.719319767883137, -4.71, 0),
        App.Vector(0,0,1),
        3.14
    ),
    False
)

sketch.addGeometry(
    Part.Circle(
        App.Vector(-5.438639535766274, 0.0, 0),
        App.Vector(0,0,1),
        3.14
    ),
    False
)

sketch.addGeometry(
    Part.Circle(
        App.Vector(-5.438639535766274, 9.42, 0),
        App.Vector(0,0,1),
        3.14
    ),
    False
)

sketch.addGeometry(
    Part.Circle(
        App.Vector(0.0, 9.42, 0),
        App.Vector(0,0,1),
        3.14
    ),
    False
)

sketch.addGeometry(
    Part.Circle(
        App.Vector(5.438639535766274, 9.42, 0),
        App.Vector(0,0,1),
        3.14
    ),
    False
)

sketch.addGeometry(
    Part.Circle(
        App.Vector(8.157959303649413, 4.71, 0),
        App.Vector(0,0,1),
        3.14
    ),
    False
)

sketch.addGeometry(
    Part.Circle(
        App.Vector(10.877279071532548, 0.0, 0),
        App.Vector(0,0,1),
        3.14
    ),
    False
)

sketch.addGeometry(
    Part.Circle(
        App.Vector(8.157959303649413, -4.71, 0),
        App.Vector(0,0,1),
        3.14
    ),
    False
)

sketch.addGeometry(
    Part.Circle(
        App.Vector(5.438639535766274, -9.42, 0),
        App.Vector(0,0,1),
        3.14
    ),
    False
)

sketch.addGeometry(
    Part.Circle(
        App.Vector(0.0, -9.42, 0),
        App.Vector(0,0,1),
        3.14
    ),
    False
)

sketch.addGeometry(
    Part.Circle(
        App.Vector(-5.438639535766274, -9.42, 0),
        App.Vector(0,0,1),
        3.14
    ),
    False
)

sketch.addGeometry(
    Part.Circle(
        App.Vector(-8.157959303649413, -4.71, 0),
        App.Vector(0,0,1),
        3.14
    ),
    False
)

sketch.addGeometry(
    Part.Circle(
        App.Vector(-10.877279071532548, 0.0, 0),
        App.Vector(0,0,1),
        3.14
    ),
    False
)

sketch.addGeometry(
    Part.Circle(
        App.Vector(-8.157959303649413, 4.71, 0),
        App.Vector(0,0,1),
        3.14
    ),
    False
)


doc.recompute()
Gui.ActiveDocument.ActiveView.fitAll()
Gui.SendMsgToActiveView("ViewFit")
