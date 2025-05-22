from datetime import datetime, timezone

# Get current UTC time
current_utc_time = datetime.now(timezone.utc)
current_utc_time.strftime("%Y-%m-%d %H:%M:%S %Z")

print(current_utc_time)