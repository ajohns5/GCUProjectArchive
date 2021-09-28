//Austin Johns
//CST-315
#include <pthread.h> 
#include <stdio.h> 
#include <unistd.h> 
  
//Defining thread condition variable
pthread_cond_t cond1 = PTHREAD_COND_INITIALIZER; 
  
//Defining the mutex lock
pthread_mutex_t lock = PTHREAD_MUTEX_INITIALIZER; 
  
int done = 1; 
  
//Function for thread
void* foo() 
{ 
  
    //create the mutex lock 
    pthread_mutex_lock(&lock); 
    if (done == 1) { 
  
        //Waiting on the condition variable (First condition) 
        done = 2; 
        printf("Waiting for condition variable to be ready\n"); 
        pthread_cond_wait(&cond1, &lock); 
    } 
    else { 
  
        //Signaling the condition variable 
        printf("Signaling the condition variable\n"); 
        pthread_cond_signal(&cond1); 
    } 
  
    //releasing mutex lock 
    pthread_mutex_unlock(&lock); 
  
    printf("Returning thread\n"); 
  
    return NULL; 
} 
  
//MAIN 
int main() 
{ 
    pthread_t tid1, tid2; 
  
    // Create thread 1 
    pthread_create(&tid1, NULL, foo, NULL); 
  
    //pause for one second to ensure that thread1 runs first without interruption 
    sleep(1); 
  
    //Beginning of thread 2 
    pthread_create(&tid2, NULL, foo, NULL); 
  
    //pause for thread 2 to finish
    pthread_join(tid2, NULL); 
  
    return 0; 
} 