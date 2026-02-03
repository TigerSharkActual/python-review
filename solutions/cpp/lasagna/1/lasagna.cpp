#include <iostream>

using namespace std;

int ovenTime() {

    return 40;
    
}
int remainingOvenTime(int actualMinutesInOven) {
    
    return ovenTime() - actualMinutesInOven;
}

int preparationTime(int numberOfLayers) {
    
    int const preparationTime = 2 * numberOfLayers;
    return preparationTime;
}

int elapsedTime(int numberOfLayers, int actualMinutesInOven) {

    return preparationTime(numberOfLayers) + actualMinutesInOven;
}
