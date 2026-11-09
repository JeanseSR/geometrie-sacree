import FreeCAD as App
import Part

doc = App.newDocument('FleurDeVieGravure')

# ================================================
# PLAQUE
# ================================================

plaque = Part.makeBox(70, 70, 2, App.Vector(-35.0, -35.0, 0))

# ================================================
# VOLUMES DE GRAVURE
# ================================================

outils = []

# Couronne 1
centre_0 = App.Vector(-26.331830477908024, 0.0, 1)
exterieur_0 = Part.makeCylinder(4.668169522091975, 1, centre_0)
interieur_0 = Part.makeCylinder(4.109107303877367, 1, centre_0)
anneau_0 = exterieur_0.cut(interieur_0)
outils.append(anneau_0)

# Couronne 2
centre_1 = App.Vector(-24.13751127141569, 3.800672353668947, 1)
exterieur_1 = Part.makeCylinder(4.668169522091975, 1, centre_1)
interieur_1 = Part.makeCylinder(4.109107303877367, 1, centre_1)
anneau_1 = exterieur_1.cut(interieur_1)
outils.append(anneau_1)

# Couronne 3
centre_2 = App.Vector(-21.943192064923355, 7.601344707337894, 1)
exterieur_2 = Part.makeCylinder(4.668169522091975, 1, centre_2)
interieur_2 = Part.makeCylinder(4.109107303877367, 1, centre_2)
anneau_2 = exterieur_2.cut(interieur_2)
outils.append(anneau_2)

# Couronne 4
centre_3 = App.Vector(-19.74887285843102, 11.402017061006845, 1)
exterieur_3 = Part.makeCylinder(4.668169522091975, 1, centre_3)
interieur_3 = Part.makeCylinder(4.109107303877367, 1, centre_3)
anneau_3 = exterieur_3.cut(interieur_3)
outils.append(anneau_3)

# Couronne 5
centre_4 = App.Vector(-17.554553651938683, 15.202689414675788, 1)
exterieur_4 = Part.makeCylinder(4.668169522091975, 1, centre_4)
interieur_4 = Part.makeCylinder(4.109107303877367, 1, centre_4)
anneau_4 = exterieur_4.cut(interieur_4)
outils.append(anneau_4)

# Couronne 6
centre_5 = App.Vector(-15.360234445446348, 19.003361768344735, 1)
exterieur_5 = Part.makeCylinder(4.668169522091975, 1, centre_5)
interieur_5 = Part.makeCylinder(4.109107303877367, 1, centre_5)
anneau_5 = exterieur_5.cut(interieur_5)
outils.append(anneau_5)

# Couronne 7
centre_6 = App.Vector(-13.165915238954012, 22.80403412201369, 1)
exterieur_6 = Part.makeCylinder(4.668169522091975, 1, centre_6)
interieur_6 = Part.makeCylinder(4.109107303877367, 1, centre_6)
anneau_6 = exterieur_6.cut(interieur_6)
outils.append(anneau_6)

# Couronne 8
centre_7 = App.Vector(-24.13751127141569, -3.800672353668947, 1)
exterieur_7 = Part.makeCylinder(4.668169522091975, 1, centre_7)
interieur_7 = Part.makeCylinder(4.109107303877367, 1, centre_7)
anneau_7 = exterieur_7.cut(interieur_7)
outils.append(anneau_7)

# Couronne 9
centre_8 = App.Vector(-21.943192064923355, 0.0, 1)
exterieur_8 = Part.makeCylinder(4.668169522091975, 1, centre_8)
interieur_8 = Part.makeCylinder(4.109107303877367, 1, centre_8)
anneau_8 = exterieur_8.cut(interieur_8)
outils.append(anneau_8)

# Couronne 10
centre_9 = App.Vector(-19.74887285843102, 3.800672353668947, 1)
exterieur_9 = Part.makeCylinder(4.668169522091975, 1, centre_9)
interieur_9 = Part.makeCylinder(4.109107303877367, 1, centre_9)
anneau_9 = exterieur_9.cut(interieur_9)
outils.append(anneau_9)

# Couronne 11
centre_10 = App.Vector(-17.554553651938683, 7.601344707337894, 1)
exterieur_10 = Part.makeCylinder(4.668169522091975, 1, centre_10)
interieur_10 = Part.makeCylinder(4.109107303877367, 1, centre_10)
anneau_10 = exterieur_10.cut(interieur_10)
outils.append(anneau_10)

# Couronne 12
centre_11 = App.Vector(-15.360234445446348, 11.402017061006845, 1)
exterieur_11 = Part.makeCylinder(4.668169522091975, 1, centre_11)
interieur_11 = Part.makeCylinder(4.109107303877367, 1, centre_11)
anneau_11 = exterieur_11.cut(interieur_11)
outils.append(anneau_11)

# Couronne 13
centre_12 = App.Vector(-13.165915238954012, 15.202689414675788, 1)
exterieur_12 = Part.makeCylinder(4.668169522091975, 1, centre_12)
interieur_12 = Part.makeCylinder(4.109107303877367, 1, centre_12)
anneau_12 = exterieur_12.cut(interieur_12)
outils.append(anneau_12)

# Couronne 14
centre_13 = App.Vector(-10.971596032461678, 19.003361768344735, 1)
exterieur_13 = Part.makeCylinder(4.668169522091975, 1, centre_13)
interieur_13 = Part.makeCylinder(4.109107303877367, 1, centre_13)
anneau_13 = exterieur_13.cut(interieur_13)
outils.append(anneau_13)

# Couronne 15
centre_14 = App.Vector(-8.777276825969341, 22.80403412201369, 1)
exterieur_14 = Part.makeCylinder(4.668169522091975, 1, centre_14)
interieur_14 = Part.makeCylinder(4.109107303877367, 1, centre_14)
anneau_14 = exterieur_14.cut(interieur_14)
outils.append(anneau_14)

# Couronne 16
centre_15 = App.Vector(-21.943192064923355, -7.601344707337894, 1)
exterieur_15 = Part.makeCylinder(4.668169522091975, 1, centre_15)
interieur_15 = Part.makeCylinder(4.109107303877367, 1, centre_15)
anneau_15 = exterieur_15.cut(interieur_15)
outils.append(anneau_15)

# Couronne 17
centre_16 = App.Vector(-19.74887285843102, -3.800672353668947, 1)
exterieur_16 = Part.makeCylinder(4.668169522091975, 1, centre_16)
interieur_16 = Part.makeCylinder(4.109107303877367, 1, centre_16)
anneau_16 = exterieur_16.cut(interieur_16)
outils.append(anneau_16)

# Couronne 18
centre_17 = App.Vector(-17.554553651938683, 0.0, 1)
exterieur_17 = Part.makeCylinder(4.668169522091975, 1, centre_17)
interieur_17 = Part.makeCylinder(4.109107303877367, 1, centre_17)
anneau_17 = exterieur_17.cut(interieur_17)
outils.append(anneau_17)

# Couronne 19
centre_18 = App.Vector(-15.360234445446348, 3.800672353668947, 1)
exterieur_18 = Part.makeCylinder(4.668169522091975, 1, centre_18)
interieur_18 = Part.makeCylinder(4.109107303877367, 1, centre_18)
anneau_18 = exterieur_18.cut(interieur_18)
outils.append(anneau_18)

# Couronne 20
centre_19 = App.Vector(-13.165915238954012, 7.601344707337894, 1)
exterieur_19 = Part.makeCylinder(4.668169522091975, 1, centre_19)
interieur_19 = Part.makeCylinder(4.109107303877367, 1, centre_19)
anneau_19 = exterieur_19.cut(interieur_19)
outils.append(anneau_19)

# Couronne 21
centre_20 = App.Vector(-10.971596032461678, 11.402017061006845, 1)
exterieur_20 = Part.makeCylinder(4.668169522091975, 1, centre_20)
interieur_20 = Part.makeCylinder(4.109107303877367, 1, centre_20)
anneau_20 = exterieur_20.cut(interieur_20)
outils.append(anneau_20)

# Couronne 22
centre_21 = App.Vector(-8.777276825969341, 15.202689414675788, 1)
exterieur_21 = Part.makeCylinder(4.668169522091975, 1, centre_21)
interieur_21 = Part.makeCylinder(4.109107303877367, 1, centre_21)
anneau_21 = exterieur_21.cut(interieur_21)
outils.append(anneau_21)

# Couronne 23
centre_22 = App.Vector(-6.582957619477006, 19.003361768344735, 1)
exterieur_22 = Part.makeCylinder(4.668169522091975, 1, centre_22)
interieur_22 = Part.makeCylinder(4.109107303877367, 1, centre_22)
anneau_22 = exterieur_22.cut(interieur_22)
outils.append(anneau_22)

# Couronne 24
centre_23 = App.Vector(-4.388638412984671, 22.80403412201369, 1)
exterieur_23 = Part.makeCylinder(4.668169522091975, 1, centre_23)
interieur_23 = Part.makeCylinder(4.109107303877367, 1, centre_23)
anneau_23 = exterieur_23.cut(interieur_23)
outils.append(anneau_23)

# Couronne 25
centre_24 = App.Vector(-19.74887285843102, -11.402017061006845, 1)
exterieur_24 = Part.makeCylinder(4.668169522091975, 1, centre_24)
interieur_24 = Part.makeCylinder(4.109107303877367, 1, centre_24)
anneau_24 = exterieur_24.cut(interieur_24)
outils.append(anneau_24)

# Couronne 26
centre_25 = App.Vector(-17.554553651938683, -7.601344707337894, 1)
exterieur_25 = Part.makeCylinder(4.668169522091975, 1, centre_25)
interieur_25 = Part.makeCylinder(4.109107303877367, 1, centre_25)
anneau_25 = exterieur_25.cut(interieur_25)
outils.append(anneau_25)

# Couronne 27
centre_26 = App.Vector(-15.360234445446348, -3.800672353668947, 1)
exterieur_26 = Part.makeCylinder(4.668169522091975, 1, centre_26)
interieur_26 = Part.makeCylinder(4.109107303877367, 1, centre_26)
anneau_26 = exterieur_26.cut(interieur_26)
outils.append(anneau_26)

# Couronne 28
centre_27 = App.Vector(-13.165915238954012, 0.0, 1)
exterieur_27 = Part.makeCylinder(4.668169522091975, 1, centre_27)
interieur_27 = Part.makeCylinder(4.109107303877367, 1, centre_27)
anneau_27 = exterieur_27.cut(interieur_27)
outils.append(anneau_27)

# Couronne 29
centre_28 = App.Vector(-10.971596032461678, 3.800672353668947, 1)
exterieur_28 = Part.makeCylinder(4.668169522091975, 1, centre_28)
interieur_28 = Part.makeCylinder(4.109107303877367, 1, centre_28)
anneau_28 = exterieur_28.cut(interieur_28)
outils.append(anneau_28)

# Couronne 30
centre_29 = App.Vector(-8.777276825969341, 7.601344707337894, 1)
exterieur_29 = Part.makeCylinder(4.668169522091975, 1, centre_29)
interieur_29 = Part.makeCylinder(4.109107303877367, 1, centre_29)
anneau_29 = exterieur_29.cut(interieur_29)
outils.append(anneau_29)

# Couronne 31
centre_30 = App.Vector(-6.582957619477006, 11.402017061006845, 1)
exterieur_30 = Part.makeCylinder(4.668169522091975, 1, centre_30)
interieur_30 = Part.makeCylinder(4.109107303877367, 1, centre_30)
anneau_30 = exterieur_30.cut(interieur_30)
outils.append(anneau_30)

# Couronne 32
centre_31 = App.Vector(-4.388638412984671, 15.202689414675788, 1)
exterieur_31 = Part.makeCylinder(4.668169522091975, 1, centre_31)
interieur_31 = Part.makeCylinder(4.109107303877367, 1, centre_31)
anneau_31 = exterieur_31.cut(interieur_31)
outils.append(anneau_31)

# Couronne 33
centre_32 = App.Vector(-2.1943192064923354, 19.003361768344735, 1)
exterieur_32 = Part.makeCylinder(4.668169522091975, 1, centre_32)
interieur_32 = Part.makeCylinder(4.109107303877367, 1, centre_32)
anneau_32 = exterieur_32.cut(interieur_32)
outils.append(anneau_32)

# Couronne 34
centre_33 = App.Vector(0.0, 22.80403412201369, 1)
exterieur_33 = Part.makeCylinder(4.668169522091975, 1, centre_33)
interieur_33 = Part.makeCylinder(4.109107303877367, 1, centre_33)
anneau_33 = exterieur_33.cut(interieur_33)
outils.append(anneau_33)

# Couronne 35
centre_34 = App.Vector(-17.554553651938683, -15.202689414675788, 1)
exterieur_34 = Part.makeCylinder(4.668169522091975, 1, centre_34)
interieur_34 = Part.makeCylinder(4.109107303877367, 1, centre_34)
anneau_34 = exterieur_34.cut(interieur_34)
outils.append(anneau_34)

# Couronne 36
centre_35 = App.Vector(-15.360234445446348, -11.402017061006845, 1)
exterieur_35 = Part.makeCylinder(4.668169522091975, 1, centre_35)
interieur_35 = Part.makeCylinder(4.109107303877367, 1, centre_35)
anneau_35 = exterieur_35.cut(interieur_35)
outils.append(anneau_35)

# Couronne 37
centre_36 = App.Vector(-13.165915238954012, -7.601344707337894, 1)
exterieur_36 = Part.makeCylinder(4.668169522091975, 1, centre_36)
interieur_36 = Part.makeCylinder(4.109107303877367, 1, centre_36)
anneau_36 = exterieur_36.cut(interieur_36)
outils.append(anneau_36)

# Couronne 38
centre_37 = App.Vector(-10.971596032461678, -3.800672353668947, 1)
exterieur_37 = Part.makeCylinder(4.668169522091975, 1, centre_37)
interieur_37 = Part.makeCylinder(4.109107303877367, 1, centre_37)
anneau_37 = exterieur_37.cut(interieur_37)
outils.append(anneau_37)

# Couronne 39
centre_38 = App.Vector(-8.777276825969341, 0.0, 1)
exterieur_38 = Part.makeCylinder(4.668169522091975, 1, centre_38)
interieur_38 = Part.makeCylinder(4.109107303877367, 1, centre_38)
anneau_38 = exterieur_38.cut(interieur_38)
outils.append(anneau_38)

# Couronne 40
centre_39 = App.Vector(-6.582957619477006, 3.800672353668947, 1)
exterieur_39 = Part.makeCylinder(4.668169522091975, 1, centre_39)
interieur_39 = Part.makeCylinder(4.109107303877367, 1, centre_39)
anneau_39 = exterieur_39.cut(interieur_39)
outils.append(anneau_39)

# Couronne 41
centre_40 = App.Vector(-4.388638412984671, 7.601344707337894, 1)
exterieur_40 = Part.makeCylinder(4.668169522091975, 1, centre_40)
interieur_40 = Part.makeCylinder(4.109107303877367, 1, centre_40)
anneau_40 = exterieur_40.cut(interieur_40)
outils.append(anneau_40)

# Couronne 42
centre_41 = App.Vector(-2.1943192064923354, 11.402017061006845, 1)
exterieur_41 = Part.makeCylinder(4.668169522091975, 1, centre_41)
interieur_41 = Part.makeCylinder(4.109107303877367, 1, centre_41)
anneau_41 = exterieur_41.cut(interieur_41)
outils.append(anneau_41)

# Couronne 43
centre_42 = App.Vector(0.0, 15.202689414675788, 1)
exterieur_42 = Part.makeCylinder(4.668169522091975, 1, centre_42)
interieur_42 = Part.makeCylinder(4.109107303877367, 1, centre_42)
anneau_42 = exterieur_42.cut(interieur_42)
outils.append(anneau_42)

# Couronne 44
centre_43 = App.Vector(2.1943192064923354, 19.003361768344735, 1)
exterieur_43 = Part.makeCylinder(4.668169522091975, 1, centre_43)
interieur_43 = Part.makeCylinder(4.109107303877367, 1, centre_43)
anneau_43 = exterieur_43.cut(interieur_43)
outils.append(anneau_43)

# Couronne 45
centre_44 = App.Vector(4.388638412984671, 22.80403412201369, 1)
exterieur_44 = Part.makeCylinder(4.668169522091975, 1, centre_44)
interieur_44 = Part.makeCylinder(4.109107303877367, 1, centre_44)
anneau_44 = exterieur_44.cut(interieur_44)
outils.append(anneau_44)

# Couronne 46
centre_45 = App.Vector(-15.360234445446348, -19.003361768344735, 1)
exterieur_45 = Part.makeCylinder(4.668169522091975, 1, centre_45)
interieur_45 = Part.makeCylinder(4.109107303877367, 1, centre_45)
anneau_45 = exterieur_45.cut(interieur_45)
outils.append(anneau_45)

# Couronne 47
centre_46 = App.Vector(-13.165915238954012, -15.202689414675788, 1)
exterieur_46 = Part.makeCylinder(4.668169522091975, 1, centre_46)
interieur_46 = Part.makeCylinder(4.109107303877367, 1, centre_46)
anneau_46 = exterieur_46.cut(interieur_46)
outils.append(anneau_46)

# Couronne 48
centre_47 = App.Vector(-10.971596032461678, -11.402017061006845, 1)
exterieur_47 = Part.makeCylinder(4.668169522091975, 1, centre_47)
interieur_47 = Part.makeCylinder(4.109107303877367, 1, centre_47)
anneau_47 = exterieur_47.cut(interieur_47)
outils.append(anneau_47)

# Couronne 49
centre_48 = App.Vector(-8.777276825969341, -7.601344707337894, 1)
exterieur_48 = Part.makeCylinder(4.668169522091975, 1, centre_48)
interieur_48 = Part.makeCylinder(4.109107303877367, 1, centre_48)
anneau_48 = exterieur_48.cut(interieur_48)
outils.append(anneau_48)

# Couronne 50
centre_49 = App.Vector(-6.582957619477006, -3.800672353668947, 1)
exterieur_49 = Part.makeCylinder(4.668169522091975, 1, centre_49)
interieur_49 = Part.makeCylinder(4.109107303877367, 1, centre_49)
anneau_49 = exterieur_49.cut(interieur_49)
outils.append(anneau_49)

# Couronne 51
centre_50 = App.Vector(-4.388638412984671, 0.0, 1)
exterieur_50 = Part.makeCylinder(4.668169522091975, 1, centre_50)
interieur_50 = Part.makeCylinder(4.109107303877367, 1, centre_50)
anneau_50 = exterieur_50.cut(interieur_50)
outils.append(anneau_50)

# Couronne 52
centre_51 = App.Vector(-2.1943192064923354, 3.800672353668947, 1)
exterieur_51 = Part.makeCylinder(4.668169522091975, 1, centre_51)
interieur_51 = Part.makeCylinder(4.109107303877367, 1, centre_51)
anneau_51 = exterieur_51.cut(interieur_51)
outils.append(anneau_51)

# Couronne 53
centre_52 = App.Vector(0.0, 7.601344707337894, 1)
exterieur_52 = Part.makeCylinder(4.668169522091975, 1, centre_52)
interieur_52 = Part.makeCylinder(4.109107303877367, 1, centre_52)
anneau_52 = exterieur_52.cut(interieur_52)
outils.append(anneau_52)

# Couronne 54
centre_53 = App.Vector(2.1943192064923354, 11.402017061006845, 1)
exterieur_53 = Part.makeCylinder(4.668169522091975, 1, centre_53)
interieur_53 = Part.makeCylinder(4.109107303877367, 1, centre_53)
anneau_53 = exterieur_53.cut(interieur_53)
outils.append(anneau_53)

# Couronne 55
centre_54 = App.Vector(4.388638412984671, 15.202689414675788, 1)
exterieur_54 = Part.makeCylinder(4.668169522091975, 1, centre_54)
interieur_54 = Part.makeCylinder(4.109107303877367, 1, centre_54)
anneau_54 = exterieur_54.cut(interieur_54)
outils.append(anneau_54)

# Couronne 56
centre_55 = App.Vector(6.582957619477006, 19.003361768344735, 1)
exterieur_55 = Part.makeCylinder(4.668169522091975, 1, centre_55)
interieur_55 = Part.makeCylinder(4.109107303877367, 1, centre_55)
anneau_55 = exterieur_55.cut(interieur_55)
outils.append(anneau_55)

# Couronne 57
centre_56 = App.Vector(8.777276825969341, 22.80403412201369, 1)
exterieur_56 = Part.makeCylinder(4.668169522091975, 1, centre_56)
interieur_56 = Part.makeCylinder(4.109107303877367, 1, centre_56)
anneau_56 = exterieur_56.cut(interieur_56)
outils.append(anneau_56)

# Couronne 58
centre_57 = App.Vector(-13.165915238954012, -22.80403412201369, 1)
exterieur_57 = Part.makeCylinder(4.668169522091975, 1, centre_57)
interieur_57 = Part.makeCylinder(4.109107303877367, 1, centre_57)
anneau_57 = exterieur_57.cut(interieur_57)
outils.append(anneau_57)

# Couronne 59
centre_58 = App.Vector(-10.971596032461678, -19.003361768344735, 1)
exterieur_58 = Part.makeCylinder(4.668169522091975, 1, centre_58)
interieur_58 = Part.makeCylinder(4.109107303877367, 1, centre_58)
anneau_58 = exterieur_58.cut(interieur_58)
outils.append(anneau_58)

# Couronne 60
centre_59 = App.Vector(-8.777276825969341, -15.202689414675788, 1)
exterieur_59 = Part.makeCylinder(4.668169522091975, 1, centre_59)
interieur_59 = Part.makeCylinder(4.109107303877367, 1, centre_59)
anneau_59 = exterieur_59.cut(interieur_59)
outils.append(anneau_59)

# Couronne 61
centre_60 = App.Vector(-6.582957619477006, -11.402017061006845, 1)
exterieur_60 = Part.makeCylinder(4.668169522091975, 1, centre_60)
interieur_60 = Part.makeCylinder(4.109107303877367, 1, centre_60)
anneau_60 = exterieur_60.cut(interieur_60)
outils.append(anneau_60)

# Couronne 62
centre_61 = App.Vector(-4.388638412984671, -7.601344707337894, 1)
exterieur_61 = Part.makeCylinder(4.668169522091975, 1, centre_61)
interieur_61 = Part.makeCylinder(4.109107303877367, 1, centre_61)
anneau_61 = exterieur_61.cut(interieur_61)
outils.append(anneau_61)

# Couronne 63
centre_62 = App.Vector(-2.1943192064923354, -3.800672353668947, 1)
exterieur_62 = Part.makeCylinder(4.668169522091975, 1, centre_62)
interieur_62 = Part.makeCylinder(4.109107303877367, 1, centre_62)
anneau_62 = exterieur_62.cut(interieur_62)
outils.append(anneau_62)

# Couronne 64
centre_63 = App.Vector(0.0, 0.0, 1)
exterieur_63 = Part.makeCylinder(4.668169522091975, 1, centre_63)
interieur_63 = Part.makeCylinder(4.109107303877367, 1, centre_63)
anneau_63 = exterieur_63.cut(interieur_63)
outils.append(anneau_63)

# Couronne 65
centre_64 = App.Vector(2.1943192064923354, 3.800672353668947, 1)
exterieur_64 = Part.makeCylinder(4.668169522091975, 1, centre_64)
interieur_64 = Part.makeCylinder(4.109107303877367, 1, centre_64)
anneau_64 = exterieur_64.cut(interieur_64)
outils.append(anneau_64)

# Couronne 66
centre_65 = App.Vector(4.388638412984671, 7.601344707337894, 1)
exterieur_65 = Part.makeCylinder(4.668169522091975, 1, centre_65)
interieur_65 = Part.makeCylinder(4.109107303877367, 1, centre_65)
anneau_65 = exterieur_65.cut(interieur_65)
outils.append(anneau_65)

# Couronne 67
centre_66 = App.Vector(6.582957619477006, 11.402017061006845, 1)
exterieur_66 = Part.makeCylinder(4.668169522091975, 1, centre_66)
interieur_66 = Part.makeCylinder(4.109107303877367, 1, centre_66)
anneau_66 = exterieur_66.cut(interieur_66)
outils.append(anneau_66)

# Couronne 68
centre_67 = App.Vector(8.777276825969341, 15.202689414675788, 1)
exterieur_67 = Part.makeCylinder(4.668169522091975, 1, centre_67)
interieur_67 = Part.makeCylinder(4.109107303877367, 1, centre_67)
anneau_67 = exterieur_67.cut(interieur_67)
outils.append(anneau_67)

# Couronne 69
centre_68 = App.Vector(10.971596032461678, 19.003361768344735, 1)
exterieur_68 = Part.makeCylinder(4.668169522091975, 1, centre_68)
interieur_68 = Part.makeCylinder(4.109107303877367, 1, centre_68)
anneau_68 = exterieur_68.cut(interieur_68)
outils.append(anneau_68)

# Couronne 70
centre_69 = App.Vector(13.165915238954012, 22.80403412201369, 1)
exterieur_69 = Part.makeCylinder(4.668169522091975, 1, centre_69)
interieur_69 = Part.makeCylinder(4.109107303877367, 1, centre_69)
anneau_69 = exterieur_69.cut(interieur_69)
outils.append(anneau_69)

# Couronne 71
centre_70 = App.Vector(-8.777276825969341, -22.80403412201369, 1)
exterieur_70 = Part.makeCylinder(4.668169522091975, 1, centre_70)
interieur_70 = Part.makeCylinder(4.109107303877367, 1, centre_70)
anneau_70 = exterieur_70.cut(interieur_70)
outils.append(anneau_70)

# Couronne 72
centre_71 = App.Vector(-6.582957619477006, -19.003361768344735, 1)
exterieur_71 = Part.makeCylinder(4.668169522091975, 1, centre_71)
interieur_71 = Part.makeCylinder(4.109107303877367, 1, centre_71)
anneau_71 = exterieur_71.cut(interieur_71)
outils.append(anneau_71)

# Couronne 73
centre_72 = App.Vector(-4.388638412984671, -15.202689414675788, 1)
exterieur_72 = Part.makeCylinder(4.668169522091975, 1, centre_72)
interieur_72 = Part.makeCylinder(4.109107303877367, 1, centre_72)
anneau_72 = exterieur_72.cut(interieur_72)
outils.append(anneau_72)

# Couronne 74
centre_73 = App.Vector(-2.1943192064923354, -11.402017061006845, 1)
exterieur_73 = Part.makeCylinder(4.668169522091975, 1, centre_73)
interieur_73 = Part.makeCylinder(4.109107303877367, 1, centre_73)
anneau_73 = exterieur_73.cut(interieur_73)
outils.append(anneau_73)

# Couronne 75
centre_74 = App.Vector(0.0, -7.601344707337894, 1)
exterieur_74 = Part.makeCylinder(4.668169522091975, 1, centre_74)
interieur_74 = Part.makeCylinder(4.109107303877367, 1, centre_74)
anneau_74 = exterieur_74.cut(interieur_74)
outils.append(anneau_74)

# Couronne 76
centre_75 = App.Vector(2.1943192064923354, -3.800672353668947, 1)
exterieur_75 = Part.makeCylinder(4.668169522091975, 1, centre_75)
interieur_75 = Part.makeCylinder(4.109107303877367, 1, centre_75)
anneau_75 = exterieur_75.cut(interieur_75)
outils.append(anneau_75)

# Couronne 77
centre_76 = App.Vector(4.388638412984671, 0.0, 1)
exterieur_76 = Part.makeCylinder(4.668169522091975, 1, centre_76)
interieur_76 = Part.makeCylinder(4.109107303877367, 1, centre_76)
anneau_76 = exterieur_76.cut(interieur_76)
outils.append(anneau_76)

# Couronne 78
centre_77 = App.Vector(6.582957619477006, 3.800672353668947, 1)
exterieur_77 = Part.makeCylinder(4.668169522091975, 1, centre_77)
interieur_77 = Part.makeCylinder(4.109107303877367, 1, centre_77)
anneau_77 = exterieur_77.cut(interieur_77)
outils.append(anneau_77)

# Couronne 79
centre_78 = App.Vector(8.777276825969341, 7.601344707337894, 1)
exterieur_78 = Part.makeCylinder(4.668169522091975, 1, centre_78)
interieur_78 = Part.makeCylinder(4.109107303877367, 1, centre_78)
anneau_78 = exterieur_78.cut(interieur_78)
outils.append(anneau_78)

# Couronne 80
centre_79 = App.Vector(10.971596032461678, 11.402017061006845, 1)
exterieur_79 = Part.makeCylinder(4.668169522091975, 1, centre_79)
interieur_79 = Part.makeCylinder(4.109107303877367, 1, centre_79)
anneau_79 = exterieur_79.cut(interieur_79)
outils.append(anneau_79)

# Couronne 81
centre_80 = App.Vector(13.165915238954012, 15.202689414675788, 1)
exterieur_80 = Part.makeCylinder(4.668169522091975, 1, centre_80)
interieur_80 = Part.makeCylinder(4.109107303877367, 1, centre_80)
anneau_80 = exterieur_80.cut(interieur_80)
outils.append(anneau_80)

# Couronne 82
centre_81 = App.Vector(15.360234445446348, 19.003361768344735, 1)
exterieur_81 = Part.makeCylinder(4.668169522091975, 1, centre_81)
interieur_81 = Part.makeCylinder(4.109107303877367, 1, centre_81)
anneau_81 = exterieur_81.cut(interieur_81)
outils.append(anneau_81)

# Couronne 83
centre_82 = App.Vector(-4.388638412984671, -22.80403412201369, 1)
exterieur_82 = Part.makeCylinder(4.668169522091975, 1, centre_82)
interieur_82 = Part.makeCylinder(4.109107303877367, 1, centre_82)
anneau_82 = exterieur_82.cut(interieur_82)
outils.append(anneau_82)

# Couronne 84
centre_83 = App.Vector(-2.1943192064923354, -19.003361768344735, 1)
exterieur_83 = Part.makeCylinder(4.668169522091975, 1, centre_83)
interieur_83 = Part.makeCylinder(4.109107303877367, 1, centre_83)
anneau_83 = exterieur_83.cut(interieur_83)
outils.append(anneau_83)

# Couronne 85
centre_84 = App.Vector(0.0, -15.202689414675788, 1)
exterieur_84 = Part.makeCylinder(4.668169522091975, 1, centre_84)
interieur_84 = Part.makeCylinder(4.109107303877367, 1, centre_84)
anneau_84 = exterieur_84.cut(interieur_84)
outils.append(anneau_84)

# Couronne 86
centre_85 = App.Vector(2.1943192064923354, -11.402017061006845, 1)
exterieur_85 = Part.makeCylinder(4.668169522091975, 1, centre_85)
interieur_85 = Part.makeCylinder(4.109107303877367, 1, centre_85)
anneau_85 = exterieur_85.cut(interieur_85)
outils.append(anneau_85)

# Couronne 87
centre_86 = App.Vector(4.388638412984671, -7.601344707337894, 1)
exterieur_86 = Part.makeCylinder(4.668169522091975, 1, centre_86)
interieur_86 = Part.makeCylinder(4.109107303877367, 1, centre_86)
anneau_86 = exterieur_86.cut(interieur_86)
outils.append(anneau_86)

# Couronne 88
centre_87 = App.Vector(6.582957619477006, -3.800672353668947, 1)
exterieur_87 = Part.makeCylinder(4.668169522091975, 1, centre_87)
interieur_87 = Part.makeCylinder(4.109107303877367, 1, centre_87)
anneau_87 = exterieur_87.cut(interieur_87)
outils.append(anneau_87)

# Couronne 89
centre_88 = App.Vector(8.777276825969341, 0.0, 1)
exterieur_88 = Part.makeCylinder(4.668169522091975, 1, centre_88)
interieur_88 = Part.makeCylinder(4.109107303877367, 1, centre_88)
anneau_88 = exterieur_88.cut(interieur_88)
outils.append(anneau_88)

# Couronne 90
centre_89 = App.Vector(10.971596032461678, 3.800672353668947, 1)
exterieur_89 = Part.makeCylinder(4.668169522091975, 1, centre_89)
interieur_89 = Part.makeCylinder(4.109107303877367, 1, centre_89)
anneau_89 = exterieur_89.cut(interieur_89)
outils.append(anneau_89)

# Couronne 91
centre_90 = App.Vector(13.165915238954012, 7.601344707337894, 1)
exterieur_90 = Part.makeCylinder(4.668169522091975, 1, centre_90)
interieur_90 = Part.makeCylinder(4.109107303877367, 1, centre_90)
anneau_90 = exterieur_90.cut(interieur_90)
outils.append(anneau_90)

# Couronne 92
centre_91 = App.Vector(15.360234445446348, 11.402017061006845, 1)
exterieur_91 = Part.makeCylinder(4.668169522091975, 1, centre_91)
interieur_91 = Part.makeCylinder(4.109107303877367, 1, centre_91)
anneau_91 = exterieur_91.cut(interieur_91)
outils.append(anneau_91)

# Couronne 93
centre_92 = App.Vector(17.554553651938683, 15.202689414675788, 1)
exterieur_92 = Part.makeCylinder(4.668169522091975, 1, centre_92)
interieur_92 = Part.makeCylinder(4.109107303877367, 1, centre_92)
anneau_92 = exterieur_92.cut(interieur_92)
outils.append(anneau_92)

# Couronne 94
centre_93 = App.Vector(0.0, -22.80403412201369, 1)
exterieur_93 = Part.makeCylinder(4.668169522091975, 1, centre_93)
interieur_93 = Part.makeCylinder(4.109107303877367, 1, centre_93)
anneau_93 = exterieur_93.cut(interieur_93)
outils.append(anneau_93)

# Couronne 95
centre_94 = App.Vector(2.1943192064923354, -19.003361768344735, 1)
exterieur_94 = Part.makeCylinder(4.668169522091975, 1, centre_94)
interieur_94 = Part.makeCylinder(4.109107303877367, 1, centre_94)
anneau_94 = exterieur_94.cut(interieur_94)
outils.append(anneau_94)

# Couronne 96
centre_95 = App.Vector(4.388638412984671, -15.202689414675788, 1)
exterieur_95 = Part.makeCylinder(4.668169522091975, 1, centre_95)
interieur_95 = Part.makeCylinder(4.109107303877367, 1, centre_95)
anneau_95 = exterieur_95.cut(interieur_95)
outils.append(anneau_95)

# Couronne 97
centre_96 = App.Vector(6.582957619477006, -11.402017061006845, 1)
exterieur_96 = Part.makeCylinder(4.668169522091975, 1, centre_96)
interieur_96 = Part.makeCylinder(4.109107303877367, 1, centre_96)
anneau_96 = exterieur_96.cut(interieur_96)
outils.append(anneau_96)

# Couronne 98
centre_97 = App.Vector(8.777276825969341, -7.601344707337894, 1)
exterieur_97 = Part.makeCylinder(4.668169522091975, 1, centre_97)
interieur_97 = Part.makeCylinder(4.109107303877367, 1, centre_97)
anneau_97 = exterieur_97.cut(interieur_97)
outils.append(anneau_97)

# Couronne 99
centre_98 = App.Vector(10.971596032461678, -3.800672353668947, 1)
exterieur_98 = Part.makeCylinder(4.668169522091975, 1, centre_98)
interieur_98 = Part.makeCylinder(4.109107303877367, 1, centre_98)
anneau_98 = exterieur_98.cut(interieur_98)
outils.append(anneau_98)

# Couronne 100
centre_99 = App.Vector(13.165915238954012, 0.0, 1)
exterieur_99 = Part.makeCylinder(4.668169522091975, 1, centre_99)
interieur_99 = Part.makeCylinder(4.109107303877367, 1, centre_99)
anneau_99 = exterieur_99.cut(interieur_99)
outils.append(anneau_99)

# Couronne 101
centre_100 = App.Vector(15.360234445446348, 3.800672353668947, 1)
exterieur_100 = Part.makeCylinder(4.668169522091975, 1, centre_100)
interieur_100 = Part.makeCylinder(4.109107303877367, 1, centre_100)
anneau_100 = exterieur_100.cut(interieur_100)
outils.append(anneau_100)

# Couronne 102
centre_101 = App.Vector(17.554553651938683, 7.601344707337894, 1)
exterieur_101 = Part.makeCylinder(4.668169522091975, 1, centre_101)
interieur_101 = Part.makeCylinder(4.109107303877367, 1, centre_101)
anneau_101 = exterieur_101.cut(interieur_101)
outils.append(anneau_101)

# Couronne 103
centre_102 = App.Vector(19.74887285843102, 11.402017061006845, 1)
exterieur_102 = Part.makeCylinder(4.668169522091975, 1, centre_102)
interieur_102 = Part.makeCylinder(4.109107303877367, 1, centre_102)
anneau_102 = exterieur_102.cut(interieur_102)
outils.append(anneau_102)

# Couronne 104
centre_103 = App.Vector(4.388638412984671, -22.80403412201369, 1)
exterieur_103 = Part.makeCylinder(4.668169522091975, 1, centre_103)
interieur_103 = Part.makeCylinder(4.109107303877367, 1, centre_103)
anneau_103 = exterieur_103.cut(interieur_103)
outils.append(anneau_103)

# Couronne 105
centre_104 = App.Vector(6.582957619477006, -19.003361768344735, 1)
exterieur_104 = Part.makeCylinder(4.668169522091975, 1, centre_104)
interieur_104 = Part.makeCylinder(4.109107303877367, 1, centre_104)
anneau_104 = exterieur_104.cut(interieur_104)
outils.append(anneau_104)

# Couronne 106
centre_105 = App.Vector(8.777276825969341, -15.202689414675788, 1)
exterieur_105 = Part.makeCylinder(4.668169522091975, 1, centre_105)
interieur_105 = Part.makeCylinder(4.109107303877367, 1, centre_105)
anneau_105 = exterieur_105.cut(interieur_105)
outils.append(anneau_105)

# Couronne 107
centre_106 = App.Vector(10.971596032461678, -11.402017061006845, 1)
exterieur_106 = Part.makeCylinder(4.668169522091975, 1, centre_106)
interieur_106 = Part.makeCylinder(4.109107303877367, 1, centre_106)
anneau_106 = exterieur_106.cut(interieur_106)
outils.append(anneau_106)

# Couronne 108
centre_107 = App.Vector(13.165915238954012, -7.601344707337894, 1)
exterieur_107 = Part.makeCylinder(4.668169522091975, 1, centre_107)
interieur_107 = Part.makeCylinder(4.109107303877367, 1, centre_107)
anneau_107 = exterieur_107.cut(interieur_107)
outils.append(anneau_107)

# Couronne 109
centre_108 = App.Vector(15.360234445446348, -3.800672353668947, 1)
exterieur_108 = Part.makeCylinder(4.668169522091975, 1, centre_108)
interieur_108 = Part.makeCylinder(4.109107303877367, 1, centre_108)
anneau_108 = exterieur_108.cut(interieur_108)
outils.append(anneau_108)

# Couronne 110
centre_109 = App.Vector(17.554553651938683, 0.0, 1)
exterieur_109 = Part.makeCylinder(4.668169522091975, 1, centre_109)
interieur_109 = Part.makeCylinder(4.109107303877367, 1, centre_109)
anneau_109 = exterieur_109.cut(interieur_109)
outils.append(anneau_109)

# Couronne 111
centre_110 = App.Vector(19.74887285843102, 3.800672353668947, 1)
exterieur_110 = Part.makeCylinder(4.668169522091975, 1, centre_110)
interieur_110 = Part.makeCylinder(4.109107303877367, 1, centre_110)
anneau_110 = exterieur_110.cut(interieur_110)
outils.append(anneau_110)

# Couronne 112
centre_111 = App.Vector(21.943192064923355, 7.601344707337894, 1)
exterieur_111 = Part.makeCylinder(4.668169522091975, 1, centre_111)
interieur_111 = Part.makeCylinder(4.109107303877367, 1, centre_111)
anneau_111 = exterieur_111.cut(interieur_111)
outils.append(anneau_111)

# Couronne 113
centre_112 = App.Vector(8.777276825969341, -22.80403412201369, 1)
exterieur_112 = Part.makeCylinder(4.668169522091975, 1, centre_112)
interieur_112 = Part.makeCylinder(4.109107303877367, 1, centre_112)
anneau_112 = exterieur_112.cut(interieur_112)
outils.append(anneau_112)

# Couronne 114
centre_113 = App.Vector(10.971596032461678, -19.003361768344735, 1)
exterieur_113 = Part.makeCylinder(4.668169522091975, 1, centre_113)
interieur_113 = Part.makeCylinder(4.109107303877367, 1, centre_113)
anneau_113 = exterieur_113.cut(interieur_113)
outils.append(anneau_113)

# Couronne 115
centre_114 = App.Vector(13.165915238954012, -15.202689414675788, 1)
exterieur_114 = Part.makeCylinder(4.668169522091975, 1, centre_114)
interieur_114 = Part.makeCylinder(4.109107303877367, 1, centre_114)
anneau_114 = exterieur_114.cut(interieur_114)
outils.append(anneau_114)

# Couronne 116
centre_115 = App.Vector(15.360234445446348, -11.402017061006845, 1)
exterieur_115 = Part.makeCylinder(4.668169522091975, 1, centre_115)
interieur_115 = Part.makeCylinder(4.109107303877367, 1, centre_115)
anneau_115 = exterieur_115.cut(interieur_115)
outils.append(anneau_115)

# Couronne 117
centre_116 = App.Vector(17.554553651938683, -7.601344707337894, 1)
exterieur_116 = Part.makeCylinder(4.668169522091975, 1, centre_116)
interieur_116 = Part.makeCylinder(4.109107303877367, 1, centre_116)
anneau_116 = exterieur_116.cut(interieur_116)
outils.append(anneau_116)

# Couronne 118
centre_117 = App.Vector(19.74887285843102, -3.800672353668947, 1)
exterieur_117 = Part.makeCylinder(4.668169522091975, 1, centre_117)
interieur_117 = Part.makeCylinder(4.109107303877367, 1, centre_117)
anneau_117 = exterieur_117.cut(interieur_117)
outils.append(anneau_117)

# Couronne 119
centre_118 = App.Vector(21.943192064923355, 0.0, 1)
exterieur_118 = Part.makeCylinder(4.668169522091975, 1, centre_118)
interieur_118 = Part.makeCylinder(4.109107303877367, 1, centre_118)
anneau_118 = exterieur_118.cut(interieur_118)
outils.append(anneau_118)

# Couronne 120
centre_119 = App.Vector(24.13751127141569, 3.800672353668947, 1)
exterieur_119 = Part.makeCylinder(4.668169522091975, 1, centre_119)
interieur_119 = Part.makeCylinder(4.109107303877367, 1, centre_119)
anneau_119 = exterieur_119.cut(interieur_119)
outils.append(anneau_119)

# Couronne 121
centre_120 = App.Vector(13.165915238954012, -22.80403412201369, 1)
exterieur_120 = Part.makeCylinder(4.668169522091975, 1, centre_120)
interieur_120 = Part.makeCylinder(4.109107303877367, 1, centre_120)
anneau_120 = exterieur_120.cut(interieur_120)
outils.append(anneau_120)

# Couronne 122
centre_121 = App.Vector(15.360234445446348, -19.003361768344735, 1)
exterieur_121 = Part.makeCylinder(4.668169522091975, 1, centre_121)
interieur_121 = Part.makeCylinder(4.109107303877367, 1, centre_121)
anneau_121 = exterieur_121.cut(interieur_121)
outils.append(anneau_121)

# Couronne 123
centre_122 = App.Vector(17.554553651938683, -15.202689414675788, 1)
exterieur_122 = Part.makeCylinder(4.668169522091975, 1, centre_122)
interieur_122 = Part.makeCylinder(4.109107303877367, 1, centre_122)
anneau_122 = exterieur_122.cut(interieur_122)
outils.append(anneau_122)

# Couronne 124
centre_123 = App.Vector(19.74887285843102, -11.402017061006845, 1)
exterieur_123 = Part.makeCylinder(4.668169522091975, 1, centre_123)
interieur_123 = Part.makeCylinder(4.109107303877367, 1, centre_123)
anneau_123 = exterieur_123.cut(interieur_123)
outils.append(anneau_123)

# Couronne 125
centre_124 = App.Vector(21.943192064923355, -7.601344707337894, 1)
exterieur_124 = Part.makeCylinder(4.668169522091975, 1, centre_124)
interieur_124 = Part.makeCylinder(4.109107303877367, 1, centre_124)
anneau_124 = exterieur_124.cut(interieur_124)
outils.append(anneau_124)

# Couronne 126
centre_125 = App.Vector(24.13751127141569, -3.800672353668947, 1)
exterieur_125 = Part.makeCylinder(4.668169522091975, 1, centre_125)
interieur_125 = Part.makeCylinder(4.109107303877367, 1, centre_125)
anneau_125 = exterieur_125.cut(interieur_125)
outils.append(anneau_125)

# Couronne 127
centre_126 = App.Vector(26.331830477908024, 0.0, 1)
exterieur_126 = Part.makeCylinder(4.668169522091975, 1, centre_126)
interieur_126 = Part.makeCylinder(4.109107303877367, 1, centre_126)
anneau_126 = exterieur_126.cut(interieur_126)
outils.append(anneau_126)

# ================================================
# FUSION DES VOLUMES DE GRAVURE
# ================================================

outil_gravure = outils[0]

for outil in outils[1:]:
    outil_gravure = outil_gravure.fuse(outil)

# ================================================
# GRAVURE
# ================================================

resultat = plaque.cut(outil_gravure)

objet = doc.addObject('PartDesign::Feature', 'FleurDeVieGravee')
objet.Label = 'Fleur de Vie gravée'
objet.Shape = resultat

objet.addProperty('App::PropertyString', 'Fabrication', 'Paramètres')
objet.Fabrication = 'Fleur de Vie - gravure'
objet.addProperty('App::PropertyLength', 'ProfondeurGravure', 'Paramètres')
objet.ProfondeurGravure = 1

objet.addProperty('App::PropertyLength', 'LargeurPlaque', 'Paramètres')
objet.LargeurPlaque = 70

objet.addProperty('App::PropertyLength', 'HauteurPlaque', 'Paramètres')
objet.HauteurPlaque = 70

objet.addProperty('App::PropertyLength', 'EpaisseurPlaque', 'Paramètres')
objet.EpaisseurPlaque = 2

doc.recompute()
Gui.activeDocument().activeView().viewAxonometric()
Gui.activeDocument().activeView().fitAll()

print('Fleur de Vie gravée créée : OK')
