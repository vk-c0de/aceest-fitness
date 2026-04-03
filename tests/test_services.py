from app.services import calculate_membership_fee, estimate_calories

def test_fee_calc():
    assert calculate_membership_fee(6, "standard") == round(6 * 30 * 0.95, 2)

def test_calorie_estimate():
    assert estimate_calories(70, "Fat Loss (FL)") == 70 * 22

