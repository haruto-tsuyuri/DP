from Facade.database import Database
from Facade.html_writer import HtmlWriter


class PageMaker(object):
    @classmethod
    def make_welcome_page(cls, mailaddr, file_name):
        try:
            prop = Database.get_properties('mail_data')
            user_name = prop[mailaddr]
            writer = HtmlWriter(open(file_name, 'w'))
            writer.title('Welcomes to {}\'s page!'.format(user_name))
            writer.paragraph('Well wait for your sending')
            writer.mail_to(mailaddr, user_name)
            writer.close()
            print('{} is created for {} ({})'.format(file_name, mailaddr, user_name))
        except Exception:
            print('# Failure occurred')
