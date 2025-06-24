#include <stdio.h>
#include <math.h>

double f(double x) {
  return cos(x) - pow(x, 2);
}

double bisection(double a, double b, double tol) {
  if (f(a) * f(b) >= 0) {
    printf("Error: f(a) and f(b) must have opposite signs.\n");
    return -1;  // 区間の選択が間違っている場合はエラーを返す
  }

  double c = a;
  int iter = 0;
  while (fabs(b-a) / 2 > tol) {
    c = (a + b) / 2;
    if (f(c) == 0.0)
      break;  // cが根の場合、ループを抜ける
    else if (f(c) * f(a) < 0)
      b = c;
    else
      a = c;
    iter++;
    fprintf(stdout,"%d,%le,%le\n",iter,fabs(b-a)/ 2,c);
  }
  fprintf(stderr,"iter: %d\n",iter);
  return c;
}

int main() {
  double a = 0.0, b = 1.0, tol = 0.00001;
  double root = bisection(a, b, tol);

  if (root != -1) {
    fprintf(stderr,"An approximate root is: %f\n", root);
    }

    return 0;
}
