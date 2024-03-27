## What is dsa practice?
It helps us to create the template of the code to practice the DSA problem.

## Why do we need this repo?
There is no built-in function to swap tree to array, and vice versa.
It increases the complexity to write the test code for your practice.
So, with dsa-practice, you can easily write test code.

## How do you add your practice code with test code?
1. generate the files that you need. 
  - You can check which type the problem belongs to.
  - You can get problems from different platforms. So, I recommend to name the directory_name as platform_number
  - e.g. leetcode_100
  $ sh file_generator.sh type_of_problem directory_name
  e.g. $ sh file_generator.sh stack leetcode_9999

2. Add the code into your solution.py file.
3. modify the test code by using the method provided in solution.py
4. run your test code
  - $ sh t_e.sh type_of_problem/directory_name
  e.g. $ sh t_e.sh stack/leetcode_9999

## What's more?
Now, to practice other TypeScript, I also build the directory, TS.
In the directory, it is also easy to write the test code and solution.
But, now, there isn't the shell file to execute the generation of the new files.