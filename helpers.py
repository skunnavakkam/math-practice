def confidence (attempts, accuracy):
    # making the middle confidences less confidenct, and people who get extremes more confident
    coefficient = accuracy**2 - accuracy + 1
    return (coefficent/(2 * attempts))

