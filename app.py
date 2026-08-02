from dotenv import load_dotenv
import os
from crewai import LLM,Agent,Task,Crew,Process

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

product_description_task = Task(
    description=(
            "Analyze the product provided below:\n\n"
            "Product name: {product_name}\n"
            "Product category: {product_category}\n"
            "Target customer: {target_customer}\n"
            "Main features: {main_features}\n\n"
            "Use only the information provided about the product."
            "Do not invent missing specifications or make unsupported claims."
            ),

    expected_output=(
            "Generate a product report in Markdown format with the following sections:\n"
            "1. Product Title\n"
            "2. Short Description\n"
            "3. Main Features\n"
            "4. Customer Benefits\n"
            "5. Ideal Customer\n"
            "6. Recommended Usage\n"
            "7. Missing Information"
            ),
    agent=product_description_agent
)
