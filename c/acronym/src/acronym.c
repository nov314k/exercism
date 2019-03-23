#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#define MAX_NUMOF_CHARS 1024

char *abbreviate(char *phrase)
{
   if (phrase == NULL || strcmp(phrase, "") == 0) {
      return NULL;
   }
   /* Given (relatively simple) test examples, we don't beneift much
    * by using a more flexible data structure.  */
   char *tla = (char *)malloc(MAX_NUMOF_CHARS * sizeof(char));
   /* First character can be a space.  */
   unsigned int tla_counter = 0;
   if (isalpha(phrase[0])) {
      tla[tla_counter] = toupper(phrase[0]);
      ++tla_counter;
   }
   size_t phrase_len = strlen(phrase);
   for (unsigned int i = 0; i < phrase_len - 1; ++i) {
      /* There may be two (or more) consecutive spaces between words.  */
      if ((phrase[i] == ' ' || phrase[i] == '-') && isalpha(phrase[i + 1])) {
         tla[tla_counter] = toupper(phrase[i + 1]);
         ++tla_counter;
      }
   }
   tla[tla_counter] = '\0';
   return tla;
}
