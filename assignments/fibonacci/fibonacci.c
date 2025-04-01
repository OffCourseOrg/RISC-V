#include <stdio.h>

int fibonacci(int k) {
  if (k == 0 || k == 1) {
    return 1;
  }
  return fibonacci(k - 1) + fibonacci(k - 2);
}

int main(void) {
  int k, n;
  scanf("%d", &k);
  n = fibonacci(k);
  printf("%d\n", n);
  return 0;
}
