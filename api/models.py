from django.db import models

class Stack(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    private = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.name

class Card(models.Model):
    front = models.TextField()
    back = models.TextField()
    stack = models.ForeignKey(Stack, on_delete=models.CASCADE, related_name="cards")

    def __str__(self):
        return self.front