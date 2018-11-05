# Q12

To get the right answer for this, we need to consider some possible values for variables such as stop, start, step.
At Start = 0, Stop = 10, Step = 1
	max(0 , ( 10 – 0 + 1 – 1 ) //1 )
	max(0 , (10) // 1)
	max(0 , 10)  10
At Start = 0, Stop = 10, Step = 2
	max(0 , ( 10 – 0 + 2 – 1 ) //2 )
	max(0 , (11) // 2)
	max(0 , 5)  5
At Start = 10, Stop = 55, Step = 4
	max(0 , ( 55 – 10 + 4 – 1 ) //4 )
	max(0 , (48) // 4)
	max(0 , 12)  12
      For Negative Step:
At Start = 10, Stop = 0, Step = -1
	max(0 , ( 0 – ( –10) + (–1) – 1 ) //–1 )
	max(0 , (10 - 2) // –1)
	max(0 , -8)  0 (Error Condition) 
