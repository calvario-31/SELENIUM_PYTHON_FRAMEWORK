from faker import Faker


def get_random_user_info():
    faker = Faker()
    firstname = faker.first_name()
    lastname = faker.last_name()
    zipcode = faker.postcode()

    user_data = {
        "firstname": firstname,
        "lastname": lastname,
        "zipcode": zipcode
    }

    return [user_data]
