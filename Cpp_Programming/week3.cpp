#include<iostream>
#include<string>
#include<cmath>
using namespace std;
int main(){
//	int a=12;
//	int* ptr = &a;
//	std::cout<<"Adress of a is:- "<<ptr;


//======Array======
//	char list[]={'a','b'};
//	int arr[]={1,2,3,4,5};
//	int size=sizeof(arr);
//	std::cout<<"Size of arr is:- "<<size<<endl;
//	std::cout<<arr[3];
//	for(int i=0; i<=6;i++){
//		std::cout<<"Iteratrion exiting on index no. :- "<<i<<endl;
//		std::cout<<"Value is "<<arr[i]<<endl;
//	}

//	Methods in math & string
//	int a=12;
//	float f=23.908654;
//	std::cout<<"Power:- "<<pow(a,2);
//	std::cout<<"Power:- "<<ceil(f);

//0 1 2 3 4 5
//size 6
//index 0 se 5

char name[]={0,1,2,3,4,5};
name[0]='A';
name[1]='y';
name[2]='e';
name[3]='s';
name[4]='h';
name[5]='a';
	for(int i=0; i<=6;i++){
		std::cout<<name[i]<<" ";
	}
//	std::cout<<"Name:- "<<name[];
//std::cout<<"Length:-"<<name.length();
 	return 0;
}
