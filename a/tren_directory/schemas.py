from flasgger import Schema,fields,ValidationError
from marshmallow import validates,post_load

from models import Car,Owner

class CarSchema(Schema):
    id = fields.Int(dump_only=True)
    brand_car = fields.Str(required=True)
    owner = fields.Int(required=True)

    @post_load
    def create_car(self,data:dict,**kwargs) -> Car:
        return Car(**data)

class OwnerSchema(Schema):
    owner_id = fields.Int(dump_only=True)
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    middle_name = fields.Str()

    @post_load
    def create_owner(self,data:dict,**kwargs) ->Owner:
        return Owner(**data)