from unittest import TestCase
from datetime import datetime
import menstrualPeriodApp

class TestMenstrualTracker(TestCase):
    def test_calculate_menstrual_cycle(self):
        lmp = "2024-11-01"
        cycle_length = 28
        expected = {
            "next_period": "2024-11-29",
            "ovulation_date": "2024-11-15",
            "fertile_window": ("2024-11-13", "2024-11-17"),
            "safe_window_before": ("Cycle Start", "2024-11-12"),
            "safe_window_after": ("2024-11-18", "Cycle End"),
        }
        result = menstrualPeriodApp.calculate_menstrual_cycle(lmp, cycle_length)

        self.assertEqual(expected, result)
