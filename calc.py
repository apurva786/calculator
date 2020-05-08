import logging


def do_addition(a,b):
    return a+b

def do_subtraction(a,b):
    return a-b

def do_multiplication(a,b):
    return a*b

def do_divide(a,b):
    return a//b

if __name__ == "__main__":
    x = do_addition(6,4)
    y = do_subtraction(6,4)
    z = do_multiplication(6,4)
    v = do_divide(6,3)
    print("Addition of 6+4=",x)
    print("Subtraction of 6-4=",y)
    print("Multiplication of 6*4=",z)
    print("Division of 6*3=",v)
    logging.basicConfig(filename="logFile.txt",
                    filemode='a',
                    format='%(asctime)s %(levelname)s-%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',level=logging.DEBUG)
    logging.info(x)
    logging.info(y)
    logging.info(z)
