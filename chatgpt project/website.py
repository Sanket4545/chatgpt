from flask import Flask, render_template, request
import openai
from apikey import APIKEY

app = Flask(__name__)

# Set OpenAI API key
openai.api_key = APIKEY

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form['user_input']
        
        # Generate completion using GPT-3.5 model
        output_gpt3 = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", 
            messages=[{"role": "user", "content": user_input}]
        )
        completion_gpt3 = output_gpt3['choices'][0]['message']['content']
        
        # Generate completion using another language model (e.g., GPT-4)
        # Replace "YOUR_OTHER_API_KEY" with your actual API key for the other model
        # openai.api_key = "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"
        # output_other_model = openai.Completion.create(
        #     engine="gpt-3.5-turbo",  # Replace with your desired model
        #     prompt=user_input,
        #     max_tokens=150
        # )
        # completion_other_model = output_other_model['choices'][0]['text']
        
        return render_template('index.html', user_input=user_input, completion_gpt3=completion_gpt3)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
