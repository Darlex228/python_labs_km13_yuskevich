print("Вкажіть магнітуду землетрусів за шкалою Ріхтера")
erth_qk = float(input())      #magnitude of an earth quake 
if 0<= erth_qk < 2:
    print("Micro")
elif 2 <= erth_qk < 3:
    print("Very minor")
elif 3<= erth_qk < 4:
    print("Minor")
elif 6 <= erth_qk < 5:
    print("Light")
elif 5 <= erth_qk < 6:
    print(" Moderate")
elif 6 <= erth_qk < 7:
    print("Strong")
elif 7 <= erth_qk < 8:
    print("Major")
elif 8 <= erth_qk < 10:
    print("Great")
elif 10 <= erth_qk:
    print("Meteoric")
else:
    print("Wrong number")
