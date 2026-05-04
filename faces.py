def convert(usertxt):
    newtxt = usertxt.replace(":)", "🙂").replace(":(", "🙁")
    return newtxt

def main():
    userinput = str(input("Type: "))
    output = convert(userinput)
    print(output)

main()

