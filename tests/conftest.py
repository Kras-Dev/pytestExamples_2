# tests/conftest.py

import pytest
from discount_calculator import DiscountCalculator

@pytest.fixture(scope="class")
def discount_calculator():
    """Фикстура для создания экземпляра DiscountCalculator."""
    def create_calculator(base_price: float, quantity: int) -> DiscountCalculator:
        if quantity <= 0:
            pytest.fail("Quantity must be greater than zero")
        return DiscountCalculator(base_price=base_price , quantity=quantity)

    return create_calculator

@pytest.fixture(params=[
    (100, 1, {}, 100),
    (100, 1, {'is_student': True}, 90),
    (100, 1, {'is_holiday': True}, 95),
    (100, 1, {'is_first_purchase': True}, 85),
    (100, 20, {'is_bulk_order': True}, 1600),
    (100, 1, {'is_member': True}, 93),
    (100, 1, {'is_eco_friendly': True}, 97),
    (100, 1, {'is_referral': True}, 92),
    (100, 1, {'is_express_delivery': True}, 110),
    (100, 1, {'is_gift_wrapping': True}, 105),
    (100, 1, {'is_peak_season': True}, 112),
    (100, 1, {'has_coupon': True}, 50),
    (100, 1, {'is_student': True, 'has_coupon': True}, 40),
    (100, 1, {'is_first_purchase': True, 'is_member': True, 'is_gift_wrapping': True}, 83.0025),
    (50, 1, {'is_student': True, 'has_coupon': True}, 0),
], scope="function")
def calculation_params(request):
    """Фикстура с параметрами для тестов."""
    return request.param

@pytest.fixture(params=[
    (9, 5, {'is_student':True, 'has_coupon': True}, (9 * 5) * 0.9 - 50)], scope="function")
def calculate_expected_result(request):
    """Фикстура с параметрами для тестов."""
    return request.param
