from typing import Any

from flask import jsonify, request
from flask_restful import Resource

from inventory.consts import db

from ..orm import Unit


class UnitRest(Resource):
    def get(self) -> Any:
        data = []
        for item in Unit.query.all():
            data.append(item.to_json())

        return jsonify(data)

    def post(self) -> None:
        data = request.get_json() or {}
        items = []
        for raw_item in data:
            if Unit.query.filter_by(name=raw_item["name"]).first():
                continue

            item = Unit(name=raw_item["name"], symbol=raw_item["symbol"])
            items.append(item)

        db.session.add_all(items)
        db.session.commit()
