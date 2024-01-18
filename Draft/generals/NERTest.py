import spacy
from spacy.training.example import Example

# Load a blank English model
nlp = spacy.blank("en")
ner = nlp.add_pipe("ner")

# Add 'O' label to the NER component
ner.add_label("O")

# Training data example
training_data = [
    ("I visited a beautiful house yesterday.", {"entities": [(19, 24, "PROPERTY_TYPE")]}),
    # Add more training examples
]

# Training loop
for text, annotations in training_data:
    example = Example.from_dict(nlp.make_doc(text), annotations)
    nlp.update([example], drop=0.5)

# Save the trained model
nlp.to_disk("ner_model")

# Test the model
loaded_nlp = spacy.load("ner_model")
doc = loaded_nlp("I'm considering buying an apartment.")
print([(ent.text, ent.label_) for ent in doc.ents])



import spacy

# Load the spaCy model
nlp = spacy.blank("en")

# Add 'O' label to the NER component
ner = nlp.add_pipe("ner")
ner.add_label("O")

loaded_nlp = spacy.load("ner_model")
print(loaded_nlp.pipe_names)  # Check the components in the pipeline
print(loaded_nlp.get_pipe("ner").labels)  # Check the labels in the NER component
