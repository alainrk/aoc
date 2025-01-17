# Advent of Code

## Usage

### Setup

```py
# Create venv
python3 -m venv venv

# Activate venv
source venv/bin/activate

# Install requirements
python3 -m pip install -r requirements.txt
```

### Create another day

```py
./new [YYYY] [DD]
```

### Run a specific day

```py
# Where input_file:
#   - If not given will take YYYY/DD/input.txt
#   - If given as simple string e.g. "test" will take YYYY/DD/test.txt
#   - If given as full path, it will be used that instead (use absolute path)
#
# And module file:
#   - If not given will take main (YYYY/DD/main.py)
#   - If given (only as module name e.g. "mainPt2") will take main (YYYY/DD/mainPt2.py)
#
# Examples:
# ./run 2024 01
# ./run 2024 12
# ./run 2024 19 -i test
# ./run 2024 22 -i /tmp/input.txt
# ./run 2024 23 -f mainPt2
# ./run 2024 22 -i /tmp/input.txt -f mainPt2
./run [YYYY] [DD] [-i input_file] [-f module_name]
```
