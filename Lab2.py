def display_main_menu():
    print("Enter some numbers separated by commas: ")
    return 0

def get_user_input():
    datalist = [int(x) for x in input().split(',')]
    return datalist

def calc_average(datalist):
    mean = sum(datalist)/len(datalist)
    print("Average number is ",mean)
    return mean

def find_min_max(datalist):
    min = max = datalist[0]
    i = 0
    for i in range(0,len(datalist)):
        if max < datalist[i]:
            max = datalist[i]
        elif min > datalist[i]:
            min = datalist[i]
    int_list = [min, max]
    print("Minimum and maximum number are ",int_list)
    return 0

def sort_temperature():
    print("sort_temperature")
    return 0

def calc_median_temperature():
    print("calc_median_temperature")
    return 0

def main():
    display_main_menu()
    datalist = get_user_input()
    calc_average(datalist)
    find_min_max(datalist)
    sort_temperature(datalist)
    calc_median_temperature(datalist)
if __name__ == '__main__':
    main()
