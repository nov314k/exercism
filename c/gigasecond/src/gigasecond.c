#include "gigasecond.h"

time_t gigasecond_after(time_t given_seconds_since_epoch)
{
   return (given_seconds_since_epoch + 1e9);
}
