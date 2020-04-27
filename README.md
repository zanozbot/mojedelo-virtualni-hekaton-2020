# MojeDelo Virtual Hackathon Entry

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Maximize the number of pixels a single character of input text can occupy on the given screen size without splitting any words.

## Instructions

### LedDisplay

You've just received an order from MojaTrgovina. The client wants the customer to be able to scan a product's bar code and display its name, price, and description on an LCD screen. All of the scanned items have to be displayed on the screen. Different stores in Slovenia use different screen sizes, but all of them are rectangular. The width and height of the screen are given below, together with the description of the product. To take advantage of the full screen, you must find a way to maximize character pixel size and still be able to display the whole text without splitting any of the words. All characters must have the same width and height (eg. "I" and "m" occupy the same horizontal space as the character space does). There is no extra space between adjacent characters or adjacent lines.

### Input

Each line of input text contains a test case in the form of "W H T". W is the width and H is the height of the screen in pixels. T is the text that should appear on the screen.

### Output

The output contains a maximized character size in one line for each test case.  If the text cannot be displayed the return the value 0.

### What to submit?

Below you will find test cases that need to be solved by your algorithm. Alongside the results, you must also submit a ZIP archive containing your solution.

```
27 15 May the Force be with you
10 40 Legen wait-for-it dary, legendary
420 100 You want the truth? You can't handle the truth
65 65 Houston, we have a problem
345 160 My mama always said life was like a box of chocolates. You never know what you're gonna get
230 130 You know nothing, Jon Snow
14 10 Dobby is free
15 80 Say 'hello' to my little friend!
100 15 Live long and prosper
23 2 Bazinga
```

### Example
```
Input:
20 6 led display
100 20 led display 2020
10 20 MUST BE ABLE TO DISPLAY
55 25 Can you hack
100 20 display product text

Output:
2
9
1
8
8
```

## Solution

### Instructions
The solution is written in [Python](https://www.python.org/). We start the algorithm with the following command.

```bash
python solution.py vhod.txt
```

In case we don't supply the program an argument it returns some helpful information.

```bash
$ python solution.py
Vhodna datoteka ni bila podana.
Delovanje: python solution.py <vhod.txt> <zacni_novo_vrstico_s_presledkom>
<vhod.txt> - Ime datoteke z vhodi
<zacni_novo_vrstico_s_presledkom> - False ali True

$ python solution.py ni_vhodov.txt
Vhodna datoteka "ni_vhodov.txt" ni bila najdena.
```


### Algorithm
Firstly, we use a mathematical formula to find the maximum number of pixels a single character can occupy. Then, using bisection we find the result. A more detailed description can be found in the source code.
([solution.py](https://github.com/zanozbot/mojedelo-virtualni-hekaton-2020/blob/master/solution.py)).

### Results
```
Input:
27 15 May the Force be with you
10 40 Legen wait-for-it dary, legendary
420 100 You want the truth? You can't handle the truth
65 65 Houston, we have a problem
345 160 My mama always said life was like a box of chocolates. You never know what you're gonna get
230 130 You know nothing, Jon Snow
14 10 Dobby is free
15 80 Say 'hello' to my little friend!
100 15 Live long and prosper
23 2 Bazinga

Here we consider a space as a valid character in a new line
$ python solution.py vhodi.txt True

3
0
25
8
22
26
2
2
7
2

Here we don't consider a space as a valid character in a new line
$ python solution.py vhodi.txt False

3
0
26
8
22
28
2
2
7
2
```
