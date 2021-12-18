#include <math.h>
#include <vector>
#include <cstdint>
#include <iostream>

// All decorator-list using statements
// (e.g.: Explicit Python function/class package imports)
using std::cout;
using std::string;
using std::to_string;
using std::vector;

vector<int> prime_factors(int64_t n) {
    vector<int> factors;
    int max_prime = -1;

    while (!(n % 2)) {
        factors.push_back(2);
        n >>= 1;
    }
    while (!(n % 3)) {
        factors.push_back(3);
        n = int64_t(n / 3);
    }
    int i = 5;
    int root = sqrt(n);
    while (i <= root) {
        while (!(n % i)) {
            max_prime = i;
            factors.push_back(max_prime);
            n = int64_t(n / i);
        }
        while (!(n % (i + 2))) {
            max_prime = i + 2;
            factors.push_back(max_prime);
            n = int64_t(n / (i + 2));
        }
        i += 6;
    }
    if (n > 4) {
        max_prime = n;
        factors.push_back(max_prime);
    }

    return factors;
}

int main(int argc, char** argv) {
    cout << "Number to report prime factors for: " + string(argv[1]) + "\n";
    vector<int> factors = prime_factors(atoi(argv[1]));
    string str_factors = "";
    for (size_t i = 0; i < factors.size(); i++) {
        if (i != 0)
            str_factors += ", ";
        str_factors += to_string(factors[i]);
    }
    cout << "The factors are: " + str_factors + "\n";
}
