import sqlalchemy as sqla

# Убедитесь, что у вас правильный формат строки подключения
CONNECTION = "mysql+pymysql://is61-10:mtc20r0t@192.168.3.111/irg"

class Database:
    def __init__(self):
        self.engine = sqla.create_engine(CONNECTION)
        self.connection = self.engine.connect()

    def get_znak(self):
        # Извлекаем данные из таблицы statia
        query = sqla.text("SELECT * FROM znak")
        result = self.connection.execute(query).all()
        result_dict = []
        for r in result:
            result_dict.append(r._asdict())
        return result_dict
    
    def get_statia(self,id):
        query = sqla.text("SELECT * FROM statia WHERE id = :id")
        query = query.bindparams(sqla.bindparam("id",id))
        result = self.connection.execute(query).fetchone()._asdict()
        return result


# Пример использования
if __name__ == "__main__":
    db = Database()