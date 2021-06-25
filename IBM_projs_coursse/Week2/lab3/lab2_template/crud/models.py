from django.db import models
from django.db.models.query_utils import select_related_descend
from django.utils.timezone import now
from django.utils.translation import to_language

# Define your models from here:

#User Model
class User(models.Model):
    first_name = models.CharField(null=False, max_length=30, default='john')
    last_name = models.CharField(null=False, max_length=30, default='doe')
    dob = models.CharField(null=True, max_length=10)

    #Create a tostring method for object string representation
    def __str__(self):
        return self.first_name + " " + self.last_name

#Instructor Model
class Instructor(User):
    full_time = models.BooleanField(default=True)
    total_learners = models.IntegerField()

    #Create a tostring tmethod for object string representation
    def __str__(self):
        return "First name: " + self.first_name + ", " + \
                "Last name: " + self.last_name + ", " \
                "Is full time: " + str(self.full_time) + ", "\
                "Total Learners: " + str(self.total_learners)

#Learner Model
class Learner(User):
    STUDENT = 'student'
    DEVELOPER = 'developer'
    DATA_SCIENTIST = 'data_scientist'
    DATABASE_ADMIN = 'dba'
    OCCUPATION_CHOICES = [
        (STUDENT, 'Student'),
        (DEVELOPER, 'Developer'),
        (DATA_SCIENTIST, 'Data Scientist'),
        (DATABASE_ADMIN, 'Database Admin')
    ]
    occupation = models.CharField(
        null = False,
        max_length=20,
        choices=OCCUPATION_CHOICES,
        default=STUDENT
    )
    social_link = models.URLField(max_length=200)

    #Create a toString method for object string representation
    def __str__(self):
        return "First name: " + self.first_name + ", " +\
            "Last name: " + self.last_name + ", " +\
            "Date of Birth " + self.dob + ", "+\
            "Occupation " + self.occupation + ", "+\
            "Social Link" + self.social_link

#Course Model
class Course(models.Model):
    name = models.CharField(null=False, max_length=100, default='online course')
    description = models.CharField(max_length=500)
    #Many-to-Many relationship with Instructor
    instructors = models.ManyToManyField(Instructor)
    #Many-to-Many relationship with Learner via Enrollment relationship
    learners = models.ManyToManyField(Learner, through='Enrollment')

    #Create a toString method for object string representation
    def __str__(self):
        return "Name: " + self.name + ", " +\
            "Description: " + self.description

#Lesson Model
class Lesson(models.Model):
    title = models.CharField(max_length=240, default='title')
    course = models.ForeignKey(Course, null=True, on_delete=models.CASCADE)
    content = models.TextField()

#Enrollment model as a lookup table with additional enrollment info
class Enrollment(models.Model):
    AUDIT = 'audit'
    HONOR = 'honor'
    COURSE_MODES = [
        (AUDIT, 'Audit'),
        (HONOR, 'Honor')
    ]
    #Add a learner Foreign Key
    learner = models.ForeignKey(Learner, on_delete=models.CASCADE)
    #Add a course Foreign Key
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    #Enrollment date
    date_enrolled = models.DateField(default=now)
    #Enrollment mode
    mode = models.CharField(max_length=5, choices=COURSE_MODES, default=AUDIT)