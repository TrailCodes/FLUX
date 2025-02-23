import FLUX.FLUX as FLUX

while True:
    text = input('FLUX > ')
    result, error = FLUX.run('<stdin>', text)

    if error: print(error.as_string())
    else: print(result)