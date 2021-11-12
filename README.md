Research Track Assignment 1 [12.11.2021] by Maciej Bogdalski
================================


Installing and running
----------------------

The simulator requires a Python 2.7 installation, the [pygame](http://pygame.org/) library, [PyPyBox2D](https://pypi.python.org/pypi/pypybox2d/2.1-r331), and [PyYAML](https://pypi.python.org/pypi/PyYAML/).

Run the program with:

```bash
$ python2 run.py mySolution.py
```


Description and pseudo-code
----------------------

The program is desired to make the robot spot the silver tokens, avoiding touching or moving the golden ones at the same time. Robot comes towards a silver token, grabs it, rotates 180 degress and drops it, then moves to the next marker. 
In order to make the robot avoid golden markers, it scans its neighbourhood constantly and corrects its own movement. Its "unnatural" moves are caused by designing its scanner to scan in a certain radius, while the whole environment was designed using rather rectangular shapes. It fullfills its task however, without making mistakes. 


```bash
simulation keeps executing:
	scan the environment for silver and golden tokens - scan on the left and on the right
	calculate the average distances for both sides
	if the silver token is close enough:
		move towards the silver token and grab it
	elif average distance on the right > average distance on the left:
		turn right 
	elif  average distance on the left > average distance on the right:
		turn left
	drive
```



The environment
----------------------

![image](https://user-images.githubusercontent.com/91498765/141461177-de0a459b-f97d-4fc5-b039-fb7d7638dcb8.png)


