import sys

def my_printf(original_str,swap_str):
    print(f"{original_str.replace('#k',swap_str.swapcase())}")

if __name__ == '__main__':
    data=sys.stdin.readlines()
    for i in range(0,len(data),2):
        my_printf(data[i].rstrip(),data[i+1].rstrip())
