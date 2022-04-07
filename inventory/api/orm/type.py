from inventory.consts import db


class Type(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(length=50), unique=True)

    def to_json(self) -> dict:
        return {
            "name": self.name,
        }
