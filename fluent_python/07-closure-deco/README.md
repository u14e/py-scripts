- Python 如何计算装饰器句法 
- Python 如何判断变量是不是局部的
- 闭包存在的原因和工作原理
- nonlocal 能解决什么问题

装饰器可能会处理被装饰的函数，然后把它返回，或者将其替换成另一个函数或可调用对象
装饰器在加载模块时立即执行

闭包指延伸了作用域的函数，其中包含函数定义体中引用、但是不在定义体中定义的非全局变量。函数是不是匿名的没有关系，关键是 **它能访问定义体之外定义的非全局变量**

闭包是一种函数，它会保留定义函数时存在的**自由变量**的绑定， 这样调用函数时，虽然定义作用域不可用了，但是仍能使用那些绑定

`nonlocal` 它的作用是把变量标记为自由变量，即使在函数中为变量赋予新值了，也会变成自由变量。