# Calibration Pose
Calibration_X = 167
Calibration_Y = 244.3
Calibration_Z = -36

# Convayor Belt Pose
Place_X = 280
Place_Y = 17
Place_Z = 17
dType.SetEndEffectorParamsEx(api, 59.7, 0, 0, 1)
j = 0
k = 0

dType.SetPTPJointParamsEx(api,400,400,400,400,400,400,400,400,1)
dType.SetPTPCommonParamsEx(api,100,100,1)
dType.SetPTPJumpParamsEx(api,40,100,1)
dType.SetPTPCmdEx(api, 0, Calibration_X,  Calibration_Y,  Calibration_Z, 0, 1)
dType.SetEndEffectorSuctionCupEx(api, 0, 1)

STEP_PER_CRICLE = 360.0 / 1.8 * 10.0 * 16.0
MM_PER_CRICLE = 3.1415926535898 * 36.0
vel = float(0) * STEP_PER_CRICLE / MM_PER_CRICLE
dType.SetEMotorEx(api, 0, 0, int(vel), 1)

for count in range(9):
  dType.SetPTPCmdEx(api, 0, (Calibration_X - j),  (Calibration_Y - k),  (Calibration_Z - 10), 0, 1)
  dType.SetEndEffectorSuctionCupEx(api, 1, 1)
  dType.SetWAITCmdEx(api, 0.5, 1)
  dType.SetPTPCmdEx(api, 0, Place_X,  Place_Y,  Place_Z, 0, 1)
  dType.SetEndEffectorSuctionCupEx(api, 0, 1)
  dType.SetWAITCmdEx(api, 0.5, 1)
  j = j + 25
  if j == 75:
    k = k + 25
    j = 0
  dType.dSleep(9000)
dType.SetEndEffectorSuctionCupEx(api, 0, 1)
dType.SetPTPCmdEx(api, 0, Calibration_X,  Calibration_Y,  Calibration_Z, 0, 1)
