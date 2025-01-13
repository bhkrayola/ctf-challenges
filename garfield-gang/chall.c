#include <stdio.h>
#include <unistd.h>

#define FLAG_SIZE 256
#define FLAG_FILE "./flag.txt"

void BESTIES_ONLY()
{
    char buf[FLAG_SIZE];
    memset(buf, 0, FLAG_SIZE);
    FILE *f = fopen(FLAG_FILE, "r");
    if (f == NULL)
        printf("Missing flag file! Please contact an officer if you see this error on the remote target!\n");
    else
    {
        fgets(buf, FLAG_SIZE, f);
        printf("\n");
        write(STDOUT_FILENO, buf, strlen(buf));
        printf("\n");
    }
    exit(0);
}

void GARFIELD_AUTH_6000()
{
    printf("\n---\n>>> GARFIELD GANG AUTHENTICATION MODULE v1.0 (DEV) <<<\n---\n\n");
    printf("WELCOME AGENT: GARFIELD FRIEND #183892349 \n");
    printf("SELECT CLEARANCE LEVEL #(1-6): ");
    
    int level;
    scanf("%i", &level);

    if (level > 6)
    {
INVALID:
        printf("[INVALID LEVEL]!\n");
        exit(0);
    }
    switch ((short)level)
    {
        case 1:
            printf("[CLEARANCE LEVEL 1]\nwenomechainsama\n");
            break;
        case 2:
            printf("[CLEARANCE LEVEL 2]\nwifenloof\n");
            break;
        case 3:
            printf("[CLEARANCE LEVEL 3]\neselifterbraun\n");
            break;
        case 4:
            printf("[CLEARANCE LEVEL 4]\ni hate mondays \n");
            break;
        case 5:
            printf("[CLEARANCE LEVEL 5]\ni hate mondays \n");
            break;
        case 6:
            printf("[CLEARANCE LEVEL 6]\ni hate mondays \n");
            break;
        case 1337:
            printf("[GARFIELD'S SECRET]\n");
            BESTIES_ONLY();
            break;
        default:
            goto INVALID;
    }
}

int main (int argc, char *argv[])
{
    setvbuf(stdin,  NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
    
    GARFIELD_AUTH_6000();
    return 0;
}
