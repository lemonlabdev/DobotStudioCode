target = [[250,0], [275,0], [250,-22], [275,-22]]

targetZ = -120
dType.SetDeviceWithL(api, 1, 1)
dType.SetPTPLParamsEx(api,100,50,1)
dType.SetEndEffectorParamsEx(api, 59.7, 0, 0, 1)

for step in target:
  targetX = step[0]
  targetY = step[1]
  current_pose = dType.GetPose(api)
  dType.SetPTPWithLCmdEx(api, 1, current_pose[0], current_pose[1], current_pose[2], current_pose[3], 0, 1)
  dType.SetPTPCmdEx(api, 0, targetX,  targetY,  targetZ, 0, 1)
  dType.SetEndEffectorSuctionCupEx(api, 1, 1)
  dType.SetPTPCmdEx(api, 0, 250,  0,  0, 0, 1)
  current_pose = dType.GetPose(api)
  dType.SetPTPWithLCmdEx(api, 1, current_pose[0], current_pose[1], current_pose[2], current_pose[3], 1000, 1)
  current_pose = dType.GetPose(api)
  dType.SetPTPCmdEx(api, 4, (-90),  80,  (dType.GetPoseEx(api, 7)), current_pose[7], 1)
  dType.SetEndEffectorSuctionCupEx(api, 0, 1)
  dType.SetPTPCmdEx(api, 0, 250,  0,  50, 0, 1)