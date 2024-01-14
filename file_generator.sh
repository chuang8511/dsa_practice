#!/bin/bash

# Declare variables to capture argument values
ProblemType="$1"
PlatformNumber="$2"

# Create the directory structure with appropriate formatting
mkdir "${ProblemType}/${PlatformNumber}"  

# Create empty Python files with proper extensions
touch "${ProblemType}/${PlatformNumber}/solution.py"
touch "${ProblemType}/${PlatformNumber}/test_solution.py"