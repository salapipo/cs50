def main():
    a=input("write a sentence with an emoticon: ")
    print(convert(a))

def convert(emo):
    return emo.replace(":)","🙂").replace(":(","🙁")

main()
