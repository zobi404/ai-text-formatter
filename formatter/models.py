from django.db import models

class TextHistory(models.Model):
    raw_text = models.TextField()
    formatted_html = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Formatted Text {self.id} - {self.created_at.strftime('%Y-%m-%d %H:%M')}"
