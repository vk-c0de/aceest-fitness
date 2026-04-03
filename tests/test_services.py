from app.services import calculate_membership_fee, estimate_calories


def test_fee_calc():
    fee = calculate_membership_fee(6, "standard")
    assert fee == round(6 * 30 * 0.95, 2)


def test_calorie_estimate():
    calories = estimate_calories(70, "Fat Loss (FL)")
    assert calories == 70 * 22
