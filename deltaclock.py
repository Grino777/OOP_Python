class DeltaClock:
    def __init__(self, clock1, clock2):
        self.clock1: Clock = clock1
        self.clock2: Clock = clock2
        self.seconds = self.difference_time()

    def __str__(self):
        if self.seconds < 0:
            return f'00: 00: 00'
        else:
            h, m, s = self.convert_time(self.seconds)
            return '{:02}: {:02}: {:02}'.format(h, m, s)

    def __len__(self):
        if self.seconds < 0:
            return 0
        else:
            return self.seconds

    def difference_time(self):
        t1 = self.clock1.get_time()
        t2 = self.clock2.get_time()
        res = t1 - t2
        return res

    def convert_time(self, sec):
        sec = sec % (24 * 3600)
        hour = sec // 3600
        sec %= 3600
        min = sec // 60
        sec %= 60
        return (hour, min, sec)


class Clock:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds


dt = DeltaClock(Clock(2, 45, 0), Clock(1, 15, 0))
print(dt)  # 01: 30: 00
len_dt = len(dt) # 5400
print(len_dt)
