//Kristen Printup, Ashley Abel, Allison Ryan
#include<iostream>
#include<fstream>
#include<cstdlib>

using namespace std;

class rational
{
public:

rational (int n, int d)
{
num=n;
denom=d;
}

rational(int n)
{
num=n;
denom=1;
}

rational display()
{
        if (denom==0)
        {
        cerr<<"Error: Cannot have 0 for a denominator. Now Exiting."<<endl;
        exit(-1);
        }

        if (denom<0)
        {
        denom = denom * -1;
        num = num * -1;
        }

int gcd=0;
int max=0;
if (denom>=num)
{
max=denom;
}

else
{
max=num;
}
	for (int i=1; i<=max; i++)
	{
		if(num%i==0 && denom%i==0)
		{
		gcd=i;
		}
	}
cout<<num/gcd<<"/"<<denom/gcd<<endl;
}

rational add(const rational r)
{
	int num_new = (this->num * r.denom) + (this->denom * r.num);
	int dem_new = this->denom * r.denom;
	rational r_new(num_new, dem_new);
	//cout << r_new.num << "/" << r_new.denom << endl;

	return r_new;
}

rational sub(const rational r)
{
	int num_new = (this->num * r.denom) - (this->denom * r.num);
	int dem_new = (this->denom * r.denom);
	rational r_new(num_new, dem_new);
	//cout << r_new.num << "/" << r_new.denom << endl;

	return r_new;
}

rational mul(const rational r)
{
	int num_new = (this->num * r.num);
	int dem_new = (this->denom * r.denom);
	rational r_new(num_new, dem_new);
	//cout << r_new.num << "/" << r_new.denom << endl;

	return r_new;
}

rational div(const rational r)
{
	int num_new = (this->num * r.denom);
	int dem_new = (this->denom * r.num);
	rational r_new(num_new, dem_new);
	//cout << r_new.num << "/" << r_new.denom << endl;

	return r_new;
}

bool less(rational x, rational y)
{
	if((x.num * y.denom)<(y.num * x.denom))
	{
	return true;	
	}

	else if((x.num * y.denom)>(y.num * x.denom))
	{
	return false;
	}
}

bool equal(rational x, rational y)
{
        if((x.num * y.denom)==(y.num * x.denom))
        {
        return true;
        }

        else
        {
        return false;
        }
}

rational neg()
{
num=(-num);
}

void output(ofstream& y)
{
y.open("file.txt");
y<<num<<"/"<<denom;
y.close();
}

void input(ifstream& y)
{
y.open("file1.txt");
int x;
int z;
while(y>>x>>z)
{
	if(z==0)
	{
	cerr<<"Error: Cannot have 0 for a denominator. Now Exiting."<<endl;
        exit(-1);
	}
}
int gcd=0;
int max=0;
if (z>=x)
{
max=z;
}

else
{
max=x;
}
        for (int i=1; i<=max; i++)
        {
                if(x%i==0 && z%i==0)
                {
                gcd=i;
                }
        }
cout<<x/gcd<<"/"<<z/gcd<<endl;
y.close();
}

~rational() //destructor
{
}

private:
int num;
int denom;

};

int main()
{
//rational z(9,0) UNCOMMENTING THIS WILL CAUSE THE PROGRAM TO ABORT (DENOM=0)
cout<<"1st rational: ";
rational a(2,-3);
a.display();

cout<<"2nd rational: ";
rational b(4,5);
b.display();

ofstream ofs;
a.output(ofs); //write 1st rational to file.txt

cout<<"Rational number read from file: ";
rational g(1,1);
ifstream ifs;
g.input(ifs);

cout<<"Rational with single int parameter: ";
rational q(6);
q.display();

cout<<"Rational 1 + Rational 2: ";
rational c = a.add(b);
c.display();

cout<<"Rational 1 - Rational 2: ";
rational c1 = a.sub(b);
c1.display();

cout<<"Rational 1 * Rational 2: ";
rational c2 = a.mul(b);
c2.display();

cout<<"Rational 1 / Rational 2: ";
rational c3 = a.div(b);
c3.display();

if (c.less(a, b)==true && c.equal(a, b)==false)
{
cout<<"1st rational is less than the 2nd rational"<<endl;
}

else if (c.less(a, b)==false && c.equal(a, b)==false)
{
cout<<"1st rational is greater than the 2nd rational"<<endl;
}

else
{
cout<<"1st rational is equal to the 2nd rational"<<endl;
}

cout<<"Negative of 1st rational: ";
a.neg();
a.display();

cout<<"Negative of 2nd rational: ";
b.neg();
b.display();

return 0;
}
