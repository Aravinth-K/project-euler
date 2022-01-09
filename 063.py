"""
The 5-digit number, 16807=7^5, is also a fifth power.
Similarly, the 9-digit number, 134217728=8^9, is a ninth power.

How many n-digit positive integers exist which are also an nth
power?
"""

print(sum(1 for i in range(1, 10)
      for x in range(1, 100) if len(str(i**x)) == x))
