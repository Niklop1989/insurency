from crypt import methods
from typing import List, Optional

from certifi import where
from sqlalchemy import insert,update,select,delete,String, Integer, Float,ForeignKey, create_engine, MetaData
from sqlalchemy.orm import (DeclarativeBase, Mapped,
                            mapped_column, relationship,Session)

from flask import Flask,jsonify,abort,request

app = Flask(__name__)
engine = create_engine("sqlite:///my_db")
session = Session(engine)
class Base(DeclarativeBase):
    pass

class Product(Base):
    __tablename__ = 'products'

    id:Mapped[int] = mapped_column(primary_key=True)
    title:Mapped[str] = mapped_column(String(200),nullable=False)
    count:Mapped[int] = mapped_column(Integer,default=0)
    price:Mapped[float] = mapped_column(Float,default=0)

    def __repr__(self):
        return f"Товар {self.title}, кол-во {self.count}, цена: {self.price}"
    def to_json(self):
        return {c.name: getattr(self,c.name) for c in self.__table__.columns}

@app.before_request
def before_request_func():
    Base.metadata.create_all(engine)

@app.route('/')
def hello_world():
    return "Hello world"
@app.route('/products',methods=['GET'])
def get_all_products():
    product_list = []
    products = session.query(Product).all()
    for pr in products:
        product_list.append(pr.to_json())
    session.close()
    return jsonify(product_list = product_list), 200

@app.route("/product/<int:id>",methods=['GET'])
def get_product_by_id(id):
    product = session.query(Product).filter(Product.id==id).one_or_none()
    if product is None:
        abort(404)
    return jsonify(product=product.to_json()) ,200

@app.route("/products",methods=['POST'])
def add_product():
    title = request.form.get("title",type=str)
    count = request.form.get('count',type=int)
    price = request.form.get('price',type=float)
    new_prod = Product(title=title,count=count,price=price)

    session.add(new_prod)
    session.commit()
    session.close()
    return " add new product",201
@app.route("/product/<int:id>",methods=['DELETE'])
def delete_prod(id):
    # session.query(Product).filter(Product.id==id).delete()
    # session.commit()
    prod = delete(Product).where(Product.id==id)
    session.execute(prod)
    return "product delete",200

@app.route("/product/<int:id>",methods=['PATCH'])
def update_product(id):
    title = request.form.get("title", type=str)
    count = request.form.get('count', type=int)
    price = request.form.get('price', type=float)
    # first updata
    product = session.query(Product).filter(Product.id ==id).one_or_none()
    if title:
        product.title = title
    if count:
        product.count = count
    if price:
        product.price = price
    session.commit()

    # second update
    # session.query(Product).filter(Product.id==id)\
    # .update({Product.title:title,
    #          Product.count:count,
    #          Product.price:price})
    # session.commit()

    # third u[date
    # query = update(Product).where(Product.id==id).values(title=title,
    #                                                      count=count,
    #                                                      price=price)
    # print(query)
    # session.execute(query)
    return 'product update',200


if __name__=='__main__':
    app.run()

