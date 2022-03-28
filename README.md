# Funk

A simple class that allows to work with real-valued functions using a mathematical syntax  

## Usage 

You just need to import
```
 from funk import Funk
 ```

Then you create a variable: the simplest function possible
```
 x = Funk()
```

You can then create custom functions starting from x
```
 f = (x**2 + 2*x + 8)**0.5

 f(2)   # Returns 4.0
 ```

 You can integrate non-funk functions, also coming from other libraries
 ```
 from numpy import exp

 x = Funk()
 f = x*exp
 ```

 And you can "cast" them into Funktions, to add functionalities
 ```
 from numpy import exp
 exp = Funk(exp)

 f = exp*2 + 3
 ```
