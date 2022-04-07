from typing import Any

from flask import jsonify, request
from flask_restful import Resource

from inventory.consts import db

from ..orm import Type


class TypeRest(Resource):
    def get(self) -> Any:
        data = []
        for item in Type.query.all():
            data.append(item.to_json())

        return jsonify(data)

    def post(self) -> None:
        data = request.get_json() or {}
        items = []
        for raw_item in data:
            if Type.query.filter_by(name=raw_item["name"]).first():
                continue

            item = Type(name=raw_item["name"])
            items.append(item)

        db.session.add_all(items)
        db.session.commit()
