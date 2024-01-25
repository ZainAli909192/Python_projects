import openai
openai.api_key="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";
num=1;
try :
    while num:
        model_engine="text-davinci-003"
        prompt=input('Enter new prompt:');
        if 'exit' in prompt or 'quit' in prompt:
            print("See you later")
            break;
        completion=openai.Completion.create(
            engine=model_engine,
            prompt=prompt,
            max_tokens=1024,
            n=0, stop=None,
            temperature=0.5
        )
        response=completion.choices[0].text
        print(response);
except Exception as e:
        print("Error:", e)
