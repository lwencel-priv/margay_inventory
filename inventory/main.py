from inventory.api.rest import ItemRest, TypeRest, UnitRest
from inventory.consts import api, app, db


def main() -> None:
    """Entry point."""
    db.create_all()
    api.add_resource(ItemRest, "/item")
    api.add_resource(UnitRest, "/unit")
    api.add_resource(TypeRest, "/type")
    app.run(debug=True, host="0.0.0.0")


if __name__ == "__main__":
    main()
