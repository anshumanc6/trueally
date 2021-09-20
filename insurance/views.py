"""Insurance Views"""
import json

from flask import Blueprint, request, Response
from flask_apispec import use_kwargs, marshal_with

from insurance.serializers import insurance_schema
from insurance.models import Insurance

blueprint = Blueprint('insurance', __name__)


@blueprint.route("/api/insurance/policy/<policy_id>", methods=("GET",))
@use_kwargs(insurance_schema)
@marshal_with(insurance_schema)
def get_insurance_by_policy_id(policy_id):
    """Get Insurance by policy id"""
    insurance = Insurance.query.get(policy_id)
    if insurance:
        return insurance
    else:
        return Response("{\"error\":\"no insurance found\"}", status=400, mimetype='application/json')


@blueprint.route("/api/insurance/customer/<customer_id>", methods=("GET",))
@use_kwargs(insurance_schema)
@marshal_with(insurance_schema)
def get_insurance_by_customer_id(customer_id):
    """Get Insurance by customer id"""
    insurance = Insurance.query.filter_by(customer_id=customer_id).first()
    if insurance:
        return insurance
    else:
        return Response("{\"error\":\"no insurance found\"}", status=400, mimetype='application/json')


@blueprint.route("/api/insurance/policy/<policy_id>", methods=("PUT",))
@use_kwargs(insurance_schema)
@marshal_with(insurance_schema)
def update_insurance(policy_id, **kwargs):
    """Update Insurance by policy id"""
    insurance_from_db = Insurance.query.get(policy_id)
    if insurance_from_db:
        insurance_req = request.get_json()
        for key in insurance_req:
            if key == "fuel":
                insurance_from_db.fuel = insurance_req["fuel"]
            if key == "vehicle_segment":
                insurance_from_db.vehicle_segment = insurance_req["vehicle_segment"]
            if key == "premium":
                insurance_from_db.premium = insurance_req["premium"]
            if key == "bodily_injury_liability":
                insurance_from_db.bodily_injury_liability = insurance_req["bodily_injury_liability"]
            if key == "personal_injury":
                insurance_from_db.personal_injury = insurance_req["personal_injury"]
            if key == "property_damage":
                insurance_from_db.property_damage = insurance_req["property_damage"]
            if key == "collision":
                insurance_from_db.collision = insurance_req["collision"]
            if key == "comprehensive":
                insurance_from_db.comprehensive = insurance_req["comprehensive"]
            if key == "customer_id":
                insurance_from_db.customer_id = insurance_req["customer_id"]
            if key == "customer_gender":
                insurance_from_db.customer_gender = insurance_req["customer_gender"]
            if key == "customer_income_group":
                insurance_from_db.customer_income_group = insurance_req["customer_income_group"]
            if key == "customer_region":
                insurance_from_db.customer_region = insurance_req["customer_region"]
            if key == "customer_marital_status":
                insurance_from_db.customer_marital_status = insurance_req["customer_marital_status"]
        return insurance_from_db.save()
    else:
        return Response("{\"error\":\"no insurance found\"}", status=400, mimetype='application/json')


@blueprint.route("/api/insurance/graph_data", methods=("GET",))
def get_monthly_insurance_data():
    """Get monthly insurance sales data for graph."""
    insurances = Insurance.query.all()
    graph_data = []
    ret_data = []
    unique_months = set()
    for insurance in insurances:
        elem = insurance.date_of_purchase.split("/")
        graph_data.append({"type": elem[0] + "-" + elem[2], "sales": 1})

    for idx, data in enumerate(graph_data):
        if data["type"] in unique_months:
            for inx, item in enumerate(ret_data):
                if data["type"] == item["type"]:
                    ret_data[inx]["sales"] = item["sales"] + 1
        else:
            unique_months.add(data["type"])
            ret_data.append(data)

    if ret_data:
        return Response(json.dumps(ret_data), status=200, mimetype="application/json")
    else:
        return Response({"error": "unable to fetch"}, status=500, mimetype="application/json")
