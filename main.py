from brackets import check_brackets

def main():
    print('You can check does the brackets in right position!')
    if check_brackets(input('Insert brackets here: ')):
        print('Сбалансированно')
    else:
        print('Несбалансированно')
    print('Done!')



if __name__ == '__main__':
    main()