from flask import current_app as app
from flask_login import login_user, logout_user, current_user
from .. import login

class Cartesian:
    def __init__(self, uid, pid, quantity, price):
        self.uid = uid
        self.pid = pid
        self.priceatpurchase = price
        self.quantity = quantity

    
    @staticmethod
    def get(uid):
        rows = app.db.execute('''
SELECT Users.firstname, Products.pid, CARTS.quantity, CARTS.price_when_placed
FROM CARTS, Users, Products
WHERE uid = :uid AND CARTS.uid = Users.id AND CARTS.pid = Products.pid
''',
                              uid=uid)
        return [Cartesian(*row) for row in rows] if rows else None
    
    @staticmethod
    def getspecific(uid,pid):
        rows = app.db.execute('''
SELECT Users.firstname, Products.pid, CARTS.quantity, CARTS.price_when_placed
FROM CARTS, Users, Products
WHERE uid = :uid AND Products.pid = :pid AND CARTS.uid = Users.id AND CARTS.pid = Products.pid
''',
                              uid=uid,
                              pid = pid)
        return Cartesian(*(rows[0])) if rows else None


    @staticmethod
    def addToCart(uid, pid, quantity, price):
        try:
            rows = app.db.execute("""
INSERT INTO CARTS(uid, pid, quantity, price_when_placed)
VALUES(:uid, :pid, :quantity, :price)
RETURNING uid
""",
                                  uid=uid,
                                  pid=pid,
                                  quantity=quantity,
                                  price=price)
            id = rows[0][0]
            return 1
        except Exception as e:
            # likely email already in use; better error checking and
            # reporting needed
            return None

    @staticmethod
    def addToCartAgain(uid,pid,quantity,price):
        try:
            rows = app.db.execute("""
UPDATE Carts
SET quantity = quantity + :quantity, price_when_placed = price_when_placed + (:price)*(:quantity)
WHERE Carts.uid = :uid AND pid = :pid
            """, uid = uid,
                pid = pid,
                quantity=quantity,
                price=price)
            return 1
        except Exception as l:
            print(l)
            return 0

    @staticmethod
    def subFromCart(uid,pid,quantity,price):
        try:
            rows = app.db.execute("""
UPDATE Carts
SET quantity = quantity - :quantity, price_when_placed = price_when_placed - (:price)*(:quantity)
WHERE Carts.uid = :uid AND pid = :pid
            """, uid = uid,
                pid = pid,
                quantity=quantity,
                price=price)
            return 1
        except Exception as l:
            print(l)
            return 0


    @staticmethod
    def removeFromCart(pid,uid):
        try:
            rows = app.db.execute("""
    DELETE FROM Carts WHERE pid = :pid and carts.uid= :uid
            """,pid=pid,
                uid = current_user.id)
            return 1
        except Exception as l:
            print(l)
            return None

    @staticmethod
    def placeOrder(uid):
        try:
            rows = app.db.execute("""
    INSERT INTO OrderInformation(uid) 
    VALUES (:uid)
    RETURNING *
            """,uid=uid)
            for row in rows:
                print(row)
            id = rows[0][0]
            return id
        except Exception  as y:
            print(y)
            return None
    
    @staticmethod
    def addtoOrder(oid,pid,quantity,price_per_unit):
        try:
            rows = app.db.execute("""
    Insert Into ItemsInOrder(oid,pid,quantity,price_per_unit,fulfilled)
    VALUES (:oid,:pid,:quantity,:price_per_unit,'Not Fulfilled')
    returning oid
            """, oid = oid,
                 pid = pid,
                 quantity = quantity,
                 price_per_unit = price_per_unit)
            return 1
        except Exception as teey:
            print(teey)
            return None
    
    @staticmethod
    def getOrders(uid):
        try:
            rows = app.db.execute("""
        SELECT * FROM OrderInformation
        WHERE uid = :uid Order By oid DESC
            """,uid = uid)
            return [[row.oid,row.time_purchased] for row in rows] if rows else None
        except Exception as h:
            print("hello",h)
            return None

    @staticmethod
    def getOrderInfo(oid):
        try:
            rows = app.db.execute("""
            SELECT * FROM ItemsInOrder WHERE oid = :oid
            """,oid = oid)
            return [[row.pid, row.quantity, row.quantity,row.price_per_unit,row.fulfilled] for row in rows] if rows else None
        except Exception as gh:
            print("hello", gh)
            return 0
    
    @staticmethod
    def getOTime(oid):
        try:
            rows = app.db.execute("""
            SELECT time_purchased FROM OrderInformation WHERE oid = :oid
            """,oid = oid)
            return rows[0]
        except Exception as gh:
            print("hello", gh)
            return 0

