if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    arr = list(arr)
    sorted_list = sorted(arr)
    
    n = len(sorted_list)
    maxi = sorted_list[n-1]
    for i in range(n - 1, -1, -1):
        if sorted_list[i] < maxi:
            second_maxi = sorted_list[i]
            break
    print(second_maxi)
