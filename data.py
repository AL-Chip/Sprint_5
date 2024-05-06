import faker


def get_email():
    fake = faker.Faker()
    email = fake.email()
    return email


def get_password():
    fake = faker.Faker()
    password = fake.password(7)
    return password

