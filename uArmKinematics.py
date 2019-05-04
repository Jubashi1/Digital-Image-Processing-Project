##########
# Forward & Inverse Kinematics of the Robotic arm named "uArm"
##########

import numpy as np

#Links Lengthes
L1 = 60
L2 = 100
L3 = 5
L4 = 290
L5 = 300

#End Effector Home Position
PX = 305
PY = 0
PZ = 390

Pw = [[PX],
      [PY],
      [PZ]]

PHome = [[305],
         [0],
         [390]]

#Motors Values of the Robot
th1 = (np.arctan2(PY, PX))*(180/np.pi)
th3 = (np.arccos((PX**2+PZ**2-L4**2-L5**2)/(2*L4*L5)))*(180/np.pi)
th2 = (np.arcsin((L5*np.sin(th3))/(np.sqrt(PX**2+PZ**2)))+th1)*(180/np.pi)




#Orientation
R0_3 = [[1.0,0.0,0.0],
        [0.0,-1.0,0.0],
        [0.0,0.0,-1.0]]

invR0_3 = np.linalg.inv(R0_3)

