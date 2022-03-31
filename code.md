---
title: Code Snippets
---
Creating a Factorial Class
```
class Factorial:

    def __call__(self, n):
        f = 1
        for i in range(1, n + 1):
            f = f * i
        return f

# Factorial tester
def facTester():
    for i in range(11):
        # create instance of class
        myOb = Factorial()
        # calculate factorial of i
        answer = myOb(i)
        print("The factorial of %d is %d" % (i, answer))

```
