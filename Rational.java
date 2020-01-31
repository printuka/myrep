public class Rational {

private int num;
private int den;

    public static void main(String[] args) {
       
    }

    public Rational(int numerator, int denominator) {

        if (denominator == 0) {
            throw new ArithmeticException("denominator is zero");
        }
        int g = gcd(numerator, denominator);
        num = numerator   / g;
        den = denominator / g;
        if (den < 0) { den = -den; num = -num; }
    }

public Rational plus(Rational b) {
        Rational a = this;
        int f = gcd(a.num, b.num);
        int g = gcd(a.den, b.den);
        Rational s = new Rational((a.num / f) * (b.den / g) + (b.num / f) * (a.den / g),lcm(a.den, b.den));
        s.num *= f;
        return s;
    }

    private static int gcd(int m, int n) {
        if (m < 0) m = -m;
        if (n < 0) n = -n;
        if (0 == n) return m;
        else return gcd(n, m % n);
    }

    private static int lcm(int m, int n) {
        if (m < 0) m = -m;
        if (n < 0) n = -n;
        return m * (n / gcd(m, n));
    }

    public Rational minus(Rational b) {
        Rational a = this;
        return a.plus(b.negate());
    }

    public Rational negate() {
        return new Rational(-num, den);
    }

    public Rational times(Rational b) {
        Rational a = this;
        Rational c = new Rational(a.num, b.den);
        Rational d = new Rational(b.num, a.den);
        return new Rational(c.num * d.num, c.den * d.den);
    }

    public Rational dividedBy(Rational b) {
        Rational a = this;
        return a.times(b.reciprocal());
    }

    public Rational reciprocal() {
        return new Rational(den, num);
   }

    public int numerator() {
	return num;
    }

    public int denominator() {
	 return den; 
    }

    public boolean equals(Object y) {
        if (y == null) return false;
        if (y.getClass() != this.getClass()) return false;
        Rational b = (Rational) y;
        return compare(b) == 0;
    }

    public int compare(Rational b) {
        Rational a = this;
        int lhs = a.num * b.den;
        int rhs = a.den * b.num;
        if (lhs < rhs) return -1;
        if (lhs > rhs) return +1;
        return 0;
    }

    public String toString() {
        if (den == 1) return num + "";
        else          return num + "/" + den;
    }
}
