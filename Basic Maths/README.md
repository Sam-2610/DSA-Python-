# Basic Maths in DSA — Python Programs

A collection of beginner-friendly Python programs covering fundamental mathematical concepts commonly used in Data Structures and Algorithms (DSA).

---

## Programs Included

| # | File | Description | Difficulty |
|---|------|-------------|------------|
| 1 | `Factorial_of_a_Number.py` | Compute factorial using a while loop | Beginner |
| 2 | `Check_Prime.py` | Check if a number is prime | Beginner |
| 3 | `GCD_of_a_Number.py` | Find GCD using the Euclidean algorithm | Beginner |
| 4 | `Armstrong_Number.py` | Check if a number is an Armstrong number | Beginner |
| 5 | `Palindrome_Number.py` | Check if a number reads the same backwards | Beginner |
| 6 | `Reverse_the_Number.py` | Reverse the digits of a number | Beginner |
| 7 | `Counts_the_Digits.py` | Count the number of digits in a number | Beginner |
| 8 | `Divisior_of_a_Number.py` | Print all divisors of a number | Beginner |
| 9 | `Sorting.py` | Sort a list using Bubble Sort | Beginner |

---

## Program Details

### 1. Factorial of a Number
**File:** `Factorial_of_a_Number.py`

Calculates the factorial of a given number using a `while` loop.

- **Approach:** Iterative (while loop)
- **Key concept:** `n! = n × (n-1) × ... × 1`
- **Example:** `5! = 120`

```python
Input  : 5
Output : The Factorial of a Number is 120
```

---

### 2. Check Prime
**File:** `Check_Prime.py`

Checks whether a given number is prime by counting its divisors.

- **Approach:** Count divisors from 1 to n
- **Key concept:** A prime number has exactly 2 divisors — 1 and itself
- **Example:** 7 is prime, 9 is not

```python
Input  : 7
Output : Prime Number

Input  : 9
Output : Not a Prime Number
```

---

### 3. GCD of a Number
**File:** `GCD_of_a_Number.py`

Finds the Greatest Common Divisor (GCD) of two numbers using the Euclidean algorithm.

- **Approach:** Euclidean algorithm — `GCD(a, b) = GCD(b, a % b)`
- **Key concept:** Keep replacing the larger number with the remainder until one becomes 0
- **Example:** GCD(48, 18) = 6

```python
Input  : 48, 18
Output : The GCD of both numbers is : 6
```

---

### 4. Armstrong Number
**File:** `Armstrong_Number.py`

Checks whether a number is an Armstrong (Narcissistic) number.

- **Approach:** Sum of cubes of each digit
- **Key concept:** A number is Armstrong if the sum of cubes of its digits equals the number itself
- **Example:** 153 = 1³ + 5³ + 3³ = 153 ✓

```python
Input  : 153
Output : Armstrong Number

Input  : 100
Output : Not an Armstrong Number
```

> **Note:** This program checks for 3-digit Armstrong numbers (sum of cubes). For n-digit Armstrong numbers, the exponent should be the number of digits.

---

### 5. Palindrome Number
**File:** `Palindrome_Number.py`

Checks whether a number reads the same forwards and backwards.

- **Approach:** Reverse the digits and compare with original
- **Key concept:** Extract digits using `% 10`, build reversed number
- **Example:** 121 reversed is 121 → Palindrome

```python
Input  : 121
Output : Palindrome Number

Input  : 123
Output : Not a Palindrome
```

---

### 6. Reverse the Number
**File:** `Reverse_the_Number.py`

Reverses the digits of a given number.

- **Approach:** Extract last digit using modulo, build reversed number
- **Key concept:** `rev = rev * 10 + last_digit`
- **Example:** 1234 → 4321

```python
Input  : 1234
Output : The Reverse of the Number is 4321
```

---

### 7. Count the Digits
**File:** `Counts_the_Digits.py`

Counts the number of digits in a given number.

- **Approach:** Divide by 10 repeatedly until the number becomes 0
- **Key concept:** Each division by 10 removes one digit
- **Example:** 12345 has 5 digits

```python
Input  : 12345
Output : The Count of Digits in the Number is 5
```

---

### 8. Divisors of a Number
**File:** `Divisior_of_a_Number.py`

Prints all divisors of a given number.

- **Approach:** Loop from 1 to n, print if divisible
- **Key concept:** `i` is a divisor if `n % i == 0`
- **Example:** Divisors of 12 → 1 2 3 4 6 12

```python
Input  : 12
Output : 1 2 3 4 6 12
```

---

### 9. Sorting (Bubble Sort)
**File:** `Sorting.py`

Sorts a list of integers in ascending order using the Bubble Sort algorithm.

- **Approach:** Bubble Sort — compare and swap adjacent elements
- **Key concept:** Largest element "bubbles up" to the end in each pass
- **Time complexity:** O(n²)
- **Example:** [5, 3, 8, 1] → [1, 3, 5, 8]

```python
Input  : 4 elements → 5 3 8 1
Output : Sorted List : [1, 3, 5, 8]
```

---

## Concepts Covered

- **Loops** — `while` and `for` loops for iteration
- **Modulo operator (`%`)** — extracting digits, checking divisibility
- **Integer division (`//`)** — removing digits, halving numbers
- **Conditionals** — comparing values and branching logic
- **Lists** — collecting and sorting elements
- **Functions** — encapsulating logic in reusable blocks

---

## How to Run

Make sure you have Python 3 installed.

```bash
python Factorial_of_a_Number.py
python Check_Prime.py
python GCD_of_a_Number.py
python Armstrong_Number.py
python Palindrome_Number.py
python Reverse_the_Number.py
python Counts_the_Digits.py
python Divisior_of_a_Number.py
python Sorting.py
```

Each program will prompt you to enter input via the terminal.

---

## Author

**Satyam Sagar**
📧 satyamsagar827@gmail.com
```
