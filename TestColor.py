# Grab Point Pose
Grab_X = 273.2
Grab_Y = 90
Grab_Z = 7

# Stacking Count
RedCount = 0
GreenCount = 0
BlueCount = 0

# Staking Pose
REDSTACK = None
GREENSTACK = [[69, -267],[94, -267],[69, -242],[94, -242]]
BLUESTACK = None
TargetZ = -35

# Color Sensor Pose
ColorSensor_X = 195.8
ColorSensor_Y = 37
ColorSensor_Z = 36


def getcolor():
  dType.SetPTPCmdEx(api, 0, ColorSensor_X,  ColorSensor_Y,  ColorSensor_Z, 0, 1)
  dType.SetWAITCmdEx(api, 1, 1)
  color = dType.GetColorSensor(api)
  if color[0] == 1:
    print('Red')
  elif color[2] == 1:
    print('Blue')
  else:
    print('Green')
    TargetX = GREENSTACK[GreenCount][0]
    TargetY = GREENSTACK[GreenCount][1]
    dType.SetPTPCmdEx(api, 0, TargetX,  TargetY,  TargetZ, 0, 1)
  # SectionCup Off
  dType.SetEndEffectorSuctionCupEx(api, 0, 1)
  dType.SetWAITCmdEx(api, 1, 1)
  return color


dType.SetEndEffectorParamsEx(api, 59.7, 0, 0, 1)
dType.SetColorSensor(api, 1 ,1, 1)
dType.SetInfraredSensor(api, 1 ,2, 1)
dType.SetWAITCmdEx(api, 1, 1)
dType.SetPTPJointParamsEx(api,400,400,400,400,400,400,400,400,1)
dType.SetPTPCommonParamsEx(api,100,100,1)
dType.SetPTPJumpParamsEx(api,50,100,1)
current_pose = dType.GetPose(api)
dType.SetPTPCmdEx(api, 2, ColorSensor_X,  ColorSensor_Y,  ColorSensor_Z, current_pose[3], 1)
dType.SetEndEffectorSuctionCupEx(api, 0, 1)

# Start Conveyor Belt
STEP_PER_CRICLE = 360.0 / 1.8 * 10.0 * 16.0
MM_PER_CRICLE = 3.1415926535898 * 36.0
vel = float(50) * STEP_PER_CRICLE / MM_PER_CRICLE
dType.SetEMotorEx(api, 0, 1, int(vel), 1)

while True:
  if (dType.GetInfraredSensor(api, 2)[0]) == 1:
    vel = float(0) * STEP_PER_CRICLE / MM_PER_CRICLE # Set Velocity Zero
    dType.SetEMotorEx(api, 0, 0, int(vel), 1) # Stop Conveyor Belt
    
	# SuctionCup On
    dType.SetEndEffectorSuctionCupEx(api, 1, 1)
    dType.SetPTPCmdEx(api, 0, Grab_X,  Grab_Y,  Grab_Z, 0, 1)
    
    CountColor = getcolor()
    if CountColor[0] == 1:
      RedCount += 1
    elif CountColor[1] == 1:
      GreenCount += 1
    else:
      BlueCount += 1
    
    dType.SetPTPCmdEx(api, 0, Grab_X,  Grab_Y,  ColorSensor_Z, 0, 1)
	# Restart Conveyor Belt
    vel = float(50) * STEP_PER_CRICLE / MM_PER_CRICLE
    dType.SetEMotorEx(api, 0, 1, int(vel), 1)
