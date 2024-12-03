def add(a,b):
    return a+b
def multiplication(a,b):
    return a*b
def division(a,b):
    return a/b
def  subtraction(a,b):
    return a-b
def improper_to_mixed(numerator, denominator):
    whole = numerator // denominator
    new_numerator = numerator % denominator
    if new_numerator == 0:
        return f"{whole}"
    else:
        return f"{whole} {new_numerator}/{denominator}"
def mixed_to_improper(whole, numerator, denominator):
    improper_numerator = (whole * denominator) + numerator
    improper_denominator = denominator
    return f"{improper_numerator}/{improper_denominator}"
def fraction_to_decimal(numerator,denominator):
    if denominator==0:
        return "error..."
    return numerator/denominator
def calculate_percentage(part,whole):
    if whole==0:
        return "error..."
    return (part/whole)*100
def percentage(number,yourpercentage):
    return number*(yourpercentage/100)
