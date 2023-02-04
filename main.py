import matplotlib.pyplot as plt


def lerp(P1, P2, t):
    x = t * P2[0] + (1 - t) * P1[0]
    y = t * P2[1] + (1 - t) * P1[1]
    return x, y


def bezgen4(x1, y1, x2, y2, x3, y3, x4, y4, t):
    P1 = (x1, y1)
    P2 = (x2, y2)
    P3 = (x3, y3)
    P4 = (x4, y4)

    P12 = lerp(P1, P2, t)
    P23 = lerp(P2, P3, t)
    P34 = lerp(P3, P4, t)

    P1223 = lerp(P12, P23, t)
    P2334 = lerp(P23, P34, t)

    return lerp(P1223, P2334, t)


def bezgen3(x1, y1, x2, y2, x3, y3, t):
    P1 = (x1, y1)
    P2 = (x2, y2)
    P3 = (x3, y3)

    P12 = lerp(P1, P2, t)
    P23 = lerp(P2, P3, t)

    return lerp(P12, P23, t)


if __name__ == "__main__":
    x1 = -5  # int(input("x1: "))
    y1 = -5  # int(input("y1: "))
    x2 = -5  # int(input("x2: "))
    y2 = 5  # int(input("y2: "))
    x3 = 5  # int(input("x3: "))
    y3 = 5  # int(input("y3: "))
    x4 = 5  # int(input("x4: "))
    y4 = -5  # int(input("y4: "))
    # t = float(input("t: "))

    arrx = []
    arry = []

    t = 0
    while t <= 1:
        x, y = bezgen4(x1, y1, x2, y2, x3, y3, x4, y4, t)
        arrx.append(x)
        arry.append(y)
        t += 0.001
    # print(f"{x};{y}")

    plt.plot(arrx, arry, label="Bezier")
    plt.plot([x1, x2, x3, x4], [y1, y2, y3, y4], label = "Border")

    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()
