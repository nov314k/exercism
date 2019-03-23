#include <stdbool.h>
#include <string.h>
#include <ctype.h>

bool is_isogram(const char phrase[])
{
   if (phrase == NULL) {
      return false;
   }
   size_t phrase_len = strlen(phrase);
   if (phrase_len == 0) {
      return true;
   }
   for (unsigned int i = 1; i < phrase_len; ++i) {
      for (unsigned int j = 0; j < i; ++j) {
         if (tolower(phrase[i]) == tolower(phrase[j]) && phrase[j] != '-'
             && phrase[j] != ' ') {
            return false;
         }
      }
   }
   return true;
}
