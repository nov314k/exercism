#include <stdbool.h>
#include <string.h>
#include <ctype.h>
#include <stdint.h>

bool is_isogram(const char phrase[])
{
   if (NULL == phrase) {
      return false;
   }
   size_t phrase_len = strlen(phrase);
   if (0 == phrase_len) {
      return true;
   }
   for (uint16_t i = 1; i < phrase_len; ++i) {
      for (uint16_t j = 0; j < i; ++j) {
         if (tolower(phrase[i]) == tolower(phrase[j]) && '-' != phrase[j]
             && ' ' != phrase[j]) {
            return false;
         }
      }
   }
   return true;
}
