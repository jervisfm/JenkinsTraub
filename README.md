Jervis Muindi   
Numerical Algorithms and Complexity    
April 2013
Homework 13

Introduction
============
This project contains code that implement a general purpose polynomial root-finding solver using both Newton iteration (with convergence of order 2) and a 3-point iteration given below: 

	x_(i+1) = x_i -u(x_i) + (u(x_i) * f(x_i - u(x_i))) / ( 2*f(x_i - u(x_i))  - f(x_i) )

where u(x_i) is defined as follows: 

	u(x_i) = f(x_i) / f'(x_i)



How to Run
==========
<pre>
python main.py [x0]   
     x0 : Initial x-point to use           
</pre>

For Example:    

`python main.py 0.98`   


Sample Output
============
Below is some sample output obtained from running the script on input 0.98 
<pre>

Using Initial X-value : 0.98
Finding Roots using both Newton Iteration and 3-point Iteration
1) Newton=1.004396367438787 | 3-Point-Iteration=1.000059112603294
2) Newton=1.000178099644882 | 3-Point-Iteration=1.000000000000004
3) Newton=1.000000300959787 | 3-Point-Iteration=1.000000000000000
Stopping Iteration. We're progressing slower than 0.001000 per loop

</pre>



Discussion
==========
From the sample output given about, we can see that indeed, the 3-point iteration is much faster at converging towards the solution than the plain newton iteration is. In fact, by only the third iteration, it already converged onto the answer of 1.0 whereas Newton did not. Also, note that the iteration was terminated because the progress being made (by Newton in this case) was smaller than 0.001 per loop - further evidence of its slow speed. 

Thus, I conclude that there is indeed a noticeable difference between the convergence time between plain newton iteration and the given 3-point iteration. The 3-point iteration converges more quickly towards to the root than plain newton iteration. 

These observations are in agreement with the claim that the 3-point iteration enjoys order 4 convergence compared to order 2 convergence for newton. 