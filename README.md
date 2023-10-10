# Quiz Time! 🧑‍🏫
This online quiz platform allows teachers to create quizzes and students to attempt them in their comfort zones.  

***
### Functionality 
  #### Teacher
  * Create an account as a teacher
  * After login can view a dashboard with all the available quizzes
  * Add new questions to the existing quiz
  * Create new quizzes and add questions
  * Review created quizzes
  * Delete quizzes
  #### Student
  * Create an account as a student
  * After login can view a dashboard with all the available quizzes
  * Attempt any quiz
  * View grades of all the attempted quizzes
 *** 
### How to Run the Project 
  * Install Python 
  * Install `Django 4.1.2`
  
  ```
  pip install Django
  ```
  * Download the poroject to your local machine 
  * Open a terminal from the project directory and run the below commands
  
  ```
  pip install mysql-connector-python-rf
  pip install pymysql
  pip install django-widget-tweaks
  ```
  
  * Open `settings.py` and add `widget-tweaks` to `INSTALLED_APPS` as below;

  ```python
  INSTALLED_APPS += [
    'widget_tweaks',
  ]
  ```
 * Create a php MySQL Database as `quizdb`
 * Run the following commands to do the database migrations

 ```
 python manage.py makemigrations
 python manage.py migrate
```
 * Run the server
 
 ```
 python manage.py runserver
 ```
 * Now you can view the project using the below URL

```
http://127.0.0.1:8000/
```
***
### Further Work
 * Include an admin panel
 * Let teachers view the grades of students
 * Let students view the correct answers 

***
### Web App User Interface 
#### Landing Page
![landing](/UI-Screenshots/landing.png "Landing Page")
#### Teacher Dashboard
![landing](/UI-Screenshots/teacher-dash.png "Landing Page")
#### Student Dashboard
![landing](/UI-Screenshots/student-dash.png "Landing Page")
#### Attempt Quiz
![landing](/UI-Screenshots/attempt-quiz.png "Landing Page")
#### View Grades
![landing](/UI-Screenshots/grades.png "Landing Page")
