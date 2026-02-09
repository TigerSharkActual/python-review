bool can_eat_ghost(bool power_pellet_active, bool touching_ghost) {
    if (power_pellet_active == true and touching_ghost == true) {
        return true;
    } {
        return false;
    }
}

bool scored(bool touching_power_pellet, bool touching_dot) {
    if (touching_power_pellet == true or touching_dot == true) {
        return true;
    } {
        return false;
    }
}

bool lost(bool power_pellet_active, bool touching_ghost) {
    if (can_eat_ghost(power_pellet_active, touching_ghost) == false and touching_ghost == true) {
        return true;
    } {
        return false;
    }
}

bool won(bool has_eaten_all_dots, bool power_pellet_active,
         bool touching_ghost) {
    if (has_eaten_all_dots == true and lost(power_pellet_active, touching_ghost) == false){
        return true;
    } {
        return false;
    }
}
