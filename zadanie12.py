def srodek_ciezkosci(ax, ay, bx, by, cx, cy):

    return ((ax + bx + cx) / 3, (ay + by + cy) / 3)

print("podaj wspolrzedne wierzcholkow trojkata:")

ax = float(input("Ax: "))
ay = float(input("Ay: "))
bx = float(input("Bx: "))
by = float(input("By: "))
cx = float(input("Cx: "))
cy = float(input("Cy: "))

sx, sy = srodek_ciezkosci(ax, ay, bx, by, cx, cy)

print(f"srodek ciezkosci: ({sx}, {sy})")