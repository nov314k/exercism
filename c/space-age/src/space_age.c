#include "space_age.h"
#define NUMOF_PLANETS 8
#define EARTH_YEAR_IN_SECONDS 31557600.0

static const double earth_year_multiple[NUMOF_PLANETS] =
    { 1.0, 0.2408467, 0.61519726, 1.8808158, 11.862615, 29.447498, 84.016846,
164.79132
};

double convert_planet_age(enum planet planet, uint64_t age_in_seconds)
{
   return age_in_seconds / earth_year_multiple[planet] / EARTH_YEAR_IN_SECONDS;
}
