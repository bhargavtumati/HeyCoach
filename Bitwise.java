/*Problem Statement (Practice)

Title: Demonstrate Bitwise Left Shift and Right Shift Operators

Problem

Write a Java program to demonstrate the use of the bitwise left shift (<<) and bitwise right shift (>>) operators.

The program should:

Perform a left shift on an integer.
Perform a right shift on an integer.
Print the results.
Example

Input

Number = 1
Shift = 2

Output

Bitwise right: 0
Bitwise left: 4
Explanation

The binary representation of 1 is:

0001

Right Shift (>> 2)

0001 >> 2

0000

Decimal = 0

Left Shift (<< 2)

0001 << 2

0100

Decimal = 4
Notes
x << n shifts the bits of x to the left by n positions, which is equivalent to multiplying by 2
n
 (when no overflow occurs).
x >> n shifts the bits of x to the right by n positions, which is equivalent to integer division by 2
n
 for non-negative numbers. */



class Bitwise{
    public static void main(String args[]){
        System.out.println("Bitwise right: "+(1>>2));  //0001 >> 2 = 00 = 0
        System.out.println("Bitwise left: "+(1<<2)); //0001 << 2= 000100 = 4
    }
}