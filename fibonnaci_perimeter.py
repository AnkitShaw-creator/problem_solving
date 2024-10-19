

def fibonnaci(n:int):
    a, b =0, 1
    lst =[a, b]
    i=0
    while i<n:
        c = a+b
        lst.append(c)
        a=b
        b=c
        i+=1
    print(lst)
    return sum(lst)*4


if __name__ == "__main__":
    n = int(input())
    print(fibonnaci(n))