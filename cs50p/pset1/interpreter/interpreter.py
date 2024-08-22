def main():
    a=input("Expression: ")
    x,y,z=a.split()
    x=float(x)
    z=float(z)
    match y:
        case "+":
            print(round(x+z,1))
        case "-":
            print(f"{x-z:.1f}")
        case "*":
            print(round(x*z,1))
        case "/":
            print(round(x/z,1))

main()
