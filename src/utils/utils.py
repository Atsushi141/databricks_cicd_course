from datetime import datetime, timedelta

def add_one_day(date_str: str) -> str:
    next_day_obj = datetime.strptime(date_str, "%Y-%m-%d") + timedelta(days=1)
    return next_day_obj.strftime("%Y-%m-%d")
