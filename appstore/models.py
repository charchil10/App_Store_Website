from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.user', on_delete = models.CASCADE)
    appsName = models.CharField(max_length=40, unique= True)
    appsDescription = models.TextField(max_length = 1800)
    version = models.CharField(max_length = 4)
    published_date = models.DateTimeField(
        default = timezone.now)
    App_price = models.CharField(max_length =10)

    def __str__(self):
        return self.appsName
        return self.appsDescription
        return self.version
        return self.App_price

    def publish(self):
        self.published_date = timezone.now()
        self.save()
                                                                  
class Reviews(models.Model):
    post = models.ForeignKey('appstore.Post', related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    CHOICES = [(i,i) for i in range(1,6)]
    ratings = models.IntegerField(choices = CHOICES)
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)
        
    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

    #for i in Reviews.objects.raw
    #def Average(self):
        #for i in Reviews.objects.raw(
            #'SELECT AVG(ratings) AS [Average Ratings] FROM Reviews'):
             # print (i)
    
