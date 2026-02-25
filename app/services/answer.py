from app.utils import embed_text, retrive_context_from_db, generate_answer_from_context
import asyncio

async def generate_answer(query: str):
    #1st break the query into vector
    #2nd retrive context from vector store using query
    #3rd provide the llm context, prompt, query to generate answer
    loop = asyncio.get_event_loop()
    query_embedding = await loop.run_in_executor(None, embed_text, [query]) 
    context, sources = retrive_context_from_db(query_embedding[0]) 

    answer = await generate_answer_from_context(query, context)  

    return answer, sources