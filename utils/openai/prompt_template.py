from langchain.prompts import PromptTemplate
import logging

logging.basicConfig(level=logging.INFO)

def create_prompt_template():
    """
    Create the prompt template for summarizing financial reports.
    
    Returns:
        PromptTemplate: A configured prompt template.
    """
    try:
        template = """
        You are a senior financial analyst with over 20 years of experience in evaluating company financials, including 10-K reports and financial analyst reports.
        Answer based on the context provided. Please ensure the summary is concise, accurate, and covers all the specified sections. Use bullet points for clarity and make sure to include specific data points where applicable.
        context: {context}
        input: {input}
        ANSWER
        """
        return PromptTemplate.from_template(template)
    except Exception as e:
        logging.error(f"Error creating prompt template: {e}")
        return None
