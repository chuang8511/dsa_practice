#!/bin/bash

# Declare variables to capture argument values
ProblemType="$1"
PlatformNumber="$2"

# Create the directory structure with appropriate formatting
mkdir "${ProblemType}/${PlatformNumber}"  

# Create empty Python files with proper extensions
touch "${ProblemType}/${PlatformNumber}/solution.py"

# Check if ProblemType is "tree"
if [ "$ProblemType" == "tree" ]; then
    # Copy tree_node.py and test_solution.py if true
    cp "tree/leetcode_104/tree_node.py" "${ProblemType}/${PlatformNumber}/tree_node.py"
    cp "tree/leetcode_104/test_solution.py" "${ProblemType}/${PlatformNumber}/test_solution.py"
elif [ "$ProblemType" == "linkedList" ]; then
    cp "linkedList/leetcode_2095/linked_list.py" "${ProblemType}/${PlatformNumber}/linked_list.py"
    cp "linkedList/leetcode_2095/test_solution.py" "${ProblemType}/${PlatformNumber}/test_solution.py"
else
    # Create an empty test_solution.py if ProblemType is not "tree"
    cp "test_code_sample.py" "${ProblemType}/${PlatformNumber}/test_solution.py"
fi