######################################################################
# Author: Dimitrios Ntentia and Natinael Abebe
# Username: ntentiad abeben

# Assignment: A08: UPC Barcodes
#
# Purpose: Determine the validity of a barcode
#
######################################################################
# Acknowledgements:
#
# None: Original work

# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################
import turtle

def is_valid_input(barcode):
    if len(str(barcode)) == 12 and type(int(barcode)) == int:
        return True
    else:
        return False

def addOdd(barcode):
    listy = []
    for i in str(barcode):
        listy.append(int(i))

    oddsum = listy[0]
    for i in range(len(listy)):
        if ((i + 1) % 2) == 0 and i > 2:
            oddsum += listy[i - 1]
    return (oddsum)

def addEven(barcode):
    listy = []
    for i in str(barcode):
        listy.append(int(i))

    evensum = 0
    for i in range(len(listy)):
        if (i % 2) == 0 and i < 11 and i > 1:
            evensum += listy[i - 1]
    return (evensum)

def remainder(barcode):
    mastersum=addOdd(barcode)*3+addEven(barcode)
    if mastersum%10==0:
        return 0
    else:
        return (mastersum - ((mastersum // 10)*10))

def is_valid_modulo(barcode):
    temp=remainder(barcode)
    listy = []
    for i in str(barcode):
        listy.append(int(i))

    if temp==listy[11]:
        return True
    else:
        return False


def translate(barcode_num, side):
    dict = {0: "0001101", 1: "0011001", 2: "0010011", 3: "0111101", 4: "0100011", 5: "0110001", 6: "0101111",
            7: "0111011", 8: "0110111", 9: "0001011"}
    dict2 = {0: "1110010", 1: "1100110", 2: "1101100", 3: "1000010", 4: "1011100", 5: "1001110", 6: "1010000",
            7: "1000100", 8: "1001000", 9: "1110100"}
    binary=""
    listy = []
    for i in str(barcode_num):
        listy.append(int(i))
    if side=="up":
        for i in listy[0:5]:
            binary+= dict[i]
        for i in listy[5:11]:
            binary += dict2[i]
    else:
        for i in listy[0:5]:
            binary+= dict2[i]
        for i in listy[5:11]:
            binary += dict[i]
    return binary


def main():
    input_code = input("Enter a 12 digit code [0-9]: ")
    if is_valid_input(input_code):
        if is_valid_modulo(input_code):
            print(translate(input_code, "up"))
            pass
        else:
            print("Error Message")
            pass
    else:
        main()

if __name__ == "__main__":
    main()
