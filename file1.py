import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8]
y = [45,50,55,62,68,72,78,85]

plt.plot(x,y, marker='o', label ="คะแนนสอบ")

plt.xlabel("ชั่วโมงอ่านหนังสือสอบ")
plt.ylabel("คะแนนสอบ")
plt.title("ความสัมพันธ์ระหว่างชั่วโมงอ่านหนังสือสอบกับคะแนนสอบ")

plt.legend()
plt.show()