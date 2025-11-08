import streamlit as st

st.set_page_config(
    page_title='Bingo', 
    layout='wide', 
    page_icon='🎉'
)

if 'antigos' not in st.session_state:
    st.session_state.antigos = []

if 'input_key_id' not in st.session_state:
    st.session_state.input_key_id = 0

A, B = st.columns([1, 2], gap="large") 

st.markdown('''
    <style>
        .class_que_nao_saba {
            display: flex;        
            justify-content: center;  
            align-items: center;      
            height: 60vh; 
            font-size: 300px;
            font-weight: 900;
            color: #333333; 
            background-color: #ffe066; 
            border-radius: 20px;
            box-shadow: 0 10px 20px rgba(0,0,0,0.15);
            margin-top: 20px;
        }

        .ola {
            display: flex;          
            justify-content: center;  
            align-items: center;      
            min-height: 10vh;    
            color: #d90429; 
        }

        .stTextInput, .stTextArea {
            height: 68px;
        }

        .stTextArea label, .stTextInput label {
            visibility: hidden; 
        }
        .stButton button {
            background-color: #2a9d8f;
            color: white;
            border-radius: 8px;
            padding: 10px 20px;
            font-weight: bold;
            margin-right: 10px;
        }
        
    </style>
''', unsafe_allow_html=True)


with A:
    st.markdown('<div style="font-size: 27px; font-weight: bold;">Próximo Número:</div>', unsafe_allow_html=True)
    
    numero = st.text_input(
        '', 
        key=st.session_state.input_key_id, 
        help='Insira o número do Bingo aqui'
    )
    
    col_send, col_back = st.columns(2)

    with col_send:
        botao1 = st.button('Enviar Número')

    with col_back:
        botao2 = st.button('Voltar')
    
    if botao1:
        if numero and numero.strip():
            st.session_state.antigos.append(numero.strip())
            st.session_state.input_key_id += 1 
            st.rerun() 
        else:
            st.warning("Por favor, insira um valor antes de enviar.")
    
    if botao2:
        try:
            st.session_state.antigos.pop(-1)
            st.session_state.input_key_id += 1
            st.rerun()
        except IndexError:
            st.error("Não é possível voltar, a lista de números chamados está vazia.")


    st.markdown("---")
    st.markdown(f"**Números Chamados ({len(st.session_state.antigos)}):**")
    
    if st.session_state.antigos:
        if len(st.session_state.antigos) > 4:
            st.session_state.antigos.pop(0)
        st.markdown(f"<p style='font-size: 175px;'>{', '.join(st.session_state.antigos[::-1])}</p>", unsafe_allow_html=True)
    else:
        st.info("Nenhum número foi chamado ainda.")


with B:
    st.markdown('<h1 class="ola" style="font-size: 100px;">Último Número:</h1>', unsafe_allow_html=True)
    
    if st.session_state.antigos:
        ultimo_numero = st.session_state.antigos[-1]
    else:
        ultimo_numero = "BINGO" 

    st.markdown(f'<div class="class_que_nao_saba">{ultimo_numero}</div>', unsafe_allow_html=True)
