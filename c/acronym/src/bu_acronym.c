#include <stdio.h>
#include <string.h>
#include <ctype.h>
#define MAX_NUMOF_CHARS 100

char *abbreviate(char *phrase)
main(void)
{
    char phrase[MAX_NUMOF_CHARS];
    if (fgets(phrase, sizeof phrase, stdin)) {
        phrase[strcspn(phrase, "\n")] = '\0';
    }
    /* First character can be a space.  */
    if (isalpha(phrase[0])) {
        printf("%c", toupper(phrase[0]));
    }
    size_t phrase_len = strlen(phrase);
    for (unsigned int i = 0; i < phrase_len - 1; ++i) {
        /* There may be two (or more) consecutive spaces between words.  */
        if (phrase[i] == ' ' && isalpha(phrase[i + 1])) {
            printf("%c", toupper(phrase[i + 1])); 
        }
    }
    printf("\n");
    return 0;
}
