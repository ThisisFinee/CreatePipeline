def rekursia(n):
    res = 0
    for i in range(len(n)):
        res+=int(n[i])
    if res<10:
        return res
    else:
        res = rekursia(str(res))
        return res
if __name__ == "__main__":
    n = str(input())
    print(rekursia(n))
        
    
    