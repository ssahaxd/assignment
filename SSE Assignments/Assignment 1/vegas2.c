#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>

#define BUFSIZE 100


long increment(long in) {
	return in + 1;
}

long get_random() {
	return rand() % BUFSIZE;
}

int do_stuff() {
	long ans = get_random();
	ans = increment(ans);
	long const_canary = 0x55555555;
	
	printf("What number would you like to guess?\n");
	char guess[32];
	fgets(guess, BUFSIZE, stdin);
	
	long g = atol(guess);
	if (!g) {
		printf("That's not a valid number!\n");
	} else {
		if (const_canary = 0x55555555 && g == ans) {
			printf("Congrats! You win! Your prize is this print statement!\n\n");
			return 1;
		} else {
			printf("Nope!\n\n");
		}
	}
	return 0;
}

void win(int reward) {
	char winner[BUFSIZE];
	printf("New winner!\nName? ");
	fgets(winner, 360, stdin);
	printf("Congrats %s\n\n", winner);
	printf("Your reward is %d\n\n", reward);
}

int main(int argc, char **argv){
	setvbuf(stdout, NULL, _IONBF, 0);
	// Set the gid to the effective gid
	// this prevents /bin/sh from dropping the privileges
	gid_t gid = getegid();
	setresgid(gid, gid, gid);
	
	int res;
	int reward = 1;
	
	printf("Welcome to my guessing game!\n\n");
	
	while (1) {
		res = do_stuff();
		if (res) {
			reward += reward;
			win(reward);
		}
		if (reward >= 1000000) break;
	}
	
	return 0;
}
