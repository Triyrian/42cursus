import sys

if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    list = []
    argc = len(sys.argv)
    if (argc <= 1):
        print(
            f"No score provided. Usage: python3 {sys.argv[0]}"
            "<score1> <score2> ..."
            )
    else:
        for element in range(1, len(sys.argv)):
            try:
                number = int(sys.argv[element])
            except ValueError:
                print(f"Invalid parameter: '{sys.argv[element]}'")
            else:
                list.append(number)
        if not list:
            print(
                f"No score provided. Usage: python3 {sys.argv[0]}"
                " <score1> <score2> ..."
                 )
        else:
            print(f"Scores processed: {list}")
            print(f"Total players: {len(list)}")
            print(f"Total score: {sum(list)}")
            print(f"Average score: {sum(list) / len(list)}")
            print(f"High score: {max(list)}")
            print(f"Low score: {min(list)}")
            print(f"Score range: {max(list) - min(list)}")
            print("")
