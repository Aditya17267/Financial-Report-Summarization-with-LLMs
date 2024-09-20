from utils.config.paths import get_paths
from utils.config.environment import load_environment
from utils.text_extraction.file_operations import process_pdfs
from utils.openai.document_loader import load_documents
from utils.openai.database_setup import setup_database
from utils.openai.text_splitting import split_text_documents
from utils.openai.prompt_template import create_prompt_template
from utils.openai.text_processing import save_text_to_docx
from langchain_openai import ChatOpenAI
from langchain_core.runnables import RunnableSequence
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.retrieval import create_retrieval_chain
import logging
import shutil

logging.basicConfig(level=logging.INFO)

def main():
    load_environment()
    
    #take inputs from user
    pdf_directory, output_text_file, output_docx_file, output_1_pager, vector_db_directory = get_paths()
    
    #extracts data from pdfs and writes to .txt file
    if pdf_directory and output_text_file and output_docx_file and vector_db_directory:
        process_pdfs(pdf_directory, output_text_file)
        
        #splitting extracted text into chunks
        text_documents = load_documents(output_text_file)
        if text_documents:
            split_documents = split_text_documents(text_documents)
            
            #setup the vector database
            db = setup_database(split_documents, vector_db_directory)
            if db:
                logging.info("Database setup complete.")
                retriever = db.as_retriever()
                
                # Create prompt template
                prompt_template = create_prompt_template()
                if prompt_template:
                    logging.info("Prompt template created.")
                    
                    # Initialize LLM and chains
                    llm = ChatOpenAI(model="gpt-4o-mini-2024-07-18", temperature=0.0)
                    llm_chain = RunnableSequence(prompt_template | llm)
                    combine_docs_chain = create_stuff_documents_chain(llm, prompt_template)
                    retrieval_chain = create_retrieval_chain(retriever, combine_docs_chain)

                    # Invoke retrieval chain
                    try:
                        # Generating 2 page summary
                        response = retrieval_chain.invoke({
                            "input": """
                                Use the vectors present in database. If not present, say that the data is not present. Use bullet points only for sales data. For others, use paragraphs. Limit the total response to 325 to 350 words.
                                    
                                Give Company's Business overview. Include information such as the company's formation/incorporation date, headquarters location, business description, employee count, latest revenues, stock exchange listing and market capitalization, number of offices and locations, and details on their clients.
                                    
                                Business Segment Overview
                                Extract the revenue percentage of each component (verticals, products, segments, and sections) as a part of the total revenue.
                                Performance: Evaluate the performance of each component by comparing the current year's sales perrevenue and market share with the previous year's numbers.  
                                Sales Increase/Decrease explanation: Explain the causes of the increase or decrease in the performance of each component.
                                    
                                    
                                Breakdown of sales and revenue by geography, specifying the percentage contribution of each region to the total sales.
                                    
                                Summarize geographical data, such as workforce, clients, and offices, and outline the company's regional plans for expansion or reduction.
                                    
                                Analyze and explain regional sales fluctuations, including a geographical sales breakdown to identify sales trends.
                                    
                                Year-over-year sales increase or decline and reasons for the change
                                    
                                Summary of rationale & considerations (risks & mitigating factors)
                                    
                                SWOT Analysis
                                    
                                Information about credit rating/credit rating change/change in the rating outlook.
                                    
                            """})
                        logging.info("Response from retrieval chain obtained.")

                        # Saving 2 page summary
                        save_text_to_docx(response['answer'], output_docx_file)

                        # Generating 1 page summary
                        response_1 = retrieval_chain.invoke({"input": f"Summarize the following from bullet points to paragraphs that convey the picture of the points. \n {response['answer']}"})

                        logging.info("Response from retrieval chain obtained.")

                        # Saving 1 page summary
                        save_text_to_docx(response_1['answer'], output_1_pager)

                        try:
                            #to avoid stagnation of database we delete the vector database.
                            shutil.rmtree(vector_db_directory)
                        except OSError as e:
                            print("Error: %s - %s." % (e.filename, e.strerror))

                    except Exception as e:
                        logging.error(f"Error invoking retrieval chain: {e}")
                else:
                    logging.error("Failed to create prompt template.")
            else:
                logging.error("Failed to set up the database.")
        else:
            logging.error("Failed to load documents from the text file.")
    else:
        logging.error("Invalid paths provided.")

if __name__ == "__main__":
    main()

