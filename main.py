import Dao_email
import mail_extraction
import naver_extraction
import cryptography



def extraction(connection):
    mail_extraction.ham_extraction(connection)
    mail_extraction.spam_extraction(connection)
    #naver_extraction.ham_extraction(connection)
    #naver_extraction.spam_extraction(connection)


extraction(Dao_email.connection_sqlite)
#extraction(Dao_email.connection_mysql)