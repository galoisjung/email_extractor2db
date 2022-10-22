import Dao_email
import mail_extraction
import naver_extraction

#sqlite 사용할 경우

#naver
train_set, test_set = naver_extraction.making_doclist(0.8, Dao_email.connection_sqlite)

#gmail
train_set, test_set = mail_extraction.making_doclist(0.8, Dao_email.connection_sqlite)


#mysql 사용할 경우

#naver
train_set, test_set = naver_extraction.making_doclist(0.8, Dao_email.connection_mysql)

#gmail
train_set, test_set = mail_extraction.making_doclist(0.8, Dao_email.connection_mysql)