'''

Icarus Manager

Icarus Manager for Grasshopper is a python GUI application built using tkinter that helps
users of the Icarus Grasshopper codebase streamline and improve their coding process by
allowing them to quickly inject snippets of code directly into the Grasshopper python editor.

Make sure to read all notes in the end of the python file.

'''

# Import modules
import win32com.client as client
from tkinter import *
from tkinter import ttk
# import pyperclip

# Inject function: when called switches to the Grasshopper active window and injects the selected Icarus code
def inject(event, string):
    wsh.AppActivate("Grasshopper Python Script Editor")
    wsh.SendKeys(string)
    wsh.SendKeys("{ENTER}")
    # pyperclip.copy(string)

# Update scrollregion after starting 'mainloop' when all widgets are in canvas
def on_configure(event):
    canvas.configure(scrollregion=canvas.bbox('all'))

# Variables
wsh = client.Dispatch('WScript.Shell')
root = Tk()

# --- Create canvas with scrollbar ---

canvas = Canvas(root)
canvas.pack(side=LEFT, fill=Y)

scrollbar = Scrollbar(root, command=canvas.yview)
scrollbar.pack(side=RIGHT, fill='y')

canvas.configure(yscrollcommand = scrollbar.set, width = 430)

# Update scrollregion after starting 'mainloop'
# when all widgets are in canvas
canvas.bind('<Configure>', on_configure)

# --- put frame in canvas ---
frame = Frame(canvas)
canvas.create_window((0,0), window=frame)

# --- put frames in initial frame ---
frameParameters = Frame(frame)
frameMaths = Frame(frame)
frameSets = Frame(frame)
frameVector = Frame(frame)
frameCurve = Frame(frame)
frameSurface = Frame(frame)
frameIntersect = Frame(frame)
frameTransform = Frame(frame)


# Define geometry of window
root.geometry("460x500+300+300")

# Title of the window
root.title("Icarus Manager Grasshopper")

# --- add widgets in frame ---
'''
titleLbl = Label(root, text="Icarus Manager for Grasshopper", font="Myriad 13 bold")
titleLbl.grid(row = 0)
titleLbl.place(relx=0.5, rely = 0.03, anchor=CENTER)'''

''' Naming scheme for buttons: first three letters of 1st tier menu
+ first three letters of 2nd tier menu + etc + name of item'''

# Parameters section
Label(frameParameters, text="Parameters").grid(row=1, column=0, sticky=W)


Label(frameParameters, text="Geometry").grid(row=2, column=1, sticky=W)

ParGeoPoint = Button(frameParameters, text="Point")
ParGeoPoint.grid(row=3, column=2, sticky=W)
ParGeoPoint.bind("<Button-1>", lambda event: inject(event, "Point = ghc.ConstructPoint{(}x,y,z{)}"))


# Maths section
Label(frameMaths, text="Maths").grid(row=0, column=0, sticky=W)

Label(frameMaths, text="Domain").grid(row=2, column=1, sticky=W)

MatDomConstructDomain = Button(frameMaths, text="Construct Domain")
MatDomConstructDomain.grid(row=3, column=2, sticky=W)
MatDomConstructDomain.bind("<Button-1>", lambda event: inject(event, "Domain = ghc.ConstructDomain{(}number1, number2{)}"))

MatDomConstructDomain2 = Button(frameMaths, text="Construct Domain2")
MatDomConstructDomain2.grid(row=4, column=2, sticky=W)
MatDomConstructDomain2.bind("<Button-1>", lambda event: inject(event, "Domain = ghc.ConstructDomain2{(}pair1min, pair1max, pair2min, pair2max{)}"))

MatDomRemap = Button(frameMaths, text="Remap")
MatDomRemap.grid(row=5, column=2, sticky=W)
MatDomRemap.bind("<Button-1>", lambda event: inject(event, "RemappedNum = ghc.RemapNumbers{(}number, sourceDomain, targetDomain{)}.mapped{ENTER}ClippedNum = ghc.RemapNumbers{(}number, sourceDomain, targetDomain{)}.clipped"))


# Sets section
Label(frameSets, text="Sets").grid(row=0, column=0, sticky=W)

Label(frameSets, text="List").grid(row=2, column=1, sticky=W)

SetLisListItem = Button(frameSets, text="List Item")
SetLisListItem.grid(row=3, column=2, sticky=W)
SetLisListItem.bind("<Button-1>", lambda event: inject(event, "item = ghc.ListItem{(}list,index,wrap{)}"))

SetLisListLength = Button(frameSets, text="List Length")
SetLisListLength.grid(row=4, column=2, sticky=W)
SetLisListLength.bind("<Button-1>", lambda event: inject(event, "item = ghc.ListLength{(}list{)}"))

Label(frameSets, text="Sequence").grid(row=6, column=1, sticky=W)

SetLisSeqCullPattern = Button(frameSets, text="Cull Pattern")
SetLisSeqCullPattern.grid(row=7, column=2, sticky=W)
SetLisSeqCullPattern.bind("<Button-1>", lambda event: inject(event, "ListOut = ghc.CullPattern{(}listIn, pattern{)}"))

SetLisSequence = Button(frameSets, text="Sequence")
SetLisSequence.grid(row=8, column=2, sticky=W)
SetLisSequence.bind("<Button-1>", lambda event: inject(event, "SequenceOut = ghc.Sequence{(}length, characters, format{)}"))

SetLisSeries = Button(frameSets, text="Series")
SetLisSeries.grid(row=9, column=2, sticky=W)
SetLisSeries.bind("<Button-1>", lambda event: inject(event, "SeriesOut = ghc.Series{(}start, step, length{)}"))


# Vector section
Label(frameVector, text="Vector").grid(row=0, column=0, sticky=W)

Label(frameVector, text="Grid").grid(row=2, column=1, sticky=W)

VecGriRectangular = Button(frameVector, text="Rectangular")
VecGriRectangular.grid(row=3, column=2, sticky=W)
VecGriRectangular.bind("<Button-1>", lambda event: inject(event, "Cells = ghc.Rectangular{(}plane, sizeX, sizeY, cellsX, cellsY{)}.cells{ENTER}Points = ghc.Rectangular{(}plane, sizeX, sizeY, cellsX, cellsY{)}.points"))

Label(frameVector, text="Plane").grid(row=6, column=1, sticky=W)

VecPlaConstructPlane = Button(frameVector, text="Construct Plane")
VecPlaConstructPlane.grid(row=7, column=2, sticky=W)
VecPlaConstructPlane.bind("<Button-1>", lambda event: inject(event, "Plane = ghc.ConstructPlane{(}origin, xVector, yVector{)}"))

Label(frameVector, text="Geometry").grid(row=12, column=1, sticky=W)

VecPoiConstructPoint = Button(frameVector, text="Construct Point")
VecPoiConstructPoint.grid(row=13, column=2, sticky=W)
VecPoiConstructPoint.bind("<Button-1>", lambda event: inject(event, "Point = ghc.ConstructPoint{(}x,y,z{)}"))

VecPoiDistance = Button(frameVector, text="Distance")
VecPoiDistance.grid(row=14, column=2, sticky=W)
VecPoiDistance.bind("<Button-1>", lambda event: inject(event, "DistanceOut = ghc.Distance{(}pointA, pointB{)}"))

Label(frameVector, text="Vector").grid(row=18, column=1, sticky=W)

VecVecVectorXYZ = Button(frameVector, text="Vector XYZ")
VecVecVectorXYZ.grid(row=19, column=2, sticky=W)
VecVecVectorXYZ.bind("<Button-1>", lambda event: inject(event, "Vector = ghc.VectorXYZ{(}x,y,z{)}.vector{ENTER}VectorMagnitude = ghc.VectorLength{(}Vector{)}"))

VecVecVector2Points = Button(frameVector, text="Vector from 2 Points")
VecVecVector2Points.grid(row=20, column=2, sticky=W)
VecVecVector2Points.bind("<Button-1>", lambda event: inject(event, "Vector = ghc.Vector2Pt{(}ptA, ptB{)}.vector{ENTER}VectorMagnitude = ghc.VectorLength{(}Vector{)}"))


# Curve Section
Label(frameCurve, text="Curve").grid(row=0, column=0, sticky=W)

Label(frameCurve, text="Analysis").grid(row=2, column=1, sticky=W)

CurAnaEndPoint = Button(frameCurve, text="End Point")
CurAnaEndPoint.grid(row=3, column=2, sticky=W)
CurAnaEndPoint.bind("<Button-1>", lambda event: inject(event, "StartPoint = ghc.EndPoints{(}curve{)}.start{ENTER}EndPoint = ghc.EndPoints{(}curve{)}.end"))

CurAnaEvaluateCurve = Button(frameCurve, text="Evaluate Curve")
CurAnaEvaluateCurve.grid(row=4, column=2, sticky=W)
CurAnaEvaluateCurve.bind("<Button-1>", lambda event: inject(event, "Point = ghc.EvaluateCurve{(}curve, parameter{)}.point{ENTER}Tangent = ghc.EvaluateCurve{(}curve, parameter{)}.tangent{ENTER}Angle = ghc.EvaluateCurve{(}curve, parameter{)}.angle"))

Label(frameCurve, text="Division").grid(row=8, column=1, sticky=W)

CurDivDivideCurve = Button(frameCurve, text="Divide Curve")
CurDivDivideCurve.grid(row=9, column=2, sticky=W)
CurDivDivideCurve.bind("<Button-1>", lambda event: inject(event, "Points = ghc.DivideCurve{(}curve, segmentsNum, divideAtKinks{)}.points{ENTER}Tangents = ghc.DivideCurve{(}curve, segmentsNum, divideAtKinks{)}.tangents{ENTER}Parameters = ghc.DivideCurve{(}curve, segmentsNum, divideAtKinks{)}.parameters"))

CurDivContour = Button(frameCurve, text="Contour")
CurDivContour.grid(row=10, column=2, sticky=W)
CurDivContour.bind("<Button-1>", lambda event: inject(event, "Contours = ghc.Contour{(}curve, point, direction, distance{)}.contours{ENTER}Parameters = ghc.Contour{(}curve, point, direction, distance{)}.parameters"))

Label(frameCurve, text="Primitive").grid(row=16, column=1, sticky=W)

Label(frameCurve, text="Circle").grid(row=17, column=2, sticky=W)

CurPriCirCircleRadiusPlane = Button(frameCurve, text="Circle from Radius & Plane")
CurPriCirCircleRadiusPlane.grid(row=18, column=3, sticky=W)
CurPriCirCircleRadiusPlane.bind("<Button-1>", lambda event: inject(event, "Circle = ghc.Circle{(}Plane, Radius{)}"))

CurPriCirCircle3Points = Button(frameCurve, text="Circle from 3 Points")
CurPriCirCircle3Points.grid(row=19, column=3, sticky=W)
CurPriCirCircle3Points.bind("<Button-1>", lambda event: inject(event, "Circle = ghc.Circle3Pt{(}ptA, ptB, ptC{)}"))

CurPriCirCirclePointVectorRadius = Button(frameCurve, text="Circle from Point, Vector & Radius")
CurPriCirCirclePointVectorRadius.grid(row=20, column=3, sticky=W)
CurPriCirCirclePointVectorRadius.bind("<Button-1>", lambda event: inject(event, "Circle = ghc.CircleCNR{(}Center, Vector, Radius{)}"))

CurPriCirCirclePointList = Button(frameCurve, text="Circle from List of Points")
CurPriCirCirclePointList.grid(row=21, column=3, sticky=W)
CurPriCirCirclePointList.bind("<Button-1>", lambda event: inject(event, "Circle = ghc.CircleFit{(}points{)}"))

CurPriCirCircleTangent2Curves = Button(frameCurve, text="Circle Tangent to 2 Curves")
CurPriCirCircleTangent2Curves.grid(row=22, column=3, sticky=W)
CurPriCirCircleTangent2Curves.bind("<Button-1>", lambda event: inject(event, "Circle = ghc.CircleTanTan{(}CurveA, CurveB, Center{)}"))

CurPriCirCircleTangent3Curves = Button(frameCurve, text="Circle Tangent to 3 Curves")
CurPriCirCircleTangent3Curves.grid(row=23, column=3, sticky=W)
CurPriCirCircleTangent3Curves.bind("<Button-1>", lambda event: inject(event, "Circle = ghc.CircleTanTanTan{(}CurveA, CurveB, CurveC, Center{)}"))

Label(frameCurve, text="Arc").grid(row=30, column=2, sticky=W)

CurPriArcArcPlaneRadiusAngle = Button(frameCurve, text="Arc from Plane, Radius & Angle")
CurPriArcArcPlaneRadiusAngle.grid(row=31, column=3, sticky=W)
CurPriArcArcPlaneRadiusAngle.bind("<Button-1>", lambda event: inject(event, "AngleDomain = ghc.ConstructDomain{(}0, AngleDomain{)}{ENTER}Arc = ghc.Arc{(}Plane, Radius, Angle{)}"))

CurPriArcArcStartMidEndPoint = Button(frameCurve, text="Arc from Start, Mid & End Point")
CurPriArcArcStartMidEndPoint.grid(row=32, column=3, sticky=W)
CurPriArcArcStartMidEndPoint.bind("<Button-1>", lambda event: inject(event, "Arc = ghc.Arc3Pt{(}StartPt, InteriorPt, EndPt{)}.arc{ENTER}Plane = ghc.Arc3Pt{(}StartPt, InteriorPt, EndPt{)}.plane{ENTER}Radius = ghc.Arc3Pt{(}StartPt, InteriorPt, EndPt{)}.radius"))

CurPriArcArcStartEndPointTangentVector = Button(frameCurve, text="Arc from Start & End Point & Tangent Vector")
CurPriArcArcStartEndPointTangentVector.grid(row=33, column=3, sticky=W)
CurPriArcArcStartEndPointTangentVector.bind("<Button-1>", lambda event: inject(event, "Arc = ghc.ArcSED{(}StartPt, EndPt, Vector{)}.arc{ENTER}Plane = ghc.ArcSED{(}StartPt, EndPt, Vector{)}.plane{ENTER}Radius = ghc.ArcSED{(}StartPt, EndPt, Vector{)}.radius"))

Label(frameCurve, text="Spline").grid(row=40, column=1, sticky=W)

CurSplNurbsCurve = Button(frameCurve, text="Nurbs Curve")
CurSplNurbsCurve.grid(row=41, column=2, sticky=W)
CurSplNurbsCurve.bind("<Button-1>", lambda event: inject(event, "Curve = ghc.NurbsCurve{(}vertices, degree, periodic{)}.curve{ENTER}Length = ghc.NurbsCurve{(}vertices, degree, periodic{)}.length{ENTER}Domain = ghc.NurbsCurve{(}vertices, degree, periodic{)}.domain"))

CurSplInterpolate = Button(frameCurve, text="Interpolate")
CurSplInterpolate.grid(row=42, column=2, sticky=W)
CurSplInterpolate.bind("<Button-1>", lambda event: inject(event, "Curve = ghc.Interpolate{(}vertices, degrees, periodic, knotStyle{)}.curve{ENTER}Length = ghc.Interpolate{(}vertices, degrees, periodic, knotStyle{)}.length{ENTER}Domain = ghc.Interpolate{(}vertices, degrees, periodic, knotStyle{)}.domain"))

Label(frameCurve, text="Util").grid(row=45, column=1, sticky=W)

CurUtiExplode = Button(frameCurve, text="Explode")
CurUtiExplode.grid(row=46, column=2, sticky=W)
CurUtiExplode.bind("<Button-1>", lambda event: inject(event, "Segments = ghc.Explode{(}curve, recursive{)}.segments{ENTER}Vertices = ghc.Explode{(}curve, recursive{)}.vertices"))

CurUtiJoinCurves = Button(frameCurve, text="Join Curves")
CurUtiJoinCurves.grid(row=47, column=2, sticky=W)
CurUtiJoinCurves.bind("<Button-1>", lambda event: inject(event, "CurvesJoined = ghc.JoinCurves{(}curvesIn, keepDirection{)}"))


# Surface Section
Label(frameSurface, text="Surface").grid(row=0, column=0, sticky=W)

Label(frameSurface, text="Analysis").grid(row=2, column=1, sticky=W)

SurAnaDeconstructionBrep = Button(frameSurface, text="Deconstruction Brep")
SurAnaDeconstructionBrep.grid(row=3, column=2, sticky=W)
SurAnaDeconstructionBrep.bind("<Button-1>", lambda event: inject(event, "Faces = ghc.DeconstructBrep{(}brep{)}.faces{ENTER}Edges = ghc.DeconstructBrep{(}brep{)}.edges{ENTER}Vertices = ghc.DeconstructBrep{(}brep{)}.vertices"))

Label(frameSurface, text="Freeform").grid(row=8, column=1, sticky=W)

SurFre4PointSurface = Button(frameSurface, text="4Point Surface")
SurFre4PointSurface.grid(row=9, column=2, sticky=W)
SurFre4PointSurface.bind("<Button-1>", lambda event: inject(event, "pointList = [pointA, pointB, pointD, pointC]{ENTER}Surface = ghc.SurfaceFromPoints{(}pointList, 2, False{)}"))

SurFreEdgeSurface = Button(frameSurface, text="Edge Surface")
SurFreEdgeSurface.grid(row=10, column=2, sticky=W)
SurFreEdgeSurface.bind("<Button-1>", lambda event: inject(event, "Surface = ghc.EdgeSurface{(}curveA, curveB, curveC, curveD{)}"))

Label(frameSurface, text="Freeform").grid(row=16, column=1, sticky=W)

SurPriBoundingBox = Button(frameSurface, text="Bounding Box")
SurPriBoundingBox.grid(row=17, column=2, sticky=W)
SurPriBoundingBox.bind("<Button-1>", lambda event: inject(event, "BoxWorldCoord = ghc.BoundingBox{(}geometries, plane{)}.box{ENTER}BoxPlaneCoord = ghc.BoundingBox{(}geometries, plane{)}.box"))

SurPriSphere = Button(frameSurface, text="Sphere")
SurPriSphere.grid(row=18, column=2, sticky=W)
SurPriSphere.bind("<Button-1>", lambda event: inject(event, "SphereOut = ghc.Sphere{(}plane, radius{)}"))

Label(frameSurface, text="Util").grid(row=25, column=1, sticky=W)

SurUtiDivideSurface = Button(frameSurface, text="Divide Surface")
SurUtiDivideSurface.grid(row=26, column=2, sticky=W)
SurUtiDivideSurface.bind("<Button-1>", lambda event: inject(event, "Points = ghc.DivideSurface{(}surface, uAxisDiv, yAxisDiv{)}.points{ENTER}NormVec = ghc.DivideSurface{(}surface, uAxisDiv, yAxisDiv{)}.normals{ENTER}Coordinates = ghc.DivideSurface{(}surface, uAxisDiv, yAxisDiv{)}.parameters"))

SurUtiIsotrim = Button(frameSurface, text="Isotrim")
SurUtiIsotrim.grid(row=27, column=2, sticky=W)
SurUtiIsotrim.bind("<Button-1>", lambda event: inject(event, "SurfaceOut = ghc.Isotrim{(}surfaceIn, domain{)}"))


# Intersect Section
Label(frameIntersect, text="Intersect").grid(row=0, column=0, sticky=W)

Label(frameIntersect, text="Mathematical").grid(row=2, column=1, sticky=W)

IntMatCurveLine = Button(frameIntersect, text="Curve | Line")
IntMatCurveLine.grid(row=3, column=2, sticky=W)
IntMatCurveLine.bind("<Button-1>", lambda event: inject(event, "Points = ghc.CurveXLine{(}curve, line{)}.points{ENTER}Parameters = ghc.CurveXLine{(}curve, line{)}.params{ENTER}PointsNum = ghc.CurveXLine{(}curve, line{)}.count"))

Label(frameIntersect, text="Physical").grid(row=10, column=1, sticky=W)

IntPhyCurveCurve = Button(frameIntersect, text="Curve | Curve")
IntPhyCurveCurve.grid(row=11, column=2, sticky=W)
IntPhyCurveCurve.bind("<Button-1>", lambda event: inject(event, "Points = ghc.CurveXCurve{(}curveA, curveB{)}.points{ENTER}ParamsA = ghc.CurveXCurve{(}curveA, curveB{)}[1]{ENTER}ParamsB = ghc.CurveXCurve{(}curveA, curveB{)}[2]"))

IntPhyVolume = Button(frameIntersect, text="Volume")
IntPhyVolume.grid(row=12, column=2, sticky=W)
IntPhyVolume.bind("<Button-1>", lambda event: inject(event, "Volume = ghc.Volume{(}brep{)}.volume{ENTER}Centroid = ghc.Volume{(}brep{)}.centroid"))

# Transform Section
Label(frameTransform, text="Transform").grid(row=0, column=0, sticky=W)

Label(frameTransform, text="Affine").grid(row=2, column=1, sticky=W)

TraAffScale = Button(frameTransform, text="Scale")
TraAffScale.grid(row=3, column=2, sticky=W)
TraAffScale.bind("<Button-1>", lambda event: inject(event, "GeometryOut = ghc.Scale{(}geometryIn, center, scale{)}.geometry{ENTER}TransformData = ghc.Scale{(}geometryIn, center, scale{)}.transform"))

Label(frameTransform, text="Array").grid(row=10, column=1, sticky=W)

TraArrLinearArray = Button(frameTransform, text="Linear Array")
TraArrLinearArray.grid(row=11, column=2, sticky=W)
TraArrLinearArray.bind("<Button-1>", lambda event: inject(event, "GeometryOut = ghc.LinearArray{(}geometryIn, directionVec, numOfVecPar{)}.geometry{ENTER}TransformData = ghc.LinearArray{(}geometryIn, directionVec, numOfVecPar{)}.transform"))

Label(frameTransform, text="Euclidean").grid(row=18, column=1, sticky=W)

TraEucMove = Button(frameTransform, text="Move")
TraEucMove.grid(row=19, column=2, sticky=W)
TraEucMove.bind("<Button-1>", lambda event: inject(event, "GeometryOut = ghc.Move{(}geometryIn, motionVec{)}.geometry{ENTER}TransformData = ghc.Move{(}geometryIn, motionVec{)}.transform"))

TraEucOrient = Button(frameTransform, text="Orient")
TraEucOrient.grid(row=20, column=2, sticky=W)
TraEucOrient.bind("<Button-1>", lambda event: inject(event, "GeometryOut = ghc.Orient{(}geometryIn, source, target{)}.geometry{ENTER}TransformData = ghc.Orient{(}geometryIn, source, target{)}.transform"))

TraEucRotate3D = Button(frameTransform, text="Rotate 3D")
TraEucRotate3D.grid(row=21, column=2, sticky=W)
TraEucRotate3D.bind("<Button-1>", lambda event: inject(event, "GeometryOut = ghc.Rotate3D{(}geometryIn, angle, center, axis{)}.geometry{ENTER}TransformData = ghc.Rotate3D{(}geometryIn, angle, center, axis{)}.transform"))

Label(frameTransform, text="Morph").grid(row=30, column=1, sticky=W)

TraMorBoxMorph = Button(frameTransform, text="Box Morph")
TraMorBoxMorph.grid(row=31, column=2, sticky=W)
TraMorBoxMorph.bind("<Button-1>", lambda event: inject(event, "GeometryOut = ghc.BoxMorph{(}geometryIn, reference, target{)}"))

TraMorSurfaceBox = Button(frameTransform, text="Surface Box")
TraMorSurfaceBox.grid(row=32, column=2, sticky=W)
TraMorSurfaceBox.bind("<Button-1>", lambda event: inject(event, "Box = ghc.SurfaceBox{(}surface, domain, height{)}"))




# Place section frames inside main frame
frameParameters.grid(row=0, column=0, sticky=W, pady=4)
ttk.Separator(frame,orient=HORIZONTAL).grid(row =1, columnspan=500, sticky="ew")
frameMaths.grid(row=2, column=0, sticky=W, pady=4)
ttk.Separator(frame,orient=HORIZONTAL).grid(row =3, columnspan=500, sticky="ew")
frameSets.grid(row=4, column=0, sticky=W, pady=4)
ttk.Separator(frame,orient=HORIZONTAL).grid(row =5, columnspan=500, sticky="ew")
frameVector.grid(row=6, column=0, sticky=W, pady=4)
ttk.Separator(frame,orient=HORIZONTAL).grid(row =7, columnspan=500, sticky="ew")
frameCurve.grid(row=8, column=0, sticky=W, pady=4)
ttk.Separator(frame,orient=HORIZONTAL).grid(row =9, columnspan=500, sticky="ew")
frameSurface.grid(row=10, column=0, sticky=W, pady=4)
ttk.Separator(frame,orient=HORIZONTAL).grid(row =11, columnspan=500, sticky="ew")
frameIntersect.grid(row=12, column=0, sticky=W, pady=4)
ttk.Separator(frame,orient=HORIZONTAL).grid(row =13, columnspan=500, sticky="ew")
frameTransform.grid(row=14, column=0, sticky=W, pady=4)

# --- Start program ---
root.mainloop()

'''

Notes:

Note 1:
The plus sign (+), caret (^), percent sign (%), tilde (~), and parentheses
() have special meanings to SendKeys. To specify one of these characters,
enclose it within braces ({}). For example, to specify the plus sign, use
"{+}". To specify brace characters, use "{{}" and "{}}". Brackets ([ ]) have
no special meaning to SendKeys, but you must enclose them in braces

Note 2:
To avoid repetition in extended use of Icarus Manager for Grasshopper, each
time a module of code is injected, the import of the grasshopper library line
(import ghpythonlib.components as ghc) is omitted. Thus entering this line is
expected to be done manually from the user.

Note 3:
Uncomment line 17 and 24 (related to the pyperclip module) to make Icarus manager also
load the code snipets into the computer's clipboard manager.

Note 4:
Good resource on win32 SendKeys: https://win32com.goermezer.de/microsoft/windows/controlling-applications-via-sendkeys.html

'''
