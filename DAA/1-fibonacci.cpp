//  recursive

// #include <iostream>

// int recursiveFibonacci(int n) {
//     if (n <= 1)
//         return n;
//     return recursiveFibonacci(n - 1) + recursiveFibonacci(n - 2);
// }

// int main() {
//     int n = 1; // Change n to the desired Fibonacci number
//     std::cout << "Fibonacci(" << n << ") = " << recursiveFibonacci(n) << std::endl;
//     return 0;
// }


// non-recursive

#include <iostream>

int nonRecursiveFibonacci(int n) {
    if (n <= 1)
        return n;
    
    int a = 0, b = 1, result;
    for (int i = 2; i <= n; i++) {
        result = a + b;
        a = b;
        b = result;
    }
    return result;
}

int main() {
    int n = 10; // Change n to the desired Fibonacci number
    std::cout << "Fibonacci(" << n << ") = " << nonRecursiveFibonacci(n) << std::endl;
    return 0;
}
