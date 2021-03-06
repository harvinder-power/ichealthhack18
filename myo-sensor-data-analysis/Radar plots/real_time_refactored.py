import myo

class Listener(myo.DeviceListener):
    def on_paired(self, event):
        print("Hello, {}!".format(event.device_name))
        event.device.vibrate(myo.VibrationType.short)
    def on_unpaired(self, event):
        return False  # Stop the hub
    def on_orientation(self, event):
        orientation = event.orientation
        acceleration = event.acceleration
        gyroscope = event.gyroscope
        # ... do something with that
    def on_pose(self, pose):
        pass

if __name__ == '__main__':
  myo.init(sdk_path='/Users/harvinderpower/GitHub/ichealthhack18/myo-sensor-data-analysis/sdk/')
  hub = myo.Hub()
  listener = Listener()
  while hub.run(listener.on_event, 500):
    pass
