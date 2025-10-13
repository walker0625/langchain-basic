from dotenv import load_dotenv

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PDFPlumberLoader
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

# 0. util 함수 및 키 세팅
def format_docs_join(docs):
    
    tmp_docs = []
    
    for doc in docs:
        tmp_docs.append(doc.page_content)
    
    return '\n\n\---\n\n'.join(tmp_docs)

# API KEY 정보로드
load_dotenv()

# 1. 문서 로드
loader = PDFPlumberLoader('../data/Sustainability_report_2024_kr.pdf')
docs = loader.load()

# 2. 문서 분할
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
chunks = text_splitter.split_documents(docs)

# 3. 임베딩
embeddings = OpenAIEmbeddings()

# 4. DB 생성 및 retriever 불러오기
retriever = FAISS.from_documents(documents=chunks, embedding=embeddings).as_retriever()

# 5. 프롬프트 세팅
prompt = ChatPromptTemplate.from_messages([
    ('system', """
    주어진 context만 근거로 간결하고 정확하게 대답해줘
    context에 없으면 문서에 '근거 없음'이라고 대답
    
    # Context
    {context}
    """
    
    ),
    ('human', '{question}')
])

llm = ChatOpenAI(model='gpt-4.1-mini', temperature=0)

chain = (
    {
    'context': retriever | format_docs_join,
    'question': RunnablePassthrough()
    }
    | prompt
    | llm 
    | StrOutputParser()
)

result = chain.invoke('CEO 메시지 뭐야')
print(result)