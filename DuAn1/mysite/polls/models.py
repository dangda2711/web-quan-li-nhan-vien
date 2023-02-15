from django.db import models
# ánh xạ cơ sở dữ liệu vào python
# Create your models here.
class Question(models.Model):
    question_text= models.CharField(max_length=200)
    time_pub= models.DateTimeField()
class Choice(models.Model):
    question= models.ForeignKey(Question, on_delete=models.CASCADE)# câu hỏi bị xóa đi thì câu trả lời bị xóa đi
    choice_text =models.CharField(max_length=100)
    vote= models.IntegerField(default=0)