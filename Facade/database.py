from configparser import ConfigParser

class Database(object):
    @classmethod
    def getProperties(cls, db_name):
        file_name = db_name + '.ini'
        conf = ConfigParser()
        try:
            conf.read(file_name)
            return conf['MailAddress']
        except Exception:
            print('Warning : [{0}] is not found.'.format(file_name))
