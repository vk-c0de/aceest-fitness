from flask import Blueprint, jsonify, request
from app.services import (
    list_programs,
    get_program,
    add_member,
    get_members,
    calculate_membership_fee,
    estimate_calories,
)

bp = Blueprint("api", __name__, url_prefix="/api")


@bp.route("/programs", methods=["GET"])
def programs():
    return jsonify(list_programs())


@bp.route("/programs/<pid>", methods=["GET"])
def program_detail(pid):
    program = get_program(pid)
    if program:
        return jsonify(program), 200
    return jsonify({"error": "Not found"}), 404


@bp.route("/members", methods=["GET"])
def members():
    return jsonify(get_members())


@bp.route("/members", methods=["POST"])
def create_member():
    return jsonify(add_member(request.get_json() or {})), 201


@bp.route("/fee", methods=["POST"])
def fee():
    data = request.get_json() or {}
    months = data.get("months", 1)
    tier = data.get("tier", "standard")
    return jsonify({"fee": calculate_membership_fee(months, tier)})


@bp.route("/calories", methods=["POST"])
def calories():
    data = request.get_json() or {}
    weight = data.get("weight", 70)
    program = data.get("program", "Beginner (BG)")
    return jsonify({"calories": estimate_calories(weight, program)})
