from google import genai
from google.genai import types
import webbrowser

client = genai.Client(api_key="AIzaSyDl8UqjHwy5pDYmnFN7kod2M34sSsCvVPk")

response = client.models.generate_content(
  model='gemini-2.0-flash',
  contents='you are a  assistant that will open various sites that are not defined in the code '
           'Generate and give the efficient response response.',
  config=types.GenerateContentConfig(
    tools=[types.Tool(
      code_execution=types.ToolCodeExecution
    )]
  )
)
 
import google.generativeai as genai  # Correct import

# Configure API key
genai.configure(api_key="AIzaSyDl8UqjHwy5pDYmnFN7kod2M34sSsCvVPk")  

# Function to generate AI response
def ask_gemini(prompt):
    try:
        # Check if user wants to search on YouTube
        if "search for" in prompt.lower():
            query = prompt.lower().replace("search for", "").strip()
            youtube_url = f"https://www.youtube.com/results?search_query={query.replace(' ', '+')}"
            webbrowser.open(youtube_url)  # Open YouTube search
            return f"Searching YouTube for {query}..."

        # Otherwise, use Gemini API
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)
        return response.text  # Return AI response

    except Exception as e:
        return f"Error: {e}"  # Handle API errors
        