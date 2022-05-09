def key(alpha=None, k=None, errors):
    assert(alpha or k)

    result = 0
    if (alpha):

        for (i=0; i < len(errors) - 1; i++):
            result = result + (errors[i+1] / errors[i] ^ alpha)

        return result / len(errors)
    else:
        for (i=0; i < len(errors) - 1; i++):
            result = result + (math.ln(errors[i+1]/k) / math.ln(errors[i]))

        return result / len(errors)
