# Day 21: Generics
<br>

#### Objective

Today we're discussing Generics; be aware that not all languages support this construct, so fewer languages are enabled for this challenge.

<br>

#### Task

Write a single generic function named printArray; this function must take an array of generic elements as a parameter (the exception to this is C++, which takes a vector). The locked Solution class in your editor tests your function.

Note: You must use generics to solve this challenge. Do not write overloaded functions.

<br>

#### Input Format

The locked Solution class in your editor will pass different types of arrays to your printArray function.

<br>

#### Constraints

* You must have exactly `1` function named printArray.


<br>

#### Output Format

Your printArray function should print each element of its generic array parameter on a new line.

<br>

## Solution in Java 8


```java
import java.util.*;

class Printer <T> {
 public static <Element> void printArray(Element[] array) {
        for (Element element : array) {
            System.out.println(element);
        }

    }
}

public class Generics {
    
    public static void main(String args[]){
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        Integer[] intArray = new Integer[n];
        for (int i = 0; i < n; i++) {
            intArray[i] = scanner.nextInt();
        }

        n = scanner.nextInt();
        String[] stringArray = new String[n];
        for (int i = 0; i < n; i++) {
            stringArray[i] = scanner.next();
        }
        
        Printer<Integer> intPrinter = new Printer<Integer>();
        Printer<String> stringPrinter = new Printer<String>();
        intPrinter.printArray( intArray  );
        stringPrinter.printArray( stringArray );
        if(Printer.class.getDeclaredMethods().length > 1){
            System.out.println("The Printer class should only have 1 method named printArray.");
        }
    } 
}
```

<br>
