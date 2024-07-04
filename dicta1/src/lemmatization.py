import re
from transformers import AutoModel, AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained('dicta-il/dictabert-tiny-joint')
model = AutoModel.from_pretrained('dicta-il/dictabert-tiny-joint', trust_remote_code=True, do_ner=False, do_prefix=False, do_morph=False)

model.eval()

def lemmitize(text: str, batch_size=16) -> list:
    split_text = re.split('[.!?]', text)
    split_text = [s.strip() for s in split_text if s.strip()]
    output = []
    for i in range(0, len(split_text), batch_size):
        batch = split_text[i:i + batch_size]
        preds = model.predict(batch, tokenizer, output_style='json')
        lemmas = [item['lex'] if item['lex'] != '[BLANK]' else item['token'] for pred in preds for item in pred['tokens']]
        output.extend(lemmas)
    return output


