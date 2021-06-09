for i in range(2, 21):
    for(j) in range(10):
        with open(f"E:/python/08/tables/Multiplication_table_of_{i}.txt", 'w') as f:
            for j in range(1, 11):
                f.write(f"{i} X {j} = {i*j} \n")
                if j!=10:
                    f.write('\n')