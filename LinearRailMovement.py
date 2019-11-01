targetz = None


targetz = -120
dType.SetDeviceWithL(api, 1, 1)
main.process.emit("CheckLinearRail", "")
dType.SetPTPLParamsEx(api,100,50,1)
dType.SetEndEffectorParamsEx(api, 59.7, 0, 0, 1)
if True:
  current_pose = dType.GetPose(api)
  dType.SetPTPWithLCmdEx(api, 1, current_pose[0], current_pose[1], current_pose[2], current_pose[3], 0, 1)
  dType.SetPTPCmdEx(api, 0, 250,  0,  targetz, 0, 1)
  dType.SetEndEffectorSuctionCupEx(api, 1, 1)
  dType.SetPTPCmdEx(api, 0, 250,  0,  0, 0, 1)
  current_pose = dType.GetPose(api)
  dType.SetPTPWithLCmdEx(api, 1, current_pose[0], current_pose[1], current_pose[2], current_pose[3], 1000, 1)
  current_pose = dType.GetPose(api)
  dType.SetPTPCmdEx(api, 4, (-90),  80,  (dType.GetPoseEx(api, 7)), current_pose[7], 1)
  dType.SetEndEffectorSuctionCupEx(api, 0, 1)
  dType.SetPTPCmdEx(api, 0, 250,  0,  50, 0, 1)
else:
  pass
