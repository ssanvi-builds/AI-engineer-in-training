### Insight 1

Functions can return values, but they are lost if not stored. I had that problem when using your_move() without assigning it to a variable inside the main(). The correct flow was.

 ```python
def main():
    user_move = your_move() # stored and available inside main()
```
Then , I could pass those variables as parameters to other functions such as the compare() function.

### Insight 2

It's a good practice to handle global variables inside the main() function. Initially I was handling them inside the inner functions such as compare(). If inner functions like  compare() modify globals directly with global, you can't trace where a value changed without reading every function. Passing data as parameters and returning results makes the flow visible: you can see exactly what goes in and what comes out of each function.