#include <string>
using namespace std;

namespace log_line {
    string message(const string& line) {
        auto const start_index_for_task_one_string = line.find(' ');
        string new_string_task_one = line.substr(start_index_for_task_one_string + 1);
        return new_string_task_one;
    }

    string log_level(const string& line) {
        auto const start_index_task_two_string = line.find('[');
        auto const end_index_task_two_string = line.find(']');
        string new_string_task_two = line.substr(start_index_task_two_string + 1, end_index_task_two_string - 1);
        return new_string_task_two;
    }

    string reformat(const string& line) {
        string reformated_string_task_three = message(line) + " (" +  log_level(line) + ")";
        return reformated_string_task_three;

    }
}
