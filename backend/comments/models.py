from django.db import models

class Comment(models.Model):
    text = models.TextField()               # The actual text of the comment
    sentiment = models.CharField(max_length=20)   # The sentiment (e.g., 'positive', 'negative', 'neutral')
    created_at = models.DateTimeField(auto_now_add=True)  # When the comment was fetched

    def __str__(self):
        return self.text[:50]  # Show the first 50 characters in the admin panel
