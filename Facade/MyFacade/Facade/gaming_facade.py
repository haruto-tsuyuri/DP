from Facade.MyFacade.API.camera_api import CameraApi
from Facade.MyFacade.API.playstation_api import PlaystationApi
from Facade.MyFacade.State.smart_home_state import SmartHomeState


class GamingFacade:

    def __init__(self):
        self.smart_home_state = SmartHomeState()
        self.camera_api = CameraApi()
        self.playstation_api = PlaystationApi()

    def start_gaming(self):
        self.smart_home_state.gaming_console_on = self.playstation_api.turn_on()

    def stop_gaming(self):
        self.smart_home_state.gaming_console_on = self.playstation_api.turn_off()

    def start_streaming(self):
        self.smart_home_state.streaming_camera_on = self.camera_api.turn_camera_on()
        self.start_gaming()

    def stop_streaming(self):
        self.smart_home_state.streaming_camera_on = self.camera_api.turn_camera_off()
        self.stop_gaming()
