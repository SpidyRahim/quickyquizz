from django.db.models import Avg
from Quiz.models import Quiz
from .forms import StudentReviewForm
from .models import StudentReview
from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
from django.http import HttpResponse
from Quiz import models as qmodel
from signup import models as signupModel
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import logout
from django.http import HttpResponseRedirect

# Create your views here.


def is_student(user):
    return user.groups.filter(name='STUDENT').exists()


@login_required(login_url='slogin')
@user_passes_test(is_student)
def student_d(request):
    def student_dashboard(request):
        quizes = qmodel.Quiz.objects.all()
        student = signupModel.Student.objects.get(user_id=request.user.id)
        return render(request, 'student_dashboard.html', {'quizes': quizes, 'name': student})
    return student_dashboard(request)


@login_required(login_url='slogin')
@user_passes_test(is_student)
def attempt(request, pk):
    quiz = qmodel.Quiz.objects.get(id=pk)
    questions = qmodel.Question.objects.all().filter(quiz_id=pk)
    if request.method == 'POST':
        pass
    response = render(request, 'attempt.html', {
                      'quiz': quiz, 'questions': questions})
    response.set_cookie('quiz', quiz.id)
    return response


@login_required(login_url='slogin')
@user_passes_test(is_student)
def grades(request):
    student = signupModel.Student.objects.get(user_id=request.user.id)
    results = qmodel.Result.objects.all().filter(student=student)
    return render(request, 'grades.html', {'results': results})


def stud_logout_view(request):
    logout(request)
    return redirect('../')


@login_required(login_url='slogin')
@user_passes_test(is_student)
def calculate_marks(request):
    if request.COOKIES.get('quiz') is not None:
        quiz_id = request.COOKIES.get('quiz')
        quiz = qmodel.Quiz.objects.get(id=quiz_id)
        total_marks = 0
        questions = qmodel.Question.objects.all().filter(quiz=quiz)
        for i in range(len(questions)):
            selected_ans = request.COOKIES.get(str(i+1))
            actual_answer = questions[i].answer
            if selected_ans == actual_answer:
                total_marks = total_marks + 1
        student = signupModel.Student.objects.get(user_id=request.user.id)
        result = qmodel.Result()
        result.correct = total_marks
        result.exam = quiz
        result.student = student
        result.qCount = len(questions)
        result.save()
        return HttpResponseRedirect('grades')


# def review_quiz(request, quiz_id):
#     quiz = Quiz.objects.get(id=quiz_id)
#     student = request.user.student

#     if request.method == 'POST':
#         form = StudentReviewForm(request.POST)
#         if form.is_valid():
#             review = form.save(commit=False)
#             review.student = student
#             review.quiz = quiz
#             review.save()
#             # Redirect to the grades page after submitting the review
#             return redirect('grades')
#     else:
#         form = StudentReviewForm()

#     return render(request, 'review.html', {'quiz': quiz, 'form': form})

# def review_quiz(request, quiz_id):
#     quiz = Quiz.objects.get(id=quiz_id)
#     student = request.user.student

#     if request.method == 'POST':
#         form = StudentReviewForm(request.POST)
#         if form.is_valid():
#             review = form.save(commit=False)
#             review.student = student
#             review.quiz = quiz
#             review.save()

#             # Calculate the new rating average for the quiz
#             ratings = StudentReview.objects.filter(quiz=quiz)
#             total_rating = sum(review.rating for review in ratings)
#             new_rating_average = total_rating / len(ratings)

#             # Update the rating_average field of the quiz
#             quiz.rating_average = new_rating_average
#             quiz.save()

#             # Redirect to the grades page after submitting the review
#             return redirect('grades')
#     else:
#         form = StudentReviewForm()

#     return render(request, 'review.html', {'quiz': quiz, 'form': form})


def review_quiz(request, quiz_id):
    quiz = Quiz.objects.get(id=quiz_id)
    student = request.user.student

    if request.method == 'POST':
        form = StudentReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.student = student
            review.quiz = quiz
            review.save()

            # Calculate the new rating average for the quiz
            ratings = StudentReview.objects.filter(quiz=quiz)
            total_rating = sum(review.rating for review in ratings)
            number_of_reviews = len(ratings)
            new_rating_average = total_rating / number_of_reviews

            # Update the rating_average field of the quiz
            quiz.rating_average = new_rating_average
            quiz.save()

            # Redirect to the grades page after submitting the review
            return redirect('grades')
    else:
        form = StudentReviewForm()

    return render(request, 'review.html', {'quiz': quiz, 'form': form})


def student_dashboard(request):
    quizes = qmodel.Quiz.objects.annotate(
        rating_average=Avg('studentreview__rating'))
    student = signupModel.Student.objects.get(user_id=request.user.id)
    return render(request, 'student_dashboard.html', {'quizes': quizes, 'name': student})


# notun shuru
# from django.shortcuts import render
# from .models import Result  # Import the Result model
# from signup.models import Student
# from django.contrib.auth.decorators import login_required, user_passes_test

# # ... (other imports and views) ...

# from django.db.models import Avg, Count
# from django.db import models


# @login_required(login_url='slogin')
# @user_passes_test(is_student)
# def leaderboard(request):
#     # Retrieve all quizzes that the student has attempted
#     student = signupModel.Student.objects.get(user_id=request.user.id)
#     attempted_quizzes = qmodel.Result.objects.filter(student=student).values('exam')
    
#     # Retrieve leaderboard data for attempted quizzes
#     leaderboard = qmodel.Result.objects.filter(exam__in=attempted_quizzes).annotate(
#         student_name=models.F('student__user__username'),
#         quiz_name=models.F('exam__quiz_name'),
#         score_percentage=models.ExpressionWrapper(models.F('correct') * 100 / models.F('qCount'), output_field=models.FloatField())
#     ).order_by('-score_percentage')
    
#     return render(request, 'leaderboard.html', {'leaderboard': leaderboard})



# views.py


from django.db.models import Avg, Count
from .models import Result
from signup.models import Student
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render
from django.db import models

# ...

# @login_required(login_url='slogin')
# @user_passes_test(is_student)
# def leaderboard(request):
#     # Retrieve all quizzes that the student has attempted
#     student = signupModel.Student.objects.get(user_id=request.user.id)
#     attempted_quizzes = qmodel.Result.objects.filter(student=student).values('exam')

#     # Retrieve leaderboard data for attempted quizzes
#     leaderboard = qmodel.Result.objects.filter(exam__in=attempted_quizzes).annotate(
#         student_name=models.F('student__user__username'),
#         quiz_name=models.F('exam__quiz_name'),
#         score_percentage=models.ExpressionWrapper(models.F('correct') * 100 / models.F('qCount'), output_field=models.FloatField())
#     ).order_by('-score_percentage')

#     return render(request, 'leaderboard.html', {'leaderboard': leaderboard})



from django.shortcuts import render
from .models import Result
from signup.models import Student
from django.contrib.auth.decorators import login_required, user_passes_test


@login_required(login_url='slogin')
@user_passes_test(is_student)
def leaderboard(request):
    student = signupModel.Student.objects.get(user_id=request.user.id)
    attempted_quizzes = qmodel.Result.objects.filter(student=student).values('exam__quiz_name').distinct()
    
    # Create an empty dictionary to store leaderboard data
    leaderboard = {}
    
    # Iterate through attempted quizzes
    for quiz_name in attempted_quizzes:
        quiz_name = quiz_name['exam__quiz_name']
        quiz_results = qmodel.Result.objects.filter(student=student, exam__quiz_name=quiz_name).order_by('-correct')
        
        # Calculate rank for each student within the quiz
        rank = 0
        prev_score = None
        quiz_leaderboard = []
        
        for result in quiz_results:
            if prev_score is None or result.correct < prev_score:
                rank += 1
            
            # Append student's data to the quiz leaderboard
            quiz_leaderboard.append({
                'student_name': result.student,
                'score_percentage': (result.correct * 100) / result.qCount,
                'rank': rank
            })
            
            prev_score = result.correct
        
        # Store the quiz leaderboard data in the dictionary
        leaderboard[quiz_name] = quiz_leaderboard
    
    return render(request, 'leaderboard.html', {'leaderboard': leaderboard})



#notun likhtesi
from signup.forms import StudentUserForm
from .forms import ProfileForm
def profile(request,id):
    std = Student.objects.get(pk = id)
    form = ProfileForm(instance=std)
    if request.method == 'POST':
        std = ProfileForm(request.POST)
        if std.is_valid():
            std.save()
            redirect('sdashboard')
    return render(request, 'profile.html', {'form': form})