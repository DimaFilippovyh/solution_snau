import math as m
import sympy as s



syst = ("m.sin(x) + 2 * y - 2", \
        "2 * x + m.cos(y - 1) + x - 0.7")

# syst = ("m.sin(x + 1) - y - 1", \
#         "2 * x + m.cos(y) - 2")

# x = 0.5
# y = -0.0025



def system(x, y):
    """
    Решаю систему с заданными х и у
    """
    return eval(syst[0]), eval(syst[1])


def difer(x, y, t):
    """
    Нахожу производную t - номер уравнения(0, 1)
    """
    px, py = s.symbols('px py')
    str1, str2 = syst[0], syst[1]

    for i, j in [("m", "s"), ("x", "px"), ("y", "py")]:
        str1 = str1.replace(i, j)
        str2 = str2.replace(i, j)

    if t == 0:
        dif_1, dif_2 = eval(str1), eval(str1)
    else:
        dif_1, dif_2 = eval(str2), eval(str2)

    dif_1, dif_2 = s.diff(dif_1, px), s.diff(dif_2, py)
    return dif_1.evalf(subs={px: x}), dif_2.evalf(subs={py: y})


def matr_jacobi(w, x, y):
    """
    нахожу матрицу Якоби
    """
    w[0][0], w[0][1] = difer(x, y, 0)
    w[1][0], w[1][1] = difer(x, y, 1)


def obr_matr(w):
    """
    Нахожу обратную матрицу
    """
    det = w[0][0] * w[1][1] - w[0][1] * w[1][0]
    w[0][0], w[1][1] = w[1][1] / det, w[0][0] / det
    w[0][1] = -w[0][1] / det
    w[1][0] = -w[1][0] / det


def met_newton(x, y):
    eps = 0.001
    step = 0
    w = [[0, 0], [0, 0]]

    while True:
        step += 1
        prev_x, prev_y = x, y

        matr_jacobi(w, x, y)

        obr_matr(w)

        dx = w[0][0] * system(x, y)[0] + w[0][1] * system(x, y)[1]
        dy = w[1][0] * system(x, y)[0] + w[1][1] * system(x, y)[1]

        x -= dx
        y -= dy

        flag = True

        if abs(x - prev_x) > eps and abs(y - prev_y) > eps:
            flag = False

        if flag:
            return x, y, step

def vector_nev(x, y):
    """
    Вывод вектора невязки

    """
    o_1,o_2 = eval(syst[0]), eval(syst[1])
    print("Получили вектор невязки:")
    print("1 =\t{0:10.10f} \n2 =\t{1:10.10f}".format(o_1, o_2))



def main():
    x = int(input("Введите x = "))
    y = int(input("Введите y = "))
    #x, y = 1, 1

    otv = met_newton(x, y)

    vector_nev(otv[0], otv[1])

    print("Получили ответ: ")
    print("x =  {0:10.5f} \ny =  {1:10.5f}".format(otv[0], otv[1]))
    print(F"Количество шагов - {otv[2]}")


if __name__ == "__main__":
    main()






