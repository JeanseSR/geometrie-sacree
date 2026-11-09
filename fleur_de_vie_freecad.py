import FreeCAD as App
import Draft

doc = App.newDocument("GeometrieSacree")

Draft.makeCircle(radius=50, placement=App.Placement(App.Vector(0.0, 0.0, 0), App.Rotation()))
Draft.makeCircle(radius=50, placement=App.Placement(App.Vector(-43.30127018922193, 75.0, 0), App.Rotation()))
Draft.makeCircle(radius=50, placement=App.Placement(App.Vector(43.30127018922193, 75.0, 0), App.Rotation()))
Draft.makeCircle(radius=50, placement=App.Placement(App.Vector(86.60254037844386, 0.0, 0), App.Rotation()))
Draft.makeCircle(radius=50, placement=App.Placement(App.Vector(43.30127018922193, -75.0, 0), App.Rotation()))
Draft.makeCircle(radius=50, placement=App.Placement(App.Vector(-43.30127018922193, -75.0, 0), App.Rotation()))
Draft.makeCircle(radius=50, placement=App.Placement(App.Vector(-86.60254037844386, 0.0, 0), App.Rotation()))
Draft.makeCircle(radius=50, placement=App.Placement(App.Vector(-86.60254037844386, 150.0, 0), App.Rotation()))
Draft.makeCircle(radius=50, placement=App.Placement(App.Vector(0.0, 150.0, 0), App.Rotation()))
Draft.makeCircle(radius=50, placement=App.Placement(App.Vector(86.60254037844386, 150.0, 0), App.Rotation()))
Draft.makeCircle(radius=50, placement=App.Placement(App.Vector(129.9038105676658, 75.0, 0), App.Rotation()))
Draft.makeCircle(radius=50, placement=App.Placement(App.Vector(173.20508075688772, 0.0, 0), App.Rotation()))
Draft.makeCircle(radius=50, placement=App.Placement(App.Vector(129.9038105676658, -75.0, 0), App.Rotation()))
Draft.makeCircle(radius=50, placement=App.Placement(App.Vector(86.60254037844386, -150.0, 0), App.Rotation()))
Draft.makeCircle(radius=50, placement=App.Placement(App.Vector(0.0, -150.0, 0), App.Rotation()))
Draft.makeCircle(radius=50, placement=App.Placement(App.Vector(-86.60254037844386, -150.0, 0), App.Rotation()))
Draft.makeCircle(radius=50, placement=App.Placement(App.Vector(-129.9038105676658, -75.0, 0), App.Rotation()))
Draft.makeCircle(radius=50, placement=App.Placement(App.Vector(-173.20508075688772, 0.0, 0), App.Rotation()))
Draft.makeCircle(radius=50, placement=App.Placement(App.Vector(-129.9038105676658, 75.0, 0), App.Rotation()))

doc.recompute()
App.ActiveDocument.recompute()
print("Figure créée.")