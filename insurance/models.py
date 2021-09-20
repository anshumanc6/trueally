"""Insurance Models."""
from database import Model, db, Column, SurrogatePK


class Insurance(SurrogatePK, Model):
    __tablename__ = 'insurance'
    # id = Column(db.Integer, unique=True, nullable=False)
    date_of_purchase = Column(db.String, nullable=False)
    fuel = Column(db.String, nullable=False)
    vehicle_segment = Column(db.String, nullable=False)
    premium = Column(db.Integer, nullable=False)
    bodily_injury_liability = Column(db.Boolean, nullable=False)
    personal_injury = Column(db.Boolean, nullable=False)
    property_damage = Column(db.Boolean, nullable=False)
    collision = Column(db.Boolean, nullable=False)
    comprehensive = Column(db.Boolean, nullable=False)
    customer_id = Column(db.Integer, nullable=False)
    customer_gender = Column(db.String, nullable=False)
    customer_income_group = Column(db.String, nullable=False)
    customer_region = Column(db.String, nullable=False)
    customer_marital_status = Column(db.String, nullable=False)

    def __init__(self, id, date_of_purchase, fuel, vehicle_segment, premium, bodily_injury_liability, personal_injury,
                 property_damage, collision, comprehensive, customer_id, customer_gender, customer_income_group,
                 customer_region, customer_marital_status):
        self.id = id
        self.date_of_purchase = date_of_purchase
        self.fuel = fuel
        self.vehicle_segment = vehicle_segment
        self.premium = premium
        self.bodily_injury_liability = bodily_injury_liability
        self.personal_injury = personal_injury
        self.property_damage = property_damage
        self.collision = collision
        self.comprehensive = comprehensive
        self.customer_id = customer_id
        self.customer_gender = customer_gender
        self.customer_income_group = customer_income_group
        self.customer_region = customer_region
        self.customer_marital_status = customer_marital_status
