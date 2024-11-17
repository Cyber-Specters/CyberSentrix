// socat TCP-LISTEN:5000,reuseaddr,fork EXEC:./p2,stderr,pty,cfmakeraw <- to make it public 
// gcc -g -o p2 p2.c 

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define NAME_MAX_LENGTH 32
#define HELP_MAX_LENGTH 40

unsigned int thisPersonNeedHelp = 4294967293;
unsigned char count = 5;

void banned();
void handleUser(const char *name);
void printStatus();
void checkAndPrintFlag();

int main() {
    puts("Help Responder");
    char name[NAME_MAX_LENGTH];

    while (1) {
        puts("Enter name: ");
        scanf("%s", name);
        handleUser(name);
        printStatus();
        checkAndPrintFlag();

        count++;
    }

    return 0;
}

void handleUser(const char *name) {
    if (count == 0) {
        printf("wh0pz why u are here, but btw Congrats %s.\n", name, count);
        banned();
    } else {
        printf("Sorry %s under dev\n", name, count);
    }
}

void banned() {
    char help[HELP_MAX_LENGTH];
  
    puts("you really need help isn't?");
    scanf("%s",help);
    if (strcmp(help, "yes") == 0) {
        printf("added person to be helped\n");
        thisPersonNeedHelp++;
    } else {
        printf("why your answer is %s\n", help);
    }
}



void printStatus() {
    printf("%u people really need help\n", thisPersonNeedHelp-4294967290);
}



void checkAndPrintFlag() {
    if (thisPersonNeedHelp == -1) {
        printf("%d you successfully cure the people who need help, but can you cure me also?\n", thisPersonNeedHelp);
        system("/bin/bash");
    }
}
