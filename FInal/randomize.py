import bge
import random
from bge import logic

cont=logic.getCurrentController()
owner=cont.owner
sen=cont.sensors['Delay']
act1=cont.actuators['type1']
act2=cont.actuators['type2']
act3=cont.actuators['type3']
random.seed()
rand=random.random()
print(rand)
if rand<= 0.5:
    cont.activate(act1)
elif rand <=0.8:
    cont.activate(act2)
else:
    cont.activate(act3)

