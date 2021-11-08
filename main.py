import telegraph


def main():
    file = input("Enter your file directory :- ")
    try:
        response = telegraph.upload_file(file)
        print(f"https://telegra.ph{response[0]}")
    except Exception as error:
        print(error)
    again = input("If you need to upload again?\ny for yes n for no\n:- ")
    if again.lower() == "n":
        print("\nThanks for using")
        break
    else:
        print("")
        return main()


main()
