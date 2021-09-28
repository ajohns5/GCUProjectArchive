//Austin Johns
//CST-315
//William Hurst
//This source file is for the operating system Semaphores.

#include <stdio.h>
#include <pthread.h>
#include <semaphore.h>
#include <unistd.h>

sem_t mutex;

void* thread(void* arg)
{
	//Waiting operator
	sem_wait(&mutex);
	printf("\nEntered..\n");

	//Defining critical Section
	sleep(4);

	//Operation of signal
	printf("\nJust Exiting...\n");
	sem_post(&mutex);
}


int main()
{
	sem_init(&mutex, 0, 1); //Starting mutex lock
	pthread_t thread1, thread2; //Creation of two different threads
	pthread_create(&thread1, NULL, thread, NULL); //Defining thread 1
	sleep(2);
	pthread_create(&thread2, NULL, thread, NULL); //Defining thread 2
	//running both threads simultaneously for synchronization 
	pthread_join(thread1, NULL);
	pthread_join(thread2, NULL);
	sem_destroy(&mutex); //deletes the mutex lock
	return 0;
}