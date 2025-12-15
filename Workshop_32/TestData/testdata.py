


from faker import Faker

fake_obj = Faker()

course_title = fake_obj.sentence(nb_words=4)
course_price = "99.99"
course_description = "Mytest course description"



# name = fake_obj.name()
# email_ex = fake_obj.email()
# username = fake_obj.user_name(),
# password_ex = "11111111"
