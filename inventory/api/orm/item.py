from inventory.consts import db


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(length=50))
    amount = db.Column(db.Integer)
    unit_id = db.Column(db.Integer, db.ForeignKey("unit.id"), nullable=False)
    unit = db.relationship("Unit", backref=db.backref("inventory", lazy=True))
    type_id = db.Column(db.Integer, db.ForeignKey("type.id"), nullable=False)
    type = db.relationship("Type", backref=db.backref("items", lazy=True))

    def to_json(self) -> dict:
        return {
            "name": self.name,
            "amount": self.amount,
            "unit": self.unit.to_json(),
            "type": self.type.to_json(),
        }
