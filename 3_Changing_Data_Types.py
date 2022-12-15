f_one = s_one = t_one = int(1)
print("f_one:", f_one, type(f_one), id(f_one))
print("s_one:", s_one, type(s_one), id(s_one))
print("t_one:", t_one, type(t_one), id(t_one))
print(f_one == s_one == t_one)
print("=" * 50)


f_two = str(1)
s_two = str(1)
print("f_two:", f_two, type(f_two), id(f_two))
print("s_two:", s_two, type(s_two), id(s_two))
print(f_two == s_two)
print("=" * 50)


f_one = str(f_one)
s_one = str(s_one)
t_one = str(t_one)
print("f_one:", f_one, type(f_one), id(f_one))
print("s_one:", s_one, type(s_one), id(s_one))
print("t_one:", t_one, type(t_one), id(t_one))
print(f_one == s_one == t_one)
print("=" * 50)


f_two = s_two = str("1")
print("f_two:", f_two, type(f_two), id(f_two))
print("s_two:", s_two, type(s_two), id(s_two))
print(f_two == s_two)
