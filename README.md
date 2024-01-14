In this project, we write Python code for Boolean algebra and functions. Much of the present project mirrors work done in the project Propositional Logic and Truth Tables.

[1] Define and implement the seven operators b_not, b_and, b_or, b_xor, b_nand, b_nor, b_xnor as 0/1 boolean functions (not T/F). Consider all to be binary (degree 2) functions except b_not which is unary (degree 1):
  
[2] Rewrite the truth_table function from Assignment 1 for 0/1 boolean algebra and call it boolean_table.

[3] Rewrite the analyze_truth_table function from Assignment 1 for 0/1 boolean algebra and call it analyze_boolean_table. As your starting point, use the enhanced version from class on September 6. Omit the part about tt_type (tautology, contingency, contradiction). You may want to reverse the binary string (using binary[::-1]) before converting it to a decimal number, as that may better align the result with the function number. 

[4] Rewrite functions f0 thru f15 from Assignment 1 as 0/1 boolean functions. It is not necessary to include the other functions from that assignment (De Morgan's Laws, Modus Ponens, Modus Tollens, and Hypothetical Syllogism).  

[5] Run analyze_boolean_table looping over those 16 functions. Use a dictionary to keep track of which functions resulted in which binary number. Verify that all 16 numbers were each produced once and only once.

[6] Define a function that, using the method discussed in class, reverse-engineers a 0/1 boolean table into a function that yields that table's output column. 

[7] Write a function half_adder(x, y) that uses the functions created in Task [1] as "gates" and produces the s (sum) and c (carry) outputs per the table in the slides.
