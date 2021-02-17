# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from playwright import sync_playwright

from taobao2 import run as tao2run

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    with sync_playwright() as playwright:
        tao2run(playwright)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
