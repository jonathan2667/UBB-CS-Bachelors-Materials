/*Write a c program that recives as command line arguments as many files containig random text. 
For each such file the program will create a thread. Each thread will recive as argument a file. 
All threads will have access to 2 global variables. 
Each thread will count the letter and the digits from the file it recived as argument 
and will add each of these 2 values to the global variables mentioned earlier. 
The threads must be dynamically allocated in memory. 
The access to the global variables must be efficiently synchronized using mutex variables 
(putting a mutex_lock at the begnnig of the thread and mutex_unlock at the end of the thread 
IS NOT EFFICIENT SYNCHRONIZATION) NOTE: When you compile use the -pthread obtion. 
The source file must be compiled using gcc with -Wall -g options WITHOUT WARNINGS OR SYNTAX ERRORS!!! 
Memory leaks and zombie processes are not allowed.*/



#include <stdlib.h>
#include <stdio.h>
#include <pthread.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>


typedef struct
{
        char* file;
} arg_t;

pthread_mutex_t ml, md; /// a mutex for letters and one for digits;

int l, d; /// letter and digit count

void* thread(void* arg){
        arg_t a = *(arg_t*)arg;
        FILE* fd = fopen(a.file, "r");

        char c;

        while(fscanf(fd, "%c", &c) != EOF){
                if(c >= '0' && c <= '9'){
                        pthread_mutex_lock(&md);
                        d++;
                        pthread_mutex_unlock(&md);
                }
                if((c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z')){
                        pthread_mutex_lock(&ml);
                        l++;
                        pthread_mutex_unlock(&ml);
                }
        }

        fclose(fd);
        free(arg);
        return NULL;
}

int main(int argc, char** argv)
{
        pthread_t *t;
        t = malloc((argc - 1) * sizeof(pthread_t));

        pthread_mutex_init(&ml, 0);
        pthread_mutex_init(&md, 0);

        int i;
        for(i = 0; i < argc - 1; i++){
                arg_t* a;
                a = malloc(sizeof(arg_t));
                a->file = argv[i+1];
                pthread_create(&t[i], 0, thread, (void*)a);
        }

        for(i = 0; i < argc - 1; i++){
                pthread_join(t[i], 0);
        }

        printf("l=%d\nd=%d\n", l, d);
        pthread_mutex_destroy(&ml);
        pthread_mutex_destroy(&md);

        free(t);
        return 0;
}


