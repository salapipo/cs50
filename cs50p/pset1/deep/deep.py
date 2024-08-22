def main():
    ans=input("what's the ansers? ").strip().lower()
    match ans:
        case "42"|"forty-two"|"forty two":
            print("Yes")
        case _:
            print("No")

main()

