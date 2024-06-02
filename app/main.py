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
            if (len(args)==2) and args[1] == "0":
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
                            break
                    if not found:
                        print("{} not found".format(args[1]))
        elif args[0] == 'pwd':
            print(os.getcwd())
        elif args[0] == 'cd':
            dest = args[1].split("/")
            while dest:
                if len(dest)==1 and dest[0]=='':
                    break
                if dest[0] == "..":
                    os.chdir("..")
                elif dest[0] in os.listdir():
                    os.chdir(dest[0])
                else:
                    print("/".join(dest)+": No such file or directory")
                    break
                dest.pop(0)
        elif len(args)==1:
            print("{}: command not found".format(args[0]))
        else:
            location=""
            for path in paths:
                executable = os.path.join(path, args[1])
                if os.path.isfile(executable) and os.access(executable, os.X_OK):
                    location = executable
                    
            try:
                with os.popen(f"{args[0]} {args[1]}") as _exec:
                    sys.stdout.write(_exec.read())
            except Exception as e:
                sys.stdout.write(f"failed with error: {e}\n")
          
        sys.stdout.write("$ ")
        sys.stdout.flush()
        command = input()


if __name__ == "__main__":
    main()
