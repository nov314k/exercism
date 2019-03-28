#ifndef SPACE_AGE_H
#define SPACE_AGE_H

#include <stdint.h>

enum planet {
   EARTH, MERCURY, VENUS, MARS, JUPITER, SATURN, URANUS, NEPTUNE
};

double convert_planet_age(enum planet planet, uint64_t age_in_seconds);

#endif                          /* SPACE_AGE_H  */
