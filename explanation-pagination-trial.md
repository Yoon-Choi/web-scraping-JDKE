Generally, when you implement pagination,
need to find regularity between html page address
like this : p=2, p=3

##### My idea was to combine seperated part with variable x. 

- first of all, seperate 3 parts as follows: 

   prefix = 'glassdoor.com/Job/berlin-junior-data-analyst-jobs-SRCH_IL.0,6_IC2622109_KO7,26_IP'

   tail = '.htm?includeNoSalaryJobs=true&pgc=AB4'

   variable = x   # x is int variable. str(x)  

- and then combine components 

    url = prefix + str(x) + tail

##### if page number is 2, the url would be like this: 

     'glassdoor.com/IP2.htm?includeNoSalaryJobs=true&pgc=AB4'
   

##### if page number is 3, the url would be : 

     'glassdoor.com/IP3.htm?includeNoSalaryJobs=true&pgc=AB4'


But after address comparison between tail parts of glassdoor job search pages,
I got to realized that pagination is quite difficult to implement at this moment (address encryption)


there are inregularity between pages as follows:

#### tail of page3
    '.htm?includeNoSalaryJobs=true&pgc=AB4AAoEAPAAAAAAAAAAAAAAAAbRcco4AKgEBAQ8AlE1esmV0jt%2FpCqGBFZoL9moV1PR7XNrKpC6nXSnUERn2vpv9XQAA'

#### tail of page4
    '.htm?includeNoSalaryJobs=true&pgc=AB4AAYEAHgAAAAAAAAAAAAAAAbRcco4AIgEBAQgPG0n5W3yk2WozQf8jOnTwWfP3zR77GSVMT1lHQEYAAA%3D%3D'


### Conclusion 
I will expand the project to other webpage, and would try out pagination agian 

