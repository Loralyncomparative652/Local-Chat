import streamlit as st
import json # TODO заменить на SQLite, чтобы не иметь конфликтов... а так же в принципе выучить SQLite синтакиси

# === SETTINGS ===
HISTORY_B = 'History_b.json'
HISTORY_C = 'History_c.json' # TODO вторая страница, где будет HISTORY_C, просто не через Форму Постинга, а только через chat_input, в то время как его убрать из /b/

st.set_page_config(page_title='Local Chat MichiTheCat', page_icon='💬', layout='centered')
History = []
with open(HISTORY_B, 'a') as f: f.close()
with open(HISTORY_C, 'a') as f: f.close()
def LoadHistory(history):
    global History
    try:
        with open(history, 'r', encoding='utf-8') as f: History = json.load(f)
        if not History:
            History = [{'ID': 0, 'Пользователь': 'System', 'Контент': 'Тестовое системное сообщение'}]
    except:
        History = [{'ID': 0, 'Пользователь': 'System', 'Контент': 'Тестовое системное сообщение'}]
LoadHistory(HISTORY_B)

def SaveHistory(history):
    global History
    with open(history, 'w', encoding='utf-8') as f:
        json.dump(History, f, ensure_ascii=False, indent=2)

UserSendAnon = st.chat_input('Написать как "Анон"...')
if UserSendAnon:
    History.append({'ID': (History[-1]['ID'])+1, 'Пользователь': 'Анон', 'Контент': UserSendAnon})
    SaveHistory(HISTORY_B)
    st.success('Сообщение отправлено!')
    st.rerun()

st.title('/b/') # TODO исправить ReadMe.md на актуальную версию
st.dataframe(History)
st.markdown('### Форма постинга')
with st.form('registration_form'):
    UserName = st.text_input('Прозвище')
    UserMessage = st.text_input('Сообщение')
    UserSend = st.form_submit_button('Отправить')
if UserSend:
    if not UserMessage:
        st.error('Нельзя отправить пустое сообщение!')
    else:
        History.append({'ID': len(History)+1, 'Пользователь': (UserName if UserName else 'Анон'), 'Контент': UserMessage})
        SaveHistory(HISTORY_B)
        st.success('Сообщение отправлено!')
        st.rerun()
if st.button('Обновить сообщения'):
    st.rerun()
st.markdown('''
---
Ссылки на автора:

[![Telegram](https://img.shields.io/badge/Telegram-@TeaTechnology-26A5E4?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/TeaTechnology)
            
[![GitHub](https://img.shields.io/badge/GitHub-MichiTheCat--RedStar-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/MichiTheCat-RedStar)
            
[![Itch.io](https://img.shields.io/badge/Itch.io-michi--the--cat-FA5C5C?style=for-the-badge&logo=itch.io&logoColor=white)](https://michi-the-cat.itch.io)
''')
