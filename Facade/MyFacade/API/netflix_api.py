class NetflixApi:
    @staticmethod
    def connect():
        return True

    @staticmethod
    def disconnect():
        return False

    @staticmethod
    def play(title):
        print('{} has started started playing on Netflix.'.format(title))
