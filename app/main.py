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
        if command.split()[0] == "exit":
            if command.split()[1] == "0":
                sys.exit(0)
            else:
                print("Provide exit code for exit.")
        else:
            print("{}: command not found".format(command))
        sys.stdout.write("$ ")
        sys.stdout.flush()
        command = input()


if __name__ == "__main__":
    main()
