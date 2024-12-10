import matplotlib.pyplot as plt

# Másodfokú függvény paraméterei
a = 1
b = -3
c = 2

# x értéktartomány generálása
x = [i / 10 for i in range(-100, 101)]  # -10-től 10-ig 0.1 lépésközzel
y = [a * xi**2 + b * xi + c for xi in x]  # Másodfokú függvény értékei

# Grafikon rajzolása
plt.figure(figsize=(8, 6))
plt.plot(x, y, label=f"${a}x^2 + {b}x + {c}$", color="blue")
plt.axhline(0, color="black", linewidth=0.8, linestyle="--")  # x tengely
plt.axvline(0, color="black", linewidth=0.8, linestyle="--")  # y tengely
plt.title("Másodfokú függvény ábrázolása", fontsize=14)
plt.xlabel("x tengely")
plt.ylabel("y tengely")
plt.legend()
plt.grid(True)
plt.show()
