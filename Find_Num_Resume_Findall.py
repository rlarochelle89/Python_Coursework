#This function searches text for batman/batwoman w/ regular expressions

import re

resume = '''RAYMOND LAROCHELLE
Chicago, IL
408-528-5883, 309-369-3048
rlarochelle89@gmail.com
www.linkedin.com/in/raymond-m-larochelle/
https://github.com/rlarochelle89

SUMMARY

•	Confident foundation in analytic tools such as Excel, Tableau, SQL, and Python 
•	Advanced quantitative degrees, including Ph.D. from San Diego State University 
•	Proven track record of communicating information in user-friendly language 
•	Designed studies, collected and analyzed data, and reported findings for 13 major research projects
•	Highly recommended by most recent manager and colleague on LinkedIn 

Skills include: 

Excel | Tableau | Python | SQL | R | Word | PowerPoint | Statistical Analysis | Statistical Modeling | Predictive Analytics | Data Analysis | Data Visualization | Data Management | Data Cleaning | Dashboard Creation | Research | Presentation | Report Writing | Teaching 

EXPERIENCE

Data Scientist, Aug, 2018 – Present
University of Delaware, Newark, DE and Remote
•	Investigated the efficacy of a novel early field experience for student teachers. My work supported the institutionalization of this field experience at the university as well as 4 published scientific reports and 6 conference presentations.
•	Collaborated with Principal Investigator (PI) Management Team to design studies, including methods for collecting, analyzing, and reporting on data
•	Managed data, including creating Excel tables to clean, structure, and validate data
•	Identified trends and insights in data by computing statistical models, predictive analytics, and descriptive statistics with Excel 
•	Led and managed a team of 3 research assistants to analyze over 120 interviews with preservice teachers for one project, and assisted in data analysis for 6 other projects
•	Provided recommendations to stakeholders with varying degrees of technical knowledge, such as administrators, student teachers, and other researchers
•	Assisted in writing annual reports for project evaluators
•	Ensured research met ethical standards by coordinating with Institutional Review Board 

University Instructor, Aug, 2018 – May, 2021
University of Delaware, Newark, DE and Remote
•	Taught foundational math and mathematics education courses to university students 
•	Created syllabi, oversaw learning management systems, and assisted in credential program evaluations

Graduate Student Data Scientist, Aug, 2013 – May, 2018
San Diego State University Research Foundation, San Diego, CA
•	Investigated teachers’ abilities to make sense of students’ mathematical thinking
•	Collaboratively designed studies, collected and analyzed data, presented findings at national and international conferences, and published results in peer-reviewed journals

Graduate Student Teaching Assistant, Aug, 2013 – Dec, 2017
San Diego State University, San Diego, CA
•	Taught foundational math and mathematics education courses to university students 
•	Created syllabi and oversaw learning management systems

EDUCATION

Ph.D. Mathematics Education, Jun, 2018
San Diego State University and UC San Diego
•	Dissertation: Secondary Teachers’ Professional Noticing of Students’ Mathematical Thinking in Proportional Reasoning Tasks
•	Awards: Nicholas Branca Memorial Scholarship, Graduate Student Association Travel Grant, Sowder Research Award, President’s Award at Student Research Symposium

M.A. Mathematics, May, 2013
American University

B.S. in Mathematics, Jun, 2011
University of California, Santa Barbara

PROFFESSIONAL DEVELOPMENT

Online Coursework at Udemy.com    Remote.    Oct, 2021 – Present
•	Currently enrolled in “Automate the Boring Stuff with Python.”
•	Completed Data Scientist and Data Analyst courses in SQL, Python, and Tableau
•	Independently practicing data analysis and scientist skills on Github

Mathematics and Groupwork Workshop    University of Arizona.    Jun, 2018
•	Learned instructional techniques for supporting effective group work 

Communicating your Research Workshop    UC San Diego.    Sep, 2017
•	Learned effective and compelling strategies to communicate my research

Grant Writing Workshop     San Diego State University.    Feb, 2017 - Mar, 2017
•	Learned strategies and techniques for searching for funding and writing grants

VOLUNTEER EXPERIENCE

Associate Vice President of Sponsorship, Feb, 2021 – Present
Association of Mathematics Teacher Educators
•	Recruited sponsors for annual conference and negotiated sponsorship contracts

Conference Organizer, Feb, 2019 – Feb, 2021
Association of Mathematics Teacher Educators    
•	Planned and facilitated exhibit hall where vendors would exhibit their materials
•	Collaboratively planned and assisted conference events

Conference Organizer, Feb, 2016 – Jan, 2018
Greater San Diego Mathematics Council
•	Recruited vendors to exhibit materials at annual conference and negotiated contracts
•	Planned and facilitated exhibit hall where vendors would exhibit their materials
•	Collaboratively planned and assisted conference events
'''

phoneRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneRegex.findall(resume)
print(mo)
