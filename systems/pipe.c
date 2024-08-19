#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

pthread_mutex_t resource1 = PTHREAD_MUTEX_INITIALIZER;
pthread_mutex_t resource2 = PTHREAD_MUTEX_INITIALIZER;

void* processA(void* arg) {
    pthread_mutex_lock(&resource1);
    printf("Process A locked Resource 1\n");
    sleep(1);  // Simulate some work
    printf("Process A trying to lock Resource 2\n");
    pthread_mutex_lock(&resource2);
    printf("Process A locked Resource 2\n");

    // Unlock resources
    pthread_mutex_unlock(&resource2);
    pthread_mutex_unlock(&resource1);
    
    printf("Process A finished\n");
    return NULL;
}

void* processB(void* arg) {
    pthread_mutex_lock(&resource2);
    printf("Process B locked Resource 2\n");
    sleep(1);  // Simulate some work
    printf("Process B trying to lock Resource 1\n");
    pthread_mutex_lock(&resource1);
    printf("Process B locked Resource 1\n");

    // Unlock resources
    pthread_mutex_unlock(&resource1);
    pthread_mutex_unlock(&resource2);

    printf("Process B finished\n");
    return NULL;
}

int main() {
    pthread_t threadA, threadB;

    pthread_create(&threadA, NULL, processA, NULL);
    pthread_create(&threadB, NULL, processB, NULL);

    pthread_join(threadA, NULL);
    pthread_join(threadB, NULL);

    return 0;
}
