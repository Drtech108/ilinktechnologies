from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"



class Registration(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    interests = models.TextField(blank=True)
    agreed_to_terms = models.BooleanField(default=False)

    def __str__(self):
        return self.full_name
