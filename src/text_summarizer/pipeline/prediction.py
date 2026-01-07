from transformers import AutoTokenizer, pipeline

class PredictionPipeline:
    def __init__(self):
        # Using a standard robust model for the web app to ensure it works out of the box
        self.model_name = "facebook/bart-large-cnn"
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.summarizer = pipeline("summarization", model=self.model_name, tokenizer=self.tokenizer)

    def predict(self, text):
        gen_kwargs = {"length_penalty": 2.0, "num_beams": 4, "max_length": 142, "min_length": 30}
        
        print("Dialogue:")
        print(text)

        output = self.summarizer(text, **gen_kwargs)[0]["summary_text"]
        print("\nModel Summary:")
        print(output)

        return output
