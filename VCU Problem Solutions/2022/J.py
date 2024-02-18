line = input().split()
hour, minute = line[0], line[1]
hour = int(hour)%12
hour = hour+int(minute)/60

h_angle = hour*30
m_angle = int(minute)*6

diff = int(abs(h_angle - m_angle))

if diff > 180:
    diff = abs(360 - diff)

print(diff)