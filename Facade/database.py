from configparser import ConfigParser


class Database(object):
    """
    Attributes
    ----------
    self.file_name : str
        reading on DB file .init format init
    self.conf : Any
        instance of ConfigParser
    """
    @classmethod
    def get_properties(cls, db_name: str):
        file_name = db_name + '.init'
        conf = ConfigParser()
        try:
            conf.read(file_name)
            return conf['MailAddress']
        except Exception:
            print('Warning : [{0}] is not found.'.format(file_name))
