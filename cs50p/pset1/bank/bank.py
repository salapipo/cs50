def main():
    grt=input("Greeting: ").strip().lower()
    if grt.startswith("hello"):
        print("$0")
    elif grt.startswith("h"):
        print("$20")
    else:
        print("$100")

main()
