def print_poly(px):
    term = len(px) - 1  # 최고차항 숫자 = 배열길이-1
    poly_str = "P(x) = "

    for i in range(len(px)):
        coef = px[i]  # 계수

        if coef >= 0:
            poly_str += "+"
        poly_str = poly_str + f'{coef}x^{term} '
        term = term - 1

    return poly_str


def calc_poly(x_val, p_x):
    ret_value = 0
    term = len(p_x) - 1

    for i in range(len(px)):
        coef = p_x[i]
        ret_value += coef * xValue ** term
        term -= 1

    return ret_value

px = [7, -4, 0, 5]

if __name__ == "__main__":
    pStr = print_poly(px)
    print(pStr)

    xValue = int(input("X 값-->"))

    pxValue = calc_poly(xValue, px)
    print(pxValue)


