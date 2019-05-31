#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdint.h>
#define MAX_NUMOF_CHARS 1024

char *abbreviate(const char *phrase)
{
   if (NULL == phrase || 0 == strcmp(phrase, "")) {
      return NULL;
   }
   /* Given test examples, this fixed-size data structure should suffice.  */
   char *tla = malloc(MAX_NUMOF_CHARS * sizeof(char));
   if (NULL == tla) {
      printf("Memory allocation failed!");
      abort();
   }
   uint16_t tla_index = 0;
   if (isalpha(phrase[0])) {    /* First character can be a space.  */
      tla[tla_index] = toupper(phrase[0]);
      ++tla_index;
   }
   size_t phrase_len = strlen(phrase);
   for (uint16_t i = 0; i < phrase_len - 1; ++i) {
      /* There may be two (or more) consecutive spaces between words.  */
      if ((' ' == phrase[i] || '-' == phrase[i]) && isalpha(phrase[i + 1])) {
         tla[tla_index] = toupper(phrase[i + 1]);
         ++tla_index;
      }
   }
   tla[tla_index] = '\0';
   return tla;
}
