import sqlalchemy as sqla
import telebot


API_TOKEN = '7729336143:AAFs3fKMgC7PDEhmwSm1-ZChBdg9alfsHcs'

CONNECTION = "mysql+pymysql://is61-10:mtc20r0t@192.168.3.111/irg"

class Database:
    def __init__(self):
        self.engine = sqla.create_engine(CONNECTION)
        self.connection = self.engine.connect()
    
    def adresat(self):
        query = sqla.text("SELECT * FROM ADDRESAT")
        result = self.connection.execute(query).all()
        result_dict = []
        for r in result:
            result_dict.append(r._asdict())
            return result
    def mail(self,id:int):
        query = sqla.text("SELECT * FROM mail WHERE id = :id")


if __name__ == "__main__":
    db = Database()
    print(db.get_mail(2))
        