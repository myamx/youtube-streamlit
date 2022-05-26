import streamlit as st
import time

st.title('Streamlit 超入門')

st.write('プログレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'Done!!!!!'

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('right')

expander1 = st.expander('問い合わせ1')
expander1.write('問い合わせ内容を書く')
expander2 = st.expander('問い合わせ2')
expander2.write('問い合わせ内容を書く')
# text = st.text_input('あなたの趣味を教えて下さい。')
# text = st.text_input('あなたの趣味を教えて下さい。')
# 'あなたの趣味：', text

# condition = st.sidebar.slider('あなたの今の調子は？', 0, 100, 50)
# condition = st.slider('あなたの今の調子は？', 0, 100, 50)
# 'コンディション：', condition
# option = st.selectbox(
#     'あなたが好きな数字を教えて下さい、',
#     list(range(1, 11)),
# )

# 'あなたの好きな数字は、', option, 'です'

# if st.checkbox('Show Image'):
#     img = Image.open('005.jpg')
#     st.image(img, caption='Fuka', use_column_width=True)
#st.write('DataFrame')

# df = pd.DataFrame(
#     np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
#     columns=['lat', 'lon']
# )
#st.table(df.style.highlight_max(axis=0))
#st.bar_chart(df)
#df
# st.map(df)