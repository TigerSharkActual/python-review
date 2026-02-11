#include <string>
using namespace std;

namespace log_line {
    string message(const string& line) {
        return line.substr(line.find(' ') + 1);
    }

    string log_level(const string& line) {
        return line.substr(line.find('[') + 1, line.find(']') - 1);
    }

    string reformat(const string& line) {
        return message(line) + " (" +  log_level(line) + ")";
    }
}
