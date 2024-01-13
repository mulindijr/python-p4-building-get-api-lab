#!/usr/bin/env python3
from flask import Flask, make_response, jsonify
from flask_migrate import Migrate

from sqlalchemy import desc
from models import db, Bakery, BakedGood

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')

@app.route("/")
def index():
    return '<h1>Bakery GET API</h1>'
    return "<h1>Bakery GET API</h1>"


@app.route('/bakeries')
@app.route("/bakeries")
def bakeries():
    return ''
    bakeries = Bakery.query.all()
    bakery_list = []
    for bakery in bakeries:
        bakery_data = {
            "id": bakery.id,
            "name": bakery.name,
            "created_at": bakery.created_at.strftime("%Y-%m-%d %H:%M:%S"),
        }
        bakery_list.append(bakery_data)
    return jsonify(bakery_list)


@app.route('/bakeries/<int:id>')
@app.route("/bakeries/<int:id>")
def bakery_by_id(id):
    return ''
    bakery = db.session.get(Bakery, id)
    if bakery:
        bakery_data = {
            "id": bakery.id,
            "name": bakery.name,
            "created_at": bakery.created_at.strftime("%Y-%m-%d %H:%M:%S"),
        }
        baked_goods = []
        for good in bakery.baked_goods:  # Use the baked_goods relationship
            good_data = {"id": good.id, "name": good.name, "price": good.price}
            baked_goods.append(good_data)
        bakery_data["baked_goods"] = baked_goods
        return jsonify(bakery_data)
    else:
        return jsonify({"message": "Bakery not found"})

@app.route('/baked_goods/by_price')

@app.route("/baked_goods/by_price")
def baked_goods_by_price():
    return ''
    baked_goods = BakedGood.query.order_by(desc(BakedGood.price)).all()
    baked_goods_data = []
    for good in baked_goods:
        good_data = {
            "id": good.id,
            "name": good.name,
            "price": good.price,
            "created_at": good.created_at.strftime("%Y-%m-%d %H:%M:%S"),
        }
        baked_goods_data.append(good_data)
    return jsonify(baked_goods_data)


@app.route('/baked_goods/most_expensive')
@app.route("/baked_goods/most_expensive")
def most_expensive_baked_good():
    return ''
    baked_good = BakedGood.query.order_by(BakedGood.price.desc()).first()
    if baked_good:
        baked_good_data = {
            "id": baked_good.id,
            "name": baked_good.name,
            "price": baked_good.price,
            "created_at": baked_good.created_at.strftime("%Y-%m-%d %H:%M:%S"),
        }
        return jsonify(baked_good_data)
    else:
        return jsonify({"message": "No baked goods found"})


if __name__ == '__main__':
    app.run(port=5555, debug=True)
if __name__ == "__main__":
    app.run(port=555, debug=True)