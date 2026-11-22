routine_details = ("Exercise", True, 7, 30.0)
print(routine_details)

daily_log = (2, 0, 2, 2, 0, 2, 2)
print(f"Log status : {daily_log}")
print("2 means you have completed the task - 0 means you have not")

print("Number of days recorded:", len(daily_log))

print("First day result:", daily_log[0])
print("Second day result:", daily_log[1])
print("Yesterday's result:", daily_log[-1])

early_week = daily_log[0:3]
print("Starting three days:", early_week)

end_of_week = daily_log[5:7]
print("Saturday and Sunday:", end_of_week)

daily_log = daily_log + (1,)
print("Updated log with extra day:", daily_log)

success_count = daily_log.count(1)
fail_count = daily_log.count(0)

print("Days achieved:", success_count)
print("Days skipped:", fail_count)

total_hit = 0
total_missed = 0

for i in range(0, len(daily_log)):
    if daily_log[i] == 1:
        total_hit += 1
    else:
        total_missed += 1

if total_hit > total_missed:
    print("Awesome job keeping up with your routine!")
else:
    print("Keep pushing to stay on track!")

print("")
print("----- ACTIVITY SUMMARY -----")
print("Activity:", routine_details[0])
print("Full Log:", daily_log)
print("Achieved:", total_hit)
print("Skipped:", total_missed)
print("----------------------------")
