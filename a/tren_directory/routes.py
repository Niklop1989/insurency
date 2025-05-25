from apispec.ext.marshmallow import MarshmallowPlugin
from apispec_webframeworks.flask import FlaskPlugin
from flask import Flask,request
from flask_restful import Resource,Api

from marshmallow import ValidationError

from flasgger import APISpec,Swagger

from schemas import CarSchema,OwnerSchema

from models import (DATABASE_NAME, CAR_TABLE_NAME, OWNER_TABLE_NAME, Car,Owner,
                    DATA_OWNERS, DATA_CARS,
                    init_db, get_all_cars, add_car, delete_owner_by_id,
                    add_owner, get_all_owner, get_car_by_id)
from models import get_car_by_owner, update_car_by_id

app = Flask(__name__)
api = Api(app)

spec = APISpec(
    title='CarsList',
    version='1.0.0',
    openapi_version='2.0',
    plugins=[FlaskPlugin(),MarshmallowPlugin()],
)


class CarsList(Resource):
    def get(self):
        schema = CarSchema()
        return schema.dump(get_all_cars(),many=True)

    def post(self):
        data = request.json
        schema = CarSchema()
        try:
           car = schema.load(data)
        except ValidationError as exc:
            return exc.messages, 400
        car = add_car(car)
        return schema.dump(car),201


class OwnersList(Resource):
    def get(self):
        schema = OwnerSchema()
        return schema.dump(get_all_owner(),many=True)

    def post(self):
        data = request.json
        schema=OwnerSchema()
        try:
            owner = schema.load(data)
        except ValidationError as exc:
            return exc.messages,400
        owner=add_owner(owner)
        return schema.dump(owner)

class Owners(Resource):
    def delete(self,owner_id):
        schema = OwnerSchema()
        return schema.dump(delete_owner_by_id(owner_id)),200
    def get(self,owner_id):
        schema = CarSchema()
        return schema.dump(get_car_by_owner(owner_id),many=True),200


class CarsEdit(Resource):
    def get(self,car_id):
        schema = CarSchema()
        return schema.dump(get_car_by_id(car_id))
    def put(self,car_id):
        data = request.json
        car = Car(brand_car=data['brand_car'],owner=data['owner'],id=car_id)
        return update_car_by_id(car),200

api.add_resource(CarsList,'/api/cars')
api.add_resource(OwnersList,'/api/owners')
api.add_resource(Owners,'/api/owners/<int:owner_id>')
api.add_resource(CarsEdit,'/api/cars/<int:car_id>')


swagger = Swagger(app,template_file='swagger.yaml')
if __name__=='__main__':
    init_db(initial_records_cars=DATA_CARS,initial_records_owners=DATA_OWNERS)
    app.run(debug=True,host='0.0.0.0')