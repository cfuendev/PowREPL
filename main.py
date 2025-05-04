from pow_core import evaluatePowREPL

def main():
    print("PowREPL by CFuen")
    while True:
        print(evaluatePowREPL(input("PowREPL> ")))
        
if __name__ == "__main__":
    main()