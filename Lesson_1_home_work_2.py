user_seconds = int(input("Enter seconds: "))
time_minutes = user_seconds // 60
time_hours = time_minutes // 60
time_seconds = user_seconds // 360
print(f"{time_minutes}:{time_hours}:{time_seconds}")