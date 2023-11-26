class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def addTime(self, other_time):
        total_hours = self.hours + other_time.hours
        total_minutes = self.minutes + other_time.minutes

        if total_minutes >= 60:
            total_hours += total_minutes // 60
            total_minutes %= 60

        return Time(total_hours, total_minutes)

    def displayTime(self):
        print(f"{self.hours} hours and {self.minutes} minutes")

    def displayMinutes(self):
        total_minutes = self.hours * 60 + self.minutes
        print(f"Total minutes: {total_minutes}")

time1 = Time(2, 50)
time2 = Time(1, 20)

sum_time = time1.addTime(time2)

print("Time 1:")
time1.displayTime()

print("\nTime 2:")
time2.displayTime()

print("\nSum of Time 1 and Time 2:")
sum_time.displayTime()

sum_time.displayMinutes()
