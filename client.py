from google import genai
from google.genai import types
import webbrowser

client = genai.Client(api_key="YOUR_API_KEY")

def ask_gemini(prompt):
    try:
        # If the user wants YouTube search
        if "search for" in prompt.lower():
            query = prompt.lower().replace("search for", "").strip()
            youtube_url = (
                "https://www.youtube.com/results?search_query=" + query.replace(" ", "+")
            )
            webbrowser.open(youtube_url)
            return f"Searching YouTube for: {query}"

        # Otherwise, talk to Gemini
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
            config=types.GenerateContentConfig(
                tools=[
                    types.Tool(
                        code_execution=types.ToolCodeExecution()
                    )
                ]
            )
        )

        return response.text

    except Exception as e:
        return f"Error: {str(e)}"
