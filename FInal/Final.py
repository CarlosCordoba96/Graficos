import bge
def move(cont):
    cube=cont.owner
    leftPlane = bge.logic.getCurrentScene().objects['Plane.001'].worldPosition.x
    rightPlane = bge.logic.getCurrentScene().objects['Plane.007'].worldPosition.x
    pos=cube.worldPosition.x
    prop=cube['move']
    if(prop=="right"):
        cube.applyMovement([0.1,0,0],False)
        if(pos>=rightPlane):
            cube['move']="left"
            cube.applyMovement([-0.1,0,0],False)
    else:
        cube.applyMovement([-0.1,0,0],False)
        if(pos<=leftPlane):
            cube['move']="right"
            cube.applyMovement([0.1,0,0],False)
