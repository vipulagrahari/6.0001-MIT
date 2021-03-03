import math

def main():
    x = int(input("Enter number one x = "))
    y = int(input("Enter number two y = "))

    z = x**y

    l = (math.log(x))/(math.log(y))

    print(f"Power = {z}, log = {l}")

if __name__ == "__main__":
    main()