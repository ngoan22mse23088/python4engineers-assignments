import pymysql
from laptopseller import LaptopSeller


class Database:
    def connect(self):
        return pymysql.connect(host="localhost", user="root", password="12345678", database="laptop", charset='utf8mb4')

    def read(self, id):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            if id == None:
                cursor.execute(
                    "SELECT * FROM laptopbestseller order by Name asc")
            else:
                cursor.execute(
                    "SELECT * FROM laptopbestseller where id = %s order by Name asc", (id))

            return cursor.fetchall()
        except:
            return ()
        finally:
            con.close()

    def get_laptopbestsellers(self):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("SELECT Id, Name, Brand, OldPrice, NewPrice, PercentDiscount, BestSeller FROM laptopbestseller")
            data = cursor.fetchall()
            return [LaptopSeller(*laptopSeller) for laptopSeller in data]
        except:
            return ()
        finally:
            con.close()
        pass

    def get_laptopbestseller_by_id(self, id):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute(
                "SELECT Id, Name, Brand, OldPrice, NewPrice, PercentDiscount, BestSeller FROM laptopbestseller WHERE Id = %s", (id))
            laptop = cursor.fetchone()
            return LaptopSeller(laptop[0], laptop[1], laptop[2], laptop[3], laptop[4], laptop[5], laptop[6])
        except:
            return None
        finally:
            con.close()
        pass

    def insert(self, laptop):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("INSERT INTO laptopbestseller (Name, Brand, OldPrice, NewPrice, PercentDiscount, BestSeller) VALUES (%s, %s, %s, %s, %s, %s)",
                           (laptop.name, laptop.brand, laptop.old_price, laptop.new_price, laptop.percent_discount, laptop.best_seller))
            con.commit()

            return True
        except:
            con.rollback()

            return False
        finally:
            con.close()

    def update(self, laptop):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("UPDATE laptopbestseller SET Name=%s, Brand=%s, OldPrice=%s, NewPrice=%s, PercentDiscount=%s, BestSeller=%s WHERE Id=%s",
                           (laptop.name, laptop.brand, laptop.old_price, laptop.new_price, laptop.percent_discount, laptop.best_seller, laptop.id))
            con.commit()

            return True
        except:
            con.rollback()

            return False
        finally:
            con.close()

    def delete(self, id):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("DELETE FROM laptopbestseller WHERE Id = %s", (id,))
            con.commit()

            return True
        except:
            con.rollback()

            return False
        finally:
            con.close()
