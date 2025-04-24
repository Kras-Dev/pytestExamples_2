# tests/test_discount_calculator.py
import pytest
import allure

from tests.conftest import calculation_params


@allure.epic("Discount Calculator")
@allure.description("Tests for DiscountCalculator class")
class TestDiscountCalculator:

    @allure.title("Test basic calculation")
    @pytest.mark.positive
    def test_calculate_total(self, discount_calculator, calculation_params):
        """Тестирование расчета итоговой суммы для разных условий."""
        base_price, quantity, flags, expected = calculation_params
        calculator = discount_calculator(base_price, quantity)
        with allure.step(f"Calculating total for base price {base_price} and quantity {quantity} with flags {flags}"):
            result = calculator.calculate_total(**flags)
            assert result == pytest.approx(expected)

    @allure.title("Test ValueError on negative base price")
    @pytest.mark.raises
    def test_negative_price(self, discount_calculator):
        """Проверка, что отрицательная базовая цена вызывает ошибку."""
        with pytest.raises(ValueError), allure.step("Checking that calculate_total raises ValueError"):
            calculator = discount_calculator(-10, 1)
            calculator.calculate_total()

    @allure.title("Test incorrect discount")
    @pytest.mark.xfail(reason="Expected failure due to incorrect discount calculation")
    def test_incorrect_discount(self, discount_calculator, calculate_expected_result):
        """Тест для проверки некорректного расчета скидки."""
        base_price, quantity, flags, expected = calculate_expected_result
        calculator = discount_calculator(base_price, quantity)
        with allure.step("Calculate the total with student discount and coupon"):
            result = calculator.calculate_total(**flags)
            assert result == expected
            
    @allure.title("Test warnings for large quantity")
    @pytest.mark.positive
    def test_large_quantity_warning(self, discount_calculator):
        """Проверка предупреждений, если количество товара больше 1000."""
        with pytest.warns(Warning, match="Large quantity order detected!"):
            calculator = discount_calculator(100, 1001)
            calculator.calculate_total()

    @allure.title("Test skipping calculation for specific condition")
    @pytest.mark.skipif(condition=True, reason='Skipped due to specific condition')
    def test_skipped_case(self):
        """Этот тест пропущен ввиду специфического условия."""
        assert True
