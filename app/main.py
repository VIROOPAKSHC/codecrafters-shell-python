import sys


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    # print("Logs from your program will appear here!")

    # Uncomment this block to pass the first stage
    sys.stdout.write("$ ")
    sys.stdout.flush()


    # Wait for user input
    command = input()
    while True:
        args = command.split()
        if args[0] == "exit":
            if args[1] == "0":
                sys.exit(0)
            else:
                print("Provide exit code for exit.")
        elif args[0] == "echo":
            print(" ".join(args[1:]))
        elif args[0] == "type":
            if len(args) == 1:
                print("type must provide a command.")
            else:
                if args[1] in ["echo","type","exit","cat"]:
                    print("{} is a shell bulletin".format(args[1]))
                else:
                    print("{} not found".format(args[1]))
        else:
            print("{}: command not found".format(command))
        sys.stdout.write("$ ")
        sys.stdout.flush()
        command = input()


if __name__ == "__main__":
    main()
