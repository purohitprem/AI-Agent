from dotenv import load_dotenv
import os
from crewai import LLM,Agent

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("GEMINI API KEY NOT FOUND!!")

llm = LLM(
    model='gemini/gemini-2.5-flash',
    api_key=GEMINI_API_KEY,
    temperature=0.3
)

product_description_agent = Agent(
    role= "Product Description Specialist",
    goal=(
            "Given product information ko understand karke clear, useful "
            "aur customer-friendly product description create karna."
        ),
    backstory=(
        "You are an experienced ecomprce content specialist."
        "You convert simple product details into clear product descriptions."
        "You never invent technical specifications that are not provided"
        ),
    llm=llm,
    verbose=False,
    allow_delegation=False
)