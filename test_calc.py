## This will test that the model is actually predicting the right species. 

from calc import predict_species

def test_species_setosa():
    # testing the first row does equal setosa
    sepal_length = 5.1 
    sepal_width = 3.5
    petal_length = 1.4
    petal_width= 0.2
    # final sum
    final_species= predict_species(sepal_length, sepal_width, petal_length, petal_width)
    assert final_species == 'setosa'
