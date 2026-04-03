PROGRAMS = {
    "Fat Loss (FL)": {
        "workout": "Back Squat, Cardio, Bench, Deadlift, Recovery",
        "diet": "Egg Whites, Chicken, Fish Curry",
        "color": "#e74c3c",
        "calorie_factor": 22
    },
    "Muscle Gain (MG)": {
        "workout": "Squat, Bench, Deadlift, Press, Rows",
        "diet": "Eggs, Biryani, Mutton Curry",
        "color": "#2ecc71",
        "calorie_factor": 35
    },
    "Beginner (BG)": {
        "workout": "Air Squats, Ring Rows, Push-ups",
        "diet": "Balanced Tamil Meals",
        "color": "#3498db",
        "calorie_factor": 26
    }
}

_MEMBERS = []

def list_programs():
    return [{"id": k, **v} for k, v in PROGRAMS.items()]

def get_program(pid):
    return PROGRAMS.get(pid)

def add_member(data):
    member = {"name": data.get("name"), "email": data.get("email"), "tier": data.get("tier")}
    _MEMBERS.append(member)
    return member

def get_members():
    return _MEMBERS

def calculate_membership_fee(months, tier):
    base = {"standard": 30, "premium": 50, "vip": 80}
    rate = base.get(tier, 30)
    discount = 0.05 if months >= 6 else 0
    return round(months * rate * (1 - discount), 2)

def estimate_calories(weight, program):
    factor = PROGRAMS.get(program, {}).get("calorie_factor", 25)
    return int(weight * factor)

