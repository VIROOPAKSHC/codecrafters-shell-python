import sys
import os

def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    # print("Logs from your program will appear here!")

    # Uncomment this block to pass the first stage
    sys.stdout.write("$ ")
    sys.stdout.flush()


    # Wait for user input
    command = input()
    paths = os.environ["PATH"].split(":")
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
                if args[1] in ["echo","exit","type"]:
                    print(f"{args[1]} is a shell builtin")
                else:        
                    found=0
                    for path in paths:
                        executable = os.path.join(path, args[1])
                        if os.path.isfile(executable) and os.access(executable, os.X_OK):
                            print(f"{args[1]} is {executable}")
                            found=1
                    if not found:
                        print("{} not found".format(args[1]))
        else:
            location=""
            for path in paths:
                executable = os.path.join(path, args[1])
                if os.path.isfile(executable) and os.access(executable, os.X_OK):
                    location = executable
            # print(location)
            # print(args)

            try:
                first = args[0]
                args.pop(0)
                with os.popen(f"{args[0]} {args}") as _exec:
                    sys.stdout.write(_exec.read())
            except Exception as e:
                sys.stdout.write(f"failed with error: {e}\n")
          
        sys.stdout.write("$ ")
        sys.stdout.flush()
        command = input()


if __name__ == "__main__":
    main()
