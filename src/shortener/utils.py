import string, random
#from shortener.models import ShawtyURL
# ^ will cause ImportError. Cannot import the class, as models.py is already importing utils.py. No importing an import.
# Instead, retrieve class name using instance.__class__


def generate_code(size=7, chars=string.ascii_lowercase + string.digits):
    new_code = ''
    for _ in range(size):
        new_code += random.choice(chars)
    return new_code

def create_unique_code(instance, size=7):
    new_code = generate_code(size=size)
    Klass = instance.__class__
    qs_exists = Klass.objects.filter(shortcode=new_code).exists()
    if qs_exists:
        return create_unique_code(size=size)
    return new_code
