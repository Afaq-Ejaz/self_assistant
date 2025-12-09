from google import genai 
import webbrowser

client = genai.Client(api_key="AIzaSyDl8UqjHwy5pDYmnFN7kod2M34sSsCvVPk")

def ask_gemini(prompt):
    try:
        # Handle YouTube searches
        if "search for" in prompt.lower():
            query = prompt.lower().replace("search for", "").strip()
            youtube_url = "https://www.youtube.com/results?search_query=" + query.replace(" ", "+")
            webbrowser.open(youtube_url)
            return f"Searching YouTube for: {query}"

        # Send prompt to Gemini
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
            config={
                "tools": [
                    {
                        "code_execution": {}
                    }
                ]
            }
        )

        return response.text

    except Exception as e:
        return f"Error: {str(e)}"
