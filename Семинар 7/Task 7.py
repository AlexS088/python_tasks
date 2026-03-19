st = input()
max_sym = ""
counter = 0
for i in st:
    st_counter = st.counter(i)
    if st_counter > counter:
        counter = st_counter
print(counter) # не работает
   