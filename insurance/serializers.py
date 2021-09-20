from marshmallow import Schema, fields


class InsuranceSchema(Schema):
    id = fields.Int()
    date_of_purchase = fields.Str()
    fuel = fields.Str()
    vehicle_segment = fields.Str()
    premium = fields.Int()
    bodily_injury_liability = fields.Bool()
    personal_injury = fields.Bool()
    property_damage = fields.Bool()
    collision = fields.Bool()
    comprehensive = fields.Bool()
    customer_id = fields.Int()
    customer_gender = fields.Str()
    customer_income_group = fields.Str()
    customer_region = fields.Str()
    customer_marital_status = fields.Str()


insurance_schema = InsuranceSchema()
insurance_schemas = InsuranceSchema(many=True)


class GraphData(Schema):
    type = fields.Str()
    sales = fields.Int()


graph_data_schema = GraphData()
graph_data_schemas = GraphData(many=True)
