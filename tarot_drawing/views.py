from django.shortcuts import render
import os
import openai


openai.api_key = os.environ['OPENAI_API_KEY']


def tarot_drawing(request):
    if request.method == 'POST':
        # Get the key sentence from the request POST data
        key_sentence = request.POST.get('key_sentence', '')

        # Generate a response using the ChatGPT API
        response = openai.Completion.create(
            engine='davinci',
            prompt=key_sentence,
            max_tokens=1024,
            temperature=0.7,
            frequency_penalty=0,
            presence_penalty=0
        )

        # Extract the generated text from the response
        answer = response.choices[0].text

        # Render the template with the generated answer
        return render(request, 'tarot_drawing.html', {'answer': answer})

    else:
        # Render the template with an empty form
        return render(request, 'tarot_drawing.html', {})
