from datetime import datetime, timedelta
def calculate_menstrual_cycle(lmp, cycle_length):
    
    lmp_date = datetime.strptime(lmp, "%Y-%m-%d")
    next_period = lmp_date + timedelta(days=cycle_length)
    ovulation_date = next_period - timedelta(days=14)
    fertile_start = ovulation_date - timedelta(days=2)
    fertile_end = ovulation_date + timedelta(days=2)
    safe_start = fertile_end + timedelta(days=1)
    safe_end = fertile_start - timedelta(days=1)

    return {
            "next_period": next_period.strftime("%Y-%m-%d"),
            "ovulation_date": ovulation_date.strftime("%Y-%m-%d"),
            "fertile_window": (fertile_start.strftime("%Y-%m-%d"), fertile_end.strftime("%Y-%m-%d")),
            "safe_window_before": ("Cycle Start", safe_end.strftime("%Y-%m-%d")),
            "safe_window_after": (safe_start.strftime("%Y-%m-%d"), "Cycle End"),
        }

