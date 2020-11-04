from Facade.MyFacade.API.audio_api import AudioApi
from Facade.MyFacade.API.netflix_api import NetflixApi
from Facade.MyFacade.API.smart_home_api import SmartHomeApi
from Facade.MyFacade.API.tv_api import TvApi
from Facade.MyFacade.Facade.gaming_facade import GamingFacade
from Facade.MyFacade.State.smart_home_state import SmartHomeState


class SmartHomeFacade:

    def __init__(self):
        self.gaming_facade = GamingFacade()
        self.tv_api = TvApi()
        self.audio_api = AudioApi()
        self.netflix_api = NetflixApi()
        self.smart_home_api = SmartHomeApi()
        self.smart_home_state = SmartHomeState()

    def start_movie(self, movie_title: str) -> None:
        self.smart_home_state.lights_on = self.smart_home_api.turn_lights_off()
        self.smart_home_state.tv_on = self.tv_api.turn_on()
        self.smart_home_state.audio_system_on = self.audio_api.turn_speakers_on()
        self.smart_home_state.netflix_connected = self.netflix_api.connect()
        self.netflix_api.play(movie_title)

    def stop_movie(self) -> None:
        self.smart_home_state.netflix_connected = self.netflix_api.disconnect()
        self.smart_home_state.lights_on = self.smart_home_api.turn_lights_on()
        self.smart_home_state.tv_on = self.tv_api.turn_off()
        self.smart_home_state.audio_system_on = self.audio_api.turn_speakers_off()

    def start_gaming(self) -> None:
        self.smart_home_state.lights_on = self.smart_home_api.turn_lights_off()
        self.smart_home_state.tv_on = self.tv_api.turn_on()
        self.gaming_facade.start_gaming()

    def stop_gaming(self) -> None:
        self.gaming_facade.stop_gaming()
        self.smart_home_state.tv_on = self.tv_api.turn_off()
        self.smart_home_state.lights_on = self.smart_home_api.turn_lights_on()

    def start_streaming(self) -> None:
        self.smart_home_state.lights_on = self.smart_home_api.turn_lights_off()
        self.smart_home_state.tv_on = self.tv_api.turn_on()
        self.gaming_facade.start_streaming()

    def stop_streaming(self) -> None:
        self.gaming_facade.stop_streaming()
        self.smart_home_state.lights_on = self.smart_home_api.turn_lights_on()
        self.smart_home_state.tv_on = self.tv_api.turn_off()
