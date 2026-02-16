def main ():
    matrix = [
        [1, 2, 3, 5],
        [6, 7, 8, 9],
        [10, 11, 12, 13],
    ]

    for index in range(0, len(matrix)):
        a = matrix[index]
        # print (a)
        for dindex in range(0, len(a)):
            b = a[dindex]
            if (index+1) %2 == 0 and dindex %2 == 0 and (b+1)%2 == 0 :
                print (b)




            print(b)
main()
