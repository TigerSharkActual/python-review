#include <string>
using namespace std;

namespace log_line {
    string message(const string& line) {
        return line.substr(line.find(':') + 2);
    }

    string log_level(const string& line) {
        auto const start = line.find('[') + 1;
        auto const stop = line.find(']');
        auto const length = stop - start;
        return line.substr(start, length);
    }

    string reformat(const string& line) {
        return message(line) + " (" +  log_level(line) + ")";
    }
}
