ch string received as argument, it creates a thread that counts
the number of vowels and the number of digits in the string.
Then the thread adds the numbers to two global variables, one for vowels,
     one for digits.
     The main program waits for all the threads to be done, then prints the
     number of vowels and the number of digits.

     Example:
     ./prog wgsv2 ab4ee kfddi 152

     number of vowels: 4
     number of digits: 5*/
#include <stdlib.h>
#include <stdio.h>
#include <pthread.h>
#include <string.h>

pthread_mutex_t mtx;
int vowels,digits;

void *f(void *arg)
{
	int vowelsLocal=0,digitsLocal=0;
	char *s = *(char**)arg;
	int i;
	for(i=0;i<strlen(s);i++){
		if(strchr("0123456789",s[i]))
			digitsLocal++;
		if(strchr("aeiouAEIOU",s[i]))
			vowelsLocal++;
	}
	pthread_mutex_lock(&mtx);
	vowels+=vowelsLocal;
	digits+=digitsLocal;
	pthread_mutex_unlock(&mtx);
	return NULL;
}

int main(int argc,char **argv){
	pthread_t t[argc-1];
	pthread_mutex_init(&mtx,NULL);
	int i;
	for(i=0;i<argc-1;i++){
		printf("%s\n",argv[i+1]);
	}
	for(i=0;i<argc-1;i++){
		pthread_create(&t[i],NULL,f,&argv[i+1]);
	}
	for(i=0;i<argc-1;i++){
		pthread_join(t[i],NULL);
	}
	pthread_mutex_destroy(&mtx);
	printf("Digits:%d\nVowels:%d\n",digits,vowels);
	return 0;
}
