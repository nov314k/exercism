#include "gigasecond.h"

time_t gigasecond_after(time_t seconds_since_epoch)
{
   return (seconds_since_epoch + 1e9);
}
