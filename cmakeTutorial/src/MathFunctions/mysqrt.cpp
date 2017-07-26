#include "MathFunctions.hpp"
#include "TutorialConfig.hpp"
#include <stdio.h>
#include "Table.hpp"

double mysqrt(double x)
{
	if (x <= 0)
	{
		return 0;
	}

	double result;

#if defined(HAVE_LOG) && defined(HAVE_EXP)
	result = exp(log(x) * 0.5);
	fprintf(stdout, "Computing sqrt of %g to be %g using log\n", x,result);
#else
	if (x >= 1 && x < 10)
		result = sqrtTable[static_cast<int>(x)];
	else
		result = x;

	double delta;	
	int i;
	for (i = 0; i < SQRT_ITERATIONS; ++i)
	{
		if (result <= 0)
			result = 0.1;
		delta = x - (result * result);
		if (delta < SQRT_THRESHOLD)
			break;
		else
		{
			result = result + 0.5 * delta / result;
			fprintf(stdout, "Computing sqrt of %g to be %g\n", x, result);
		}
	}
#endif
	return result;
}

