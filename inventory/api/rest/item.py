from typing import Any

from flask import jsonify, request
from flask_restful import Resource

from inventory.consts import db

from ..orm import Item, Type, Unit


class ItemRest(Resource):
    def get(self) -> Any:
        data = []
        for item in Item.query.all():
            data.append(item.to_json())

        return jsonify(data)

    def post(self) -> None:
        data = request.get_json() or {}
        items = []
        for raw_item in data:
            item = Item.query.filter_by(name=raw_item["name"]).first()
            if item:
                item.amount = raw_item["amount"]
            else:
                item = Item(
                    name=raw_item["name"],
                    amount=raw_item["amount"],
                    unit=Unit.query.filter_by(name=raw_item["unit"]).first(),
                    type=Type.query.filter_by(name=raw_item["type"]).first(),
                )
            items.append(item)

        db.session.add_all(items)
        db.session.commit()
