import FLUX

while True:
    text = input('FLUX > ')
    result, error = FLUX.run('<stdin>', text)

    if error:
        print(error.as_string())
    elif result is None:
        print("An unexpected error occurred, no result returned.")
    else:
        print(result)