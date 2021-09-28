//Austin Johns
//CST-315
//William Hurst
//This source file is for the operating system monitors.

#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <unistd.h>

pthread_mutex_t my_mutex = PTHREAD_MUTEX_INITIALIZER;
pthread_cond_t myConditionVar = PTHREAD_COND_INITIALIZER;

int threadID = 0; //ID for which thread is being used

//Implementing Thread 1
void* thread1(void* p) {
	sleep(rand() % 5); //Small delay for synchronization
	printf("Entered Thread 1\n");
	pthread_mutex_lock(&my_mutex); //locks thread 2 from running
	threadID++; //incrementing ID
	pthread_cond_signal(&myConditionVar); //sets met condition across all semaphores and monitors
	pthread_mutex_unlock(&my_mutex); //unlocking mutex 
}


void* thread2(void* p) {
	sleep(rand() % 5);

	printf("Entered Thread #2\n");
	pthread_mutex_lock(&my_mutex);
	threadID = 2;
	threadID++;
	pthread_cond_signal(&myConditionVar);
	pthread_mutex_unlock(&my_mutex);
}

int main()
{
	srand(time(0));
	//Creating thread 1
	pthread_t P_thread1;
	pthread_create(&P_thread1, NULL, thread1, NULL);
	//creating thread 2
	pthread_t P_thread2;
	pthread_create(&P_thread2, NULL, thread2, NULL);
	//locking the mutex as an initial rule
	pthread_mutex_lock(&my_mutex);
	while (threadID < 2) {
		printf("%d", threadID);
		printf("\n");
		//mutex is unlocked once condition is met
		pthread_cond_wait(&myConditionVar, &my_mutex);
	}
	//ends with locking the mutex after process is completed.
	pthread_mutex_unlock(&my_mutex);
	return (EXIT_SUCCESS);
}
