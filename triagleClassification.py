


def classify_triangle(a, b, c):
    triangleType = "" 
    if a == b and b == c:
        triangleType = "Equilateral"
    elif a == b or b == c or a == c:
        triangleType = "Isosceles"
    elif a != b and b != c and a != c:
        triangleType = "Scalene"
    if a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or a**2 + c**2 == b**2:
        triangleType += " and Right"
    return triangleType

