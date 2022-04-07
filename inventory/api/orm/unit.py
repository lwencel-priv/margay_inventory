from inventory.consts import db


class Unit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(length=50), unique=True)
    symbol = db.Column(db.String(length=10))

    def to_json(self) -> dict:
        return {
            "name": self.name,
            "symbol": self.symbol,
        }
