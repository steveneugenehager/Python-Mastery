# A simple module that I will import in another simple script.

print("I am in " + __name__)

def main():
    hello('world')
    goodbye('world')


def hello(str):
    print("Hello, " + str.title() + '!' )

def goodbye(str):
    print("Goodbye, " + str.title() + '!' )

if __name__ == '__main__':
    main()