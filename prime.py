def get_all_prime(n):
    if n > 1:
        for each in range(2, n):
            if all(each%i!=0 for i in range(2, each)):
                print(each)

if __name__ == '__main__':
    get_all_prime(100)
