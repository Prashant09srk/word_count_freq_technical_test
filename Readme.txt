To build this program, I adapted a test-driven development (TDD) approach, where test cases were created initially to cover all possible scenarios.
The code was then developed incrementally to satisfy each test case,ensuring the program's correctness and robustness.


Below are the assumptions which were made while writing the code -

1) File Format: The program assumes that the input file is in the .txt format. 
             If a file with a different extension is provided, the program will raise an exception.

2) File Content: The input file should not be empty and must contain at least one word. 
              It should not consist solely of special characters or numbers.

3) Handling Special Characters and Numbers: The program handles special characters and numbers by excluding them from the word count. 
                                         They are not considered as part of the output.

4) Handling Single Characters: Single characters are not considered as words and will not be included in the output.

5) Sorting Words with the Same Frequency: If multiple words have the same frequency, they will be sorted alphabetically in the output.

Please also have a look over the Test cases and flowchart provided along with this file.