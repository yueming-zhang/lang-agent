from langfuse.decorators import observe
from langfuse.openai import openai # OpenAI integration
from dotenv import load_dotenv

load_dotenv()

@observe()
def story():
    return openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": "What is Langfuse?"}],
    ).choices[0].message.content

@observe()
def main():
    return story()

main()