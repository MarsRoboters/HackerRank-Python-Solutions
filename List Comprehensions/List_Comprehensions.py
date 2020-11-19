if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    X = x
    Y = y
    Z = z
    
    list = []
    
    ### This is the solution using the Loop
    
    # # for i in range(X+1):
    # #     for j in range(Y+1):
    # #         for k in range(Z+1):
    # #             if i + j + k != n:
    # #                 list.append([i,j,k])
    # # print(list)
    
    
    ### This is the solution using the List Comprehension
    
    list = [[i,j,k] for i in range(X+1) for j in range(Y+1) for k in range(Z+1) if i + j + k != n ]
    print(list)
        
