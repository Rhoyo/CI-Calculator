"""
Test for calc app
"""

import calculator

class TestCalculatorApp:
    def test_add(self):
        assert 5 == calculator.add(3,2)

    def test_sub(self):
        assert 5 == calculator.sub(8,3)	

	def test_mult(self):
	    assert 4 == calculator.mult(2,2)
