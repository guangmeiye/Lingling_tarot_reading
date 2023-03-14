from django.db import models

class ChatGPTConnection(models.Model):
    API_KEY_CHOICES = [
        ('davinci', 'Davinci'),
        ('curie', 'Curie'),
        ('babbage', 'Babbage'),
        ('ada', 'Ada'),
    ]

    name = models.CharField(max_length=255)
    api_key = models.CharField(max_length=255, choices=API_KEY_CHOICES)
    max_tokens = models.PositiveIntegerField(default=1024)
    temperature = models.DecimalField(max_digits=4, decimal_places=2, default=0.7)
    frequency_penalty = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    presence_penalty = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "ChatGPT Connections"

    def __str__(self):
        return self.name
