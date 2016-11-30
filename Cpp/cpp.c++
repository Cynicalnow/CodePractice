#include <iostream>
#include <string>

#define endl std::endl

using std::cout;
using std::string;

int main () {
   string str1 = "Hello";
   string str2 = "World";
   string str3;
   int  len ;

   cout << "str1 : " << str1 << endl;
   cout << "str2 : " << str2 << endl;

   // copy str1 into str3
   str3 = str1;
   cout << "str3 : " << str3 << endl;

   // concatenates str1 and str2
   str3 = str1 + str2;
   cout << "str1 + str2 : " << str3 << endl;

   // total lenghth of str3 after concatenation
   len = str3.size();
   cout << "str3.size() :  " << len << endl;

   return 0;
}