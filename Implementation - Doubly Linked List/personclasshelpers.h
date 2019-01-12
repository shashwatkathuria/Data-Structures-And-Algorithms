#include<iostream>
#include<string.h>
#include<stdlib.h>
#include<ctype.h>
using namespace std;

int strcmpi(char s1[],char s2[]);
class Person
{
  public:

      char firstname[15];
      char lastname[15];
      int age;
      Person()
      {
          strcpy(firstname, "ND");
          strcpy(lastname, "ND");
          age = 0;
      }
      Person(char fname[], char lname[], int a)
      {
          strcpy(firstname, fname);
          strcpy(lastname, lname);
          age = a;
      }
      void display();
      string getName();
      int getAge();
      void setAge(int a);
      void setName(char fname[], char lname[]);
      bool operator<(Person p);
      bool operator>(Person p);
      bool operator==(Person p);

};

void Person::display()
{
    cout<<endl<<"Name  :"<<getName()<<" || Age  : "<<getAge()<<endl;
}


string Person::getName()
{
    char fullname[30];
    strcpy(fullname, firstname);
    strcat(fullname, " ");
    strcat(fullname, lastname);
    return fullname;
}

int Person::getAge()
{
    return age;
}

void Person::setAge(int a)
{
    age = a;
}
void Person::setName(char fname[], char lname[])
{
    strcpy(firstname, fname);
    strcpy(lastname, lname);
}

bool Person::operator<(Person p)
{
    if (age == p.getAge())
    {
        if (strcmpi(firstname, p.firstname) < 0)
            return true;
        else
            return false;
    }
    else
    {
        return age < p.getAge();
    }
}
bool Person::operator>(Person p)
{
    if (age == p.getAge())
    {
        if (strcmpi(firstname, p.firstname) > 0)
            return true;
        else
            return false;
    }
    else
    {
        return age > p.getAge();
    }
}
bool Person::operator==(Person p)
{
    return age == p.getAge();
}

int strcmpi(char s1[],char s2[])
{
    char s3[15];
    char s4[15];
    strcpy(s3,s1);
    strcpy(s4,s2);
    for(int i=0;s3[i]!=0;i++)
    {
        s3[i]=toupper(s3[i]);
    }
    for(int i=0;s2[i]!=0;i++)
    {
        s4[i]=toupper(s4[i]);
    }
    return strcmp(s3,s4);

}