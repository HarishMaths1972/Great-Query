from imports import *

page_setup()

if 'model' not in st.session_state:
    st.session_state['model'] = ChatOpenAI(temperature=0, model="gpt-4o-mini",api_key=st.secrets['OPENAI_API_KEY'])

model = st.session_state['model']

with st.sidebar:
    uploaded_files = st.file_uploader("Upload the CSV files and the metadatas", type=["csv","txt"],accept_multiple_files=True)
    upload = st.button("Upload :mushroom:")
                                         
if upload and uploaded_files:
    with st.sidebar:
        with st.spinner("Uploading"):
            save(uploaded_files)
    
if 'df' in st.session_state:
    df = st.session_state['df']

if 'metadata' in st.session_state:
    meta = st.session_state['metadata'].readlines()
    meta = json.dumps([i.strip() for i in meta])

    base_prompt = hub.pull("langchain-ai/openai-functions-template")
    inst = instructions.format(meta=meta)
    prompt = base_prompt.partial(instructions=inst)

tools = [PythonAstREPLTool(globals = globals().copy())]

if 'df' in st.session_state and 'agent' not in st.session_state:
    st.session_state['agent'] = AgentExecutor(agent=create_openai_functions_agent(
            model,
            tools = tools,
            prompt = prompt
        ),
        tools = tools,
        verbose = True
    )

if 'agent' in st.session_state:
    agent = st.session_state['agent']
    
query = st.text_input("Enter your query")

if query and 'agent' in st.session_state:
    try:
        response = agent.invoke({"input":query+"\n"+suffix})
    except:
        st.info("Unable to process")